-- Supabase / PostgreSQL Schema for Worklingo
-- Copy and paste this into the Supabase SQL Editor

-- 1. Users Table (Simplified for demo, in production use Supabase Auth)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Raw Inputs Table (Stores original text from user)
CREATE TABLE IF NOT EXISTS raw_inputs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    content TEXT NOT NULL,
    source_type VARCHAR(20) CHECK (source_type IN ('manual_paste', 'slack', 'email', 'meeting')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Analysis Records Table (Stores structured data)
CREATE TABLE IF NOT EXISTS analysis_records (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    raw_input_id INTEGER REFERENCES raw_inputs(id),
    scene VARCHAR(100),
    intent VARCHAR(100),
    original_text TEXT,
    refined_text TEXT,
    meta_data JSONB, -- Stores keywords, tags as JSON
    status VARCHAR(20) DEFAULT 'new',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Create a Demo User (so you can test immediately)
INSERT INTO users (username, email, password_hash)
VALUES ('Demo User', 'demo@worklingo.com', 'demo_hash')
ON CONFLICT (email) DO NOTHING;
