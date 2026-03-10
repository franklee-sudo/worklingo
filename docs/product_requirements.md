# Worklingo - 私人职场英语学习助手产品文档

## 1. 产品愿景 (Product Vision)
**"别再假装学习了"**

拒绝无效的打卡和海量词汇堆砌，专注于职场中真正高频使用的 200 个核心表达。打造一个只属于用户的、高度定制化的职场英语语料库，实现"学了立刻就能用"。

## 2. 目标用户 (Target Audience)
**"经历过假装学习，已经觉醒的实用主义者"**

### 用户画像特征
- **基础水平**：有一定英语基础，非零基础小白。
- **痛点**：尝试过各种背单词、看美剧等传统方法，但对实际工作帮助甚微；清楚知道自己需要提升工作场景下的沟通能力。
- **心态**：拒绝浪费时间，追求效率，愿意为真正解决问题的工具付费。

## 3. 核心应用场景 (Core Scenarios)

### 3.1 场景一：文字沟通 (Text Communication)
- **来源**：Slack、Email 等工作IM工具。
- **场景细分**：
    - **信息同步 (Sync)**：跟同事确认背景信息，为外部会议做准备（e.g., "What's the background on this issue before I meet the vendor?"）。
    - **问题排查 (Troubleshooting)**：描述 Bug，询问排期，跟进状态。
- **价值**：建立个人专属的工作语料库，涵盖项目管理、需求讨论等真实工作上下文。

### 3.2 场景二：口语沟通 (Oral Communication)
- **来源**：Zoom、Teams 等在线会议。
- **功能描述**：会议转写提取，捕捉稍纵即逝的口语精华，将"听不懂"转化为"下次会说"。

### 3.3 场景三：结构化汇报 (Structured Reporting) - **NEW**
- **来源**：周报、月报、Business Review。
- **场景描述**：老板要求分析产品数据，汇报业务情况。
- **核心结构 (The Framework)**：
    1.  **What (描述现状/变化)**：数据是多少？涨了跌了？
    2.  **Why (解释原因)**：为什么会这样？市场因素？产品改动？
    3.  **Action (行动计划)**：接下来做什么？
- **关键元素**：
    - **黑话/术语 (Jargon)**：YoY (Year over Year), MoM (Month over Month), ROI, Churn Rate 等。
    - **逻辑连接词**：用于串联 What/Why/Action 的起承转合句型。

## 4. 产品原则 (Product Principles)
1.  **Less is More**：不需要 10000 个单词，只需要工作中真正用到的 200 个表达。
2.  **Context is King**：所有学习内容必须基于用户真实的工作上下文。
3.  **Structure > Vocabulary**：**职场英语的核心不仅仅是单词，更是逻辑结构。** (e.g., STAR原则, What-Why-Action)。
4.  **Master the "Black Words"**：精通特定场景下的"黑话"（专有名词/缩写），是融入职场圈子的关键。
5.  **Deliberate Practice**：通过案例和重复的刻意练习，彻底精通某几个高频场景（如数据汇报、跨部门撕逼），而非泛泛而谈。

## 5. 核心功能列表 (Core Features)

| 模块 | 功能点 | 描述 | 优先级 |
| :--- | :--- | :--- | :--- |
| **Input (采集)** | **手动导入 (Paste-to-Import)** | **MVP核心**：支持粘贴 Slack/邮件/汇报草稿。筛选主动性强的用户。 | **P0** |
| | 会议文本导入 | 支持导入 Zoom 录音转写文本或字幕文件。 | P0 |
| **Process (处理)** | **结构化智能整理** | 将零散记录按场景（Scene）和意图（Intent）分类。 | **P0** |
| | **逻辑结构提取** | 识别文本中的逻辑链条（如 What-Why-Action），并优化结构。 | **P0** |
| | **术语库 (Glossary)** | 自动提取并解释缩写和专有名词（e.g., YoY, KPI）。 | **P1** |
| **Output (应用)** | 场景化知识库视图 | 按工作场景展示语料（如：Data Reporting, Vendor Meeting）。 | P1 |
| | 场景化闪卡 | 基于真实语料生成的复习卡片，强调语境记忆。 | P1 |

## 6. 数据结构化示例 (Structured Data Example)

### 示例 A：数据汇报 (Data Analysis)

**原始输入 (Raw Input)**:
> "Our user growth this month is 5%, which is lower than last month. I think it's because the marketing budget was cut. We need to optimize the organic search next month."

**结构化输出 (Structured Output)**:

**场景 (Scene)**: Business Review / Data Reporting
**意图 (Intent)**: 解释业绩下滑 (Explain Performance Dip)

| 维度 | 提取内容 | 优化建议/扩展 |
| :--- | :--- | :--- |
| **Structure (逻辑)** | **What**: Growth is 5% (lower)<br>**Why**: Budget cut<br>**Action**: Optimize organic search | 逻辑清晰，但表达不够专业。 |
| **Key Expression (核心句型)** | "which is lower than last month" | **Better**: "We observed a slight deceleration in growth, down to 5% **MoM**." |
| **Jargon (术语/黑话)** | - | 建议使用: **MoM** (Month over Month), **CAC** (Customer Acquisition Cost) |
| **Refined Version (润色版)** | "Our user base grew by 5% **MoM**, a slowdown attributed to the recent reduction in marketing spend. To **mitigate** this, we plan to pivot our focus to **SEO optimization** next month." | 更显专业、客观、有行动力。 |

### 示例 B：跨部门协作 (Cross-functional Alignment)

**原始输入**:
> "Hey, I have a meeting with the vendor later. Can you tell me what happened with the server yesterday? I need to know the background."

**结构化输出**:

**场景 (Scene)**: External Meeting Prep
**意图 (Intent)**: 获取背景信息 (Gather Context)

| 维度 | 内容 |
| :--- | :--- |
| **Key Expression** | "Can you tell me what happened..." |
| **Better Alternative** | "Could you **brief me on the context** regarding yesterday's server incident? I need to be **aligned** before meeting the vendor." |
