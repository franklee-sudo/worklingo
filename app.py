import os
import json
import sqlite3
import requests
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='.')

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DB_PATH = "worklingo.db"

# Supabase Config
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
USE_SUPABASE = bool(SUPABASE_URL and SUPABASE_KEY)

if USE_SUPABASE:
    print(f"✅ Using Supabase Storage ({SUPABASE_URL})")
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    print("⚠️  Supabase credentials not found. Using local SQLite.")

def init_db():
    if USE_SUPABASE:
        # Supabase is managed via cloud dashboard, no auto-init from here usually.
        # But we can try to create a default user if not exists for demo purposes
        # Assuming table 'users' exists.
        try:
            res = supabase.table('users').select("*").eq('email', 'demo@worklingo.com').execute()
            if not res.data:
                supabase.table('users').insert({
                    "email": 'demo@worklingo.com',
                    "password_hash": 'demo_hash',
                    "username": 'Demo User'
                }).execute()
        except Exception as e:
            print(f"Supabase init warning: {e}")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create Users Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        username TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create RawInputs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS raw_inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        source_type TEXT DEFAULT 'manual_paste',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    ''')

    # Create AnalysisRecords Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analysis_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        raw_input_id INTEGER,
        scene TEXT,
        intent TEXT,
        original_text TEXT,
        refined_text TEXT,
        explanation TEXT,
        meta_data TEXT,
        status TEXT DEFAULT 'new',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (raw_input_id) REFERENCES raw_inputs(id) ON DELETE SET NULL
    )
    ''')
    
    # Create default user if not exists
    cursor.execute("SELECT * FROM users WHERE id = 1")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (email, password_hash, username) VALUES (?, ?, ?)", 
                      ('demo@worklingo.com', 'demo_hash', 'Demo User'))

    conn.commit()
    conn.close()

# Initialize DB on startup
init_db()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    if not DEEPSEEK_API_KEY:
        return jsonify({"error": "Missing API Key. Please configure DEEPSEEK_API_KEY in .env file."}), 500

    data = request.json
    user_input = data.get('text', '')

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    system_prompt = """
    你是一个资深的职场英语导师。请分析用户输入的工作沟通记录。
    1. 识别场景(Scene)和意图(Intent)。
    2. 提取核心原话(Key Expression)。
    3. 提供一个更地道、更职场化的备选表达(Better Alternative)。
    4. 提取关键词(Keywords)。
    
    请严格以 JSON 格式返回，不要包含 markdown 格式标记（如 ```json ... ```），直接返回 JSON 对象。
    JSON 结构如下: 
    {
        "scene": "string", 
        "intent": "string", 
        "keyExpression": "string", 
        "betterAlternative": "string", 
        "keywords": ["string"]
    }
    """

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                "stream": False,
                "temperature": 0.3
            },
            timeout=30
        )

        if response.status_code != 200:
            return jsonify({"error": f"DeepSeek API Error: {response.text}"}), response.status_code

        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # Clean up potential markdown formatting if DeepSeek adds it despite instructions
        if content.startswith('```json'):
            content = content[7:]
        if content.endswith('```'):
            content = content[:-3]
        
        parsed_result = json.loads(content.strip())
        return jsonify(parsed_result)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/save', methods=['POST'])
