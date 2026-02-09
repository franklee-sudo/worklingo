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
- **功能描述**：
    - **润色辅助**：用户输入草稿，AI 提供地道的职场化润色建议。
    - **语料沉淀**：自动收集用户工作中实际发送和接收的高质量英文表达。
    - **价值**：建立个人专属的工作语料库，涵盖项目管理、需求讨论、Code Review 等真实工作上下文。

### 3.2 场景二：口语沟通 (Oral Communication)
- **来源**：Zoom、Teams 等在线会议。
- **功能描述**：
    - **会议转写与提取**：对会议录音进行转写（或利用实时字幕文本），结合工作上下文补全信息。
    - **核心表达挖掘**：从会议中提取同事常用的地道表达、行业术语和惯用句式。
    - **复盘与跟读**：提供针对性的跟读训练，通过模仿真实会议场景来提升口语自信。
    - **价值**：捕捉稍纵即逝的口语精华，将"听不懂"转化为"下次会说"。

## 4. 产品原则 (Product Principles)
1.  **Less is More**：不需要 10000 个单词，只需要工作中真正用到的 200 个表达。
2.  **No Gamification**：不要每日打卡，不要游戏化机制，专注于实用性。
3.  **Context is King**：所有学习内容必须基于用户真实的工作上下文，而非通用教材。
4.  **Immediate Feedback**：强调"即学即用"，让用户在第二天的工作中就能验证学习效果。

## 5. 核心功能列表 (Core Features)

| 模块 | 功能点 | 描述 | 优先级 |
| :--- | :--- | :--- | :--- |
| **Input (采集)** | **手动导入 (Paste-to-Import)** | **MVP核心**：支持用户直接粘贴 Slack 记录、邮件、或与 ChatGPT 的润色对话记录。虽然繁琐，但能筛选出高意向用户。 | **P0** |
| | 会议文本导入 | 支持导入 Zoom 录音转写文本或字幕文件。 | P0 |
| | *文本润色插件* | *（规划中）* 浏览器插件或侧边栏，自动采集。 | P2 |
| **Process (处理)** | **结构化智能整理** | 将零散的聊天记录按场景（Scene）和意图（Intent）进行分类、去重、规整。 | **P0** |
| | 核心语料提炼 | 提取关键词（Keywords）和地道表达（Expressions），剔除无效寒暄。 | P0 |
| **Output (应用)** | 场景化知识库视图 | 按工作场景展示语料（如：Ask for ETA, Report Bugs）。 | P1 |
| | 场景化闪卡 | 基于真实语料生成的复习卡片，强调语境记忆。 | P1 |

## 6. 数据结构化示例 (Structured Data Example)

针对用户痛点（记录零散、上下文混乱），系统将非结构化文本转化为结构化知识库：

### 原始输入 (Raw Input)
> 用户粘贴了一段 Slack 记录：
> "Hey, about the login bug, I think the API returns 500 error. Can you check when it can be fixed? We need this for the demo tomorrow."

### 结构化输出 (Structured Output)

**场景 (Scene)**: 软件开发 / Bug 处理
**意图 (Intent)**: 询问修复排期 (Ask for ETA) & 报告错误 (Report Issue)

| 维度 | 提取内容 | 备注/扩展 |
| :--- | :--- | :--- |
| **Context (上下文)** | Login bug, API 500 error, Demo tomorrow | 紧急程度：High |
| **Key Expression (核心句型)** | "Can you check when it can be fixed?" | 更正式说法: "Could you provide an ETA for the fix?" |
| **Keywords (关键词)** | API returns 500 error | 技术术语 |
| **Response Guide (回复建议)** | 如果你是被问方: "I'm looking into it. Expect an update by [Time]." | 预设回复模板 |

## 7. 成功指标 (Success Metrics)
- **用户活跃度**：在实际工作场景（Slack润色/会议复盘）的使用频率。
- **语料库增长**：用户个人专属语料库的条目数（目标：高质量 200 条）。
- **应用转化率**：用户将学习到的表达在后续工作中实际使用的次数（需用户反馈或自动检测）。
