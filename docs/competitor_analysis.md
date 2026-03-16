# Worklingo 竞品分析文档 (前端设计与体验聚焦)

## 1. 概览 (Overview)
Worklingo 的核心定位是**“职场英语第二大脑”**，有别于传统的单词记忆软件或单纯的机器翻译工具。用户的核心需求是“沉淀、查找、复用”。
因此，前端设计的核心目标是：**降低认知负荷（Minimalist）、高效重组（Structured）、以及凸显专业感（Premium）。**

以下选取了几款核心及跨界竞品，重点分析它们在**前端设计与交互体验**上的亮点和可借鉴之处。

---

## 2. 核心竞品对比与前端分析

### 2.1 Grammarly (标杆级纠错与风格润色)
*   **产品定位**：全平台的英语拼写检查与语气优化（Tone adjustments）。
*   **前端交互亮点**：
    *   **Inline Cards (行内卡片)**：以卡片形式贴在输入框旁边，用清晰的颜色编码区分错误类型（红：拼写错，蓝：清晰度，绿：生动性，紫：语气）。
    *   **一键替换**：用户只需点击卡片上的建议文字，原文就会被丝滑的动画替换。
    *   **Tone Detector (语气检测仪)**：用 Emoji 和雷达图的视觉形式，将文本的“情绪”直观表达出来（如 Confident, Friendly）。
*   **Worklingo 可借鉴（💡）**：
    *   在润色结果页（Result Section）采用**色块或徽章（Badge）**来区分“场景 (Scene)”和“语气 (Tone)”。
    *   增加带有过渡动画（Transition）的替换按钮，让“采纳建议”的过程具有爽快感。

### 2.2 DeepL / DeepL Write (专业级翻译与重写)
*   **产品定位**：主打精准的机器翻译与句子重构。
*   **前端交互亮点**：
    *   **极简分屏视图 (Split-view)**：经典的左右（或上下）分栏排版。左侧原文，右侧结果。没有任何多余按钮，焦点完全聚集于文本。
    *   **字词级悬浮替换 (Word-level hover)**：用户在输出框内点击任意一个单词，会直接弹出一个 Dropdown（下拉列表），提供同义词和不同句式，用户可以像拼图一样调整句子。
*   **Worklingo 可借鉴（💡）**：
    *   对 `granular_points` （细粒度知识点）的设计，前端可以在整段话中给予下划线提示，**Hover（悬停）时浮现 Tooltip** 展示其对应的分类（如 #Collab 或 #Request）。
    *   整体 UI 风格采用大留白（Whitespace），减少视觉噪音。

### 2.3 Wordtune (由 AI 驱动的改写神器)
*   **产品定位**：提供同一句话的多种表达方式（Casual, Formal, Shorten, Expand）。
*   **前端交互亮点**：
    *   **抽屉式展示 (Drawer/Carousel)**：生成的选项不是枯燥的罗列，而是用横向滑动的卡片（Carousel）或清晰的列表。
    *   **高亮对比图 (Diff Highlighting)**：Wordtune 会特别用颜色高亮被改动过的**动词或短语 (Power Verbs)**，让用户一眼看出“改了哪里”。
*   **Worklingo 可借鉴（💡）**：
    *   在我们的 `专属词典` 和 `场景攻略` 中，针对“对比原句与润色句”，可以采用 GitHub Diff 的思路：删除线（灰色）代表原句的普通表达，高亮（紫色或黑色粗体）代表高级职场表达，加深用户记忆。

### 2.4 Notion AI / Obsidian (跨界参考：知识库与第二大脑)
*   **产品定位**：结构化笔记与个人知识管理 (PKM)。
*   **前端交互亮点**：
    *   **多层级边栏 (Sidebar Hierarchy)**：用紧凑的树状图或标签云展示所有信息（犹如我们的 Workflow / Category）。
    *   **块状编辑 (Block Editor)**：万物皆可被拖拽、分类。
*   **Worklingo 可借鉴（💡）**：
    *   **标签系统 (Tagging UI)**：Worklingo 已引入了 `Category` 和 `Tag`。在前端呈现上，可以考虑设计一个专门的标签管理视图（Tag Cloud）。
    *   **三大视图的切换器 (View Switcher)**：可以参考 Notion 的 Database 视图切换体验，通过 Segmented Control (分段控制器) 在“场景”、“词典”、“时间轴”之间丝滑切换，而不用刷新页面。

---

## 3. Worklingo UI/UX 升级策略总结

结合上述分析，Worklingo 现有的前端可以从以下几个维度进行优化设计：

1.  **色彩设计 (Color Palette)**：
    *   考虑到我们要主打**高端职场感（Premium & Pragmatic）**，继续坚持目前的黑白灰极简底色（Black/White/Gray）。
    *   可以引入少量的**职场蓝 (Corporate Blue) 或深紫色 (Deep Purple)** 作为强调色，仅在展示 AI 改写亮点的部分使用。
2.  **字体体系 (Typography)**：
    *   当前使用了 `Playfair Display` 作为 Serif（衬线体）和 `Inter` 作为 Sans-serif（无衬线体），非常优雅。
    *   对于系统代码、Tag 或分析术语（如 `Reporting`, `Power Verbs`），可以混用等宽字体 (`Monospace`)，增强“技术型、数据分析”的秩序感。
3.  **微交互 (Micro-interactions)**：
    *   **Flashcard 翻转效果**：卡片翻转时增加更细腻的物理阻尼感与阴影变化。
    *   **Skeleton Loading (骨架屏)**：在等待 DeepSeek API 返回时，与其仅仅用一个 Spinner 显示“正在分析”，不如播放一段扫描文字或高亮动态骨架屏的特效。
4.  **页面响应式 (Responsiveness)**：
    *   英语语料经常会在手机端进行快速复习。在移动端下，左右分栏的视图（Scene / Dictionary）应转为折叠面板（Accordion）或是卡片流。

---

*文档生成时间：2026年3月*