def save_result():
    data = request.json
    user_id = 1  # Hardcoded demo user
    
    raw_content = data.get('raw_content', '')
    analysis = data.get('analysis', {})
    
    if not analysis:
        return jsonify({"error": "No analysis data"}), 400

    if USE_SUPABASE:
        try:
            # 1. Save Raw Input
            raw_res = supabase.table('raw_inputs').insert({
                "user_id": user_id,
                "content": raw_content,
                "source_type": 'manual_paste'
            }).execute()
            raw_input_id = raw_res.data[0]['id']

            # 2. Save Analysis Record
            meta_data = {
                "keywords": analysis.get("keywords", [])
            }
            
            supabase.table('analysis_records').insert({
                "user_id": user_id,
                "raw_input_id": raw_input_id,
                "scene": analysis.get("scene", ""),
                "intent": analysis.get("intent", ""),
                "refined_text": analysis.get("betterAlternative", ""),
                "original_text": analysis.get("keyExpression", ""),
                "meta_data": meta_data, # Supabase handles JSON automatically
                "status": 'new'
            }).execute()
            
            return jsonify({"success": True, "id": raw_input_id})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Fallback to SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # 1. Save Raw Input
        cursor.execute(
            "INSERT INTO raw_inputs (user_id, content, source_type) VALUES (?, ?, ?)",
            (user_id, raw_content, 'manual_paste')
        )
        raw_input_id = cursor.lastrowid
        
        # 2. Save Analysis Record
        meta_data = json.dumps({
            "keywords": analysis.get("keywords", [])
        })
        
        cursor.execute('''
            INSERT INTO analysis_records 
            (user_id, raw_input_id, scene, intent, refined_text, original_text, meta_data, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id, 
            raw_input_id,
            analysis.get("scene", ""),
            analysis.get("intent", ""),
            analysis.get("betterAlternative", ""), # Map betterAlternative to refined_text
            analysis.get("keyExpression", ""),    # Map keyExpression to original_text
            meta_data,
            'new'
        ))
        
        conn.commit()
        return jsonify({"success": True, "id": cursor.lastrowid})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/api/library', methods=['GET'])
def get_library():
    user_id = 1
    
    if USE_SUPABASE:
        try:
            res = supabase.table('analysis_records') \
                .select("id, scene, intent, original_text, refined_text, meta_data") \
                .eq('user_id', user_id) \
                .order('created_at', desc=True) \
                .execute()
            
            library = []
            for row in res.data:
                # Supabase returns JSON columns as dicts directly
                meta = row['meta_data'] if row['meta_data'] else {}
                library.append({
                    "id": row['id'],
                    "scene": row['scene'],
                    "intent": row['intent'],
                    "expression": row['original_text'],
                    "alternative": row['refined_text'],
                    "keywords": meta.get("keywords", [])
                })
            return jsonify(library)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, scene, intent, original_text, refined_text, meta_data 
        FROM analysis_records 
        WHERE user_id = ? 
        ORDER BY created_at DESC
    ''', (user_id,))
    
    rows = cursor.fetchall()
    library = []
    
    for row in rows:
        meta = json.loads(row['meta_data']) if row['meta_data'] else {}
        library.append({
            "id": row['id'],
            "scene": row['scene'],
            "intent": row['intent'],
            "expression": row['original_text'],
            "alternative": row['refined_text'],
            "keywords": meta.get("keywords", [])
        })
        
    conn.close()
    return jsonify(library)

@app.route('/api/library/<int:record_id>', methods=['DELETE'])
def delete_library_item(record_id):
    user_id = 1
    
    if USE_SUPABASE:
        try:
            # Verify ownership first (optional but good practice, though row level security usually handles this)
            # For this demo, we just delete matching user_id and id
            res = supabase.table('analysis_records').delete().eq('id', record_id).eq('user_id', user_id).execute()
            
            # Check if any row was actually deleted
            if not res.data:
                 return jsonify({"error": "Record not found or not authorized"}), 404
                 
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM analysis_records WHERE id = ? AND user_id = ?", (record_id, user_id))
        if cursor.rowcount == 0:
            return jsonify({"error": "Record not found"}), 404
        conn.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Hardcoded check for demo purposes as requested
    if email == 'demo@worklingo.com' and password == 'test':
        return jsonify({
            "success": True,
            "user": {
                "id": 1,
                "email": email,
                "name": "Demo User"
            }
        })
    
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    print("Starting Worklingo Server...")
    print("Please open http://localhost:5000 in your browser")
    app.run(port=5000, debug=True)
