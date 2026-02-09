# Worklingo - ASCII Prototype Design

基于 "Paste-to-Import" (手动导入) 和 "Structured Organization" (结构化整理) 的 MVP 原型设计。

## 1. 首页 / 仪表盘 (Home / Dashboard)
简洁的入口，强调"今天学了什么"和"快速开始"。

```text
+-----------------------------------------------------------------------+
|  WORKLINGO       [ Library ]  [ Practice ]  [ Settings ]      (User)  |
+-----------------------------------------------------------------------+
|                                                                       |
|   Good Morning, Frank!                                                |
|   You have collected 12 new expressions this week.                    |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |  QUICK IMPORT                                                 |   |
|   |                                                               |   |
|   |  [ Paste your text here...                                  ] |   |
|   |  [ (e.g., Slack history, Email draft, Zoom transcript)      ] |   |
|   |                                                               |   |
|   |                                       [ Analyze & Extract ]   |   |
|   +---------------------------------------------------------------+   |
|                                                                       |
|   [ Recent Collections ]                                              |
|   +--------------------------+  +--------------------------+          |
|   | Scene: Code Review       |  | Scene: Project Update    |          |
|   | Intent: Disagree politely|  | Intent: Report blocker   |          |
|   | "I see your point, but..."|  | "I'm currently blocked..."|          |
|   +--------------------------+  +--------------------------+          |
|                                                                       |
+-----------------------------------------------------------------------+
```

## 2. 导入与分析 (Import & Analysis Review)
核心功能：将非结构化文本转化为结构化数据。用户在此确认 AI 的提取结果。

```text
+-----------------------------------------------------------------------+
|  < Back to Home                                                       |
+-----------------------------------------------------------------------+
|  ANALYSIS RESULT                                                      |
|                                                                       |
|  [ Original Input ]                [ Structured Extraction ]          |
|  +------------------------+        +--------------------------------+ |
|  | Frank: Hey, I think the|  ==>   | SCENE: Software Dev / Bug Fix  | |
|  | API is returning 500.  |        |                                | |
|  | Can you check when it  |        | INTENT: Ask for ETA            | |
|  | can be fixed? We need  |        +--------------------------------+ |
|  | this for the demo.     |        |                                | |
|  |                        |        | KEY EXPRESSION (Core):         | |
|  | Bob: Checking now.     |        | [ Can you check when it can be ] |
|  | Will update you in 30m.|        | [ fixed?                       ] |
|  +------------------------+        |                                | |
|                                    | BETTER ALTERNATIVE (AI):       | |
|                                    | "Could you provide an ETA for  | |
|                                    | the fix?"                      | |
|                                    +--------------------------------+ |
|                                    | KEYWORDS:                      | |
|                                    | [x] API 500 error              | |
|                                    | [x] Demo                       | |
|                                    +--------------------------------+ |
|                                    | TAGS:  [Urgent] [Tech]         | |
|                                    +--------------------------------+ |
|                                                                       |
|                                    [ Discard ]      [ Save to Lib ]   |
+-----------------------------------------------------------------------+
```

## 3. 语料库 / 场景视图 (Knowledge Base / Scenario View)
用户查看沉淀下来的语料，按工作场景分类。

```text
+-----------------------------------------------------------------------+
|  MY LIBRARY                                            [ + Import ]   |
+-----------------------------------------------------------------------+
|  Filters: [ All Scenarios v ] [ All Intents v ]  [ Search...      ]   |
|                                                                       |
|  +----------------------+    +----------------------------------------+
|  | SCENARIOS            |    | EXPRESSIONS (Sorted by Frequency)      |
|  +----------------------+    +----------------------------------------+
|  | > All (142)          |    |                                        |
|  |                      |    | [ Code Review ] - [ Disagree ]         |
|  | > Daily Standup (45) |    | "I have a slight concern regarding..." |
|  |                      |    | Context: Discussing architecture       |
|  | > Code Review (30)   |    | -------------------------------------- |
|  |                      |    |                                        |
|  | > Client Meeting (20)|    | [ Project Mgmt ] - [ Ask ETA ]         |
|  |                      |    | "What's the timeline for this?"        |
|  | > Bug Reporting (15) |    | Context: Sprint planning               |
|  |                      |    | -------------------------------------- |
|  | > Casual Chat (10)   |    |                                        |
|  +----------------------+    | [ Bug Reporting ] - [ Clarify ]        |
|                              | "To reproduce this issue, you need..." |
|                              | Context: QA testing                    |
|                              +----------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
```

## 4. 闪卡练习模式 (Flashcard Mode)
利用碎片时间复习，强调 Context (上下文)。

```text
+-----------------------------------------------------------------------+
|  PRACTICE SESSION (5 min)                                     [ X ]   |
+-----------------------------------------------------------------------+
|                                                                       |
|   SCENE: Project Management / Delay                                   |
|                                                                       |
|   +---------------------------------------------------------------+   |
|   |                                                               |   |
|   |  CONTEXT:                                                     |   |
|   |  You are blocked by a dependency and cannot finish today.     |   |
|   |  Your manager asks for an update.                             |   |
|   |                                                               |   |
|   |  HOW WOULD YOU SAY IT?                                        |   |
|   |                                                               |   |
|   |  ( Think about it... )                                        |   |
|   |                                                               |   |
|   |                  [ Show Answer ]                              |   |
|   |                                                               |   |
|   +---------------------------------------------------------------+   |
|                                                                       |
|   [ Skip ]                                                            |
+-----------------------------------------------------------------------+
```

(点击 Show Answer 后)

```text
+-----------------------------------------------------------------------+
|   ...                                                                 |
|   +---------------------------------------------------------------+   |
|   |  YOUR SAVED EXPRESSION:                                       |   |
|   |  "I'm currently blocked by the API issue, so I might miss     |   |
|   |   the deadline today."                                        |   |
|   |                                                               |   |
|   |  BETTER ALTERNATIVE:                                          |   |
|   |  "I've hit a blocker with the API, which puts the delivery    |   |
|   |   at risk."                                                   |   |
|   +---------------------------------------------------------------+   |
|                                                                       |
|   [ Hard ]    [ Good ]    [ Easy ]                                    |
+-----------------------------------------------------------------------+
```
