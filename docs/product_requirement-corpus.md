# Worklingo 语料库体系设计文档 (Corpus Design Spec)

## 1. 设计背景 (Background)
用户反馈目前的语料库仅仅是“润色记录的堆砌”，随着记录增多，难以找到重点，无法有效复习。
参考雅思语料库和企业知识库（Knowledge Base）的设计理念，我们需要将语料库从“流水账”升级为用户的**“职场英语第二大脑”**。

## 2. 核心理念 (Core Philosophy)
**"Deconstruct & Reorganize" (拆解与重组)**
不再以“次”为单位存储，而是以“知识点”为单位存储。将一次润色记录拆解为若干个独立的表达模块，并按不同维度重新组织。

## 3. 知识库三大视图 (The Three Views)

### 3.1 视图 A：场景攻略 (Scenario Playbook) - *Episodic Memory*
**用户痛点**：“我要去开会/写邮件了，那个场景下该说什么？”
**组织方式**：按工作流（Workflow）分类，提供即插即用的“话术块”。

| 一级分类 | 二级标签 (Tag) | 典型语料示例 |
| :--- | :--- | :--- |
| **向上汇报 (Reporting)** | `Progress Update` | "We are currently **on track** to meet the Q3 targets." |
| | `Blocker` | "We hit a **roadblock** regarding the API integration." |
| | `Proposal` | "I **propose** we allocate more resources to..." |
| **跨部门协作 (Collab)** | `Request` | "Could you **facilitate** a meeting with..." |
| | `Push back` | "Due to bandwidth constraints, we have to **deprioritize** this." |
| **客户沟通 (Client)** | `Follow up` | "Just wanted to **circle back** on our last conversation." |
| | `Apology` | "Please accept our apologies for the **oversight**." |

### 3.2 视图 B：专属词典 (Domain Dictionary) - *Semantic Memory*
**用户痛点**：“这个词在我们行业/公司怎么说最地道？”
**组织方式**：按词汇属性分类，打造公司内部的“生存指南”。

*   **行业术语 (Industry Terms)**: 
    *   SaaS, YoY (Year over Year), Churn Rate, ROI, CAC
*   **公司/产品黑话 (Company Lingo)**: 
    *   Stand-up (站会), All-hands (全员会), Sync (对齐), One-on-one
*   **高频强力动词 (Power Verbs)**: 
    *   **Spearhead** (带头/主导), **Leverage** (利用/撬动), **Align** (对齐), **Drive** (推动)

### 3.3 视图 C：时间线 (Timeline) - *Recall Memory*
**用户痛点**：“我上周写给老板的那封邮件在哪？”
**组织方式**：保留现有的时间轴视图，作为“源文件”存档。点击某条记录可查看当时的完整上下文。

## 4. 数据结构升级 (Data Structure Upgrade)

### 4.1 细粒度拆解 (Granular Deconstruction)
在 AI 润色阶段，强制要求输出 `granular_points` 数组：

```json
"granular_points": [
    {
        "original_chunk": "I want to ask for help",
        "polished_chunk": "I would like to request some assistance",
        "tag": "Request",
        "category": "Collab"
    },
    {
        "original_chunk": "The data is bad",
        "polished_chunk": "The data indicates a downward trend",
        "tag": "Problem",
        "category": "Reporting"
    }
]
```

### 4.2 标签体系 (Tagging System)
*   **自动打标**：AI 根据内容自动匹配预设标签（如 Request, Update）。
*   **人工微调**：用户可以手动修改或添加自定义标签（如 #ProjectA）。

## 5. 交互设计 (Interaction Design)

### 5.1 语料库首页 (Library Home)
*   **Dashboard**: 显示“我的语料分布”（e.g., "你积累了 50 个汇报句型，20 个协作句型"）。
*   **快速入口**: [场景攻略] [专属词典] [历史记录] 三大卡片入口。

### 5.2 详情卡片 (Detail Card)
*   **样式**：不再是长文本，而是**清单体 (Listicle)**。
*   **对比**：原文（灰色删除线） vs 润色（高亮加粗）。
*   **操作**：
    *   点击单词 -> 查看字典定义/加入生词本。
    *   点击标签 -> 查看该标签下的所有语料。

## 6. 价值验证 (Value Proposition)
通过这种组织方式，Worklingo 将从一个“一次性润色工具”转变为用户的**“职场资产管理系统”**。用户积累的每一句话，都会自动归位到对应的知识货架上，越用越有价值。
