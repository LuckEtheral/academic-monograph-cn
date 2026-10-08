# 中文研究型专著写作与审核 Skill

**0.4.0-beta.1 · 试用版（GitHub Pre-release）。** 发布时默认分支保留稳定版0.3.0；本试用版来自专项验证后的最终候选，包含有限修正01。技能名称和调用标识不变。

名称：`chinese-research-monograph`；版本：`0.4.0-beta.1`。
仓库：[LuckEtheral/academic-monograph-cn](https://github.com/LuckEtheral/academic-monograph-cn)。

帮助以文献、理论模型和研究结果为基础的中文专著建立问题体系，讲清模型与机制，形成跨研究综合认识，并审核已完成书稿。主要面向中文管理科学与工程研究型专著，重点支持博弈分析、契约设计、信息不对称和决策优化；相近领域按实际问题与体裁使用。规划、编写、修订、统稿与审核均保留。

**写作与审核以中文学术专著规范为主要依据，结合目标出版社要求和作者明确约定。** 英文研究可作为学术来源，英文专著提供组织和讲解方法参考，其论文式章节、摘要或文献编排不能直接成为中文专著的形式标准。论文材料须按中文专著主线和叙述重新组织。详见[中文专著规范](skills/chinese-research-monograph/references/chinese-monograph-conventions.md)。

## 快速开始与资料准备

安装完成且当前环境能调用后，可写：

```text
使用 $chinese-research-monograph，只审核附件中的第4章，目标读者是经管研究生。
章稿为当前底本，两篇论文用于核对模型设定。以中文学术专著规范为准，
检查信息结构、交易时序及结论条件，给有定位的意见；本次不修改书稿。
```

**文献不是每次都必须上传。** 规划可从主题、读者和问题开始，润色或结构初审可从书稿开始；依据文献写作、核查引证与复算时，需提供对应原文、设定或数据。当前对话附件和可读取的本地路径均可，材料数量服从本次任务。书目、DOI有助于寻找原文，但不能代替已核读正文。

[完整使用指南](docs/usage-guide.md)说明任务需要什么材料、文件怎样准备、如何调用、资料缺失时怎样继续，并提供七种任务示例。使用者不必重新上传维护者用于提炼规则的参考专著，也不必把研究文献或书稿上传到GitHub。

## 写作与审核

|入口|模式|交付|
|---|---|---|
|写作|全书规划、整章写作、局部修订、跨章统稿|对应范围的可读成品及必要的独立说明|
|审核|快速诊断、全书系统审阅、专项核查、修订复审|总体判断、可定位问题清单、检查覆盖与待核事项|

不同章节采用不同组织方式。来源论文按本书问题重组，数学对象、结论条件和新增解释的归属得到保留。专著价值可以来自有依据的综合、比较与深化，不要求每章提出新定理。

审核检查问题体系、解释深度、模型含义、引证支持、案例事实、跨章关系、中文与图表。阅读覆盖、来源核读、计算复核和版面检查分别报告。审核默认保留原稿；明确区分确认错误、待核疑点和表达偏好。

## 安装与调用

安装目录为 `skills/chinese-research-monograph`。保留其中的入口、显示信息、参考指南和模板。安装方式与可用能力以实际环境为准；安装技能不代表已经具备检索、OCR、计算或Word/PDF渲染能力。

本Beta需从[tag v0.4.0-beta.1](https://github.com/LuckEtheral/academic-monograph-cn/tree/v0.4.0-beta.1)取得；只写仓库名会获取默认稳定分支。只希望在隔离Codex CLI项目试用时，可把该tag中的技能目录放入项目的 `.agents/skills/chinese-research-monograph/`；适用宿主与加载方式见[官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

在支持 `$skill-installer` 的环境中可请求：

```text
使用 $skill-installer，从 LuckEtheral/academic-monograph-cn 安装试用版，
必须指定 ref 为 v0.4.0-beta.1，path 为 skills/chinese-research-monograph。
不要按默认分支安装，不覆盖已有同名安装；已有副本时先选独立试用位置。
```

安装后可显式调用：

```text
使用 $chinese-research-monograph，根据提供的计划、来源和前章底本，
完成本章连续可读的正文。解释关键模型，核查说明独立成文。
按约定交付并停止。
```

```text
使用 $chinese-research-monograph，系统审阅提供的完整专著。
检查全书问题体系、解释深度、跨章关系和关键论断。
逐章记录覆盖，给出有定位和依据的意见；本次不改书稿。
```

```text
使用 $chinese-research-monograph，只复审指定修订项及必要关联内容。
分别报告已解决、部分解决、未解决和未核事项，不扩展到全书重写。
```

```text
使用 $chinese-research-monograph，检查指定小节的模型与引证。
来源缺失时准确区分待核疑点与确认错误，按实际复核范围报告。
```

## 可选技能协作

本技能独立支持核心写作与审核。中文润色、Word/PDF、经济管理图表、独立学术评估、运筹表达和新增文献调研可按需要使用环境中已有技能。

协作规则见 [skill-collaboration.md](skills/chinese-research-monograph/references/skill-collaboration.md)。不整包复制第三方技能，不自动安装，不要求每次加载全部技能。专著体裁与作者要求控制总体组织。

## 内容与模板

入口按任务选择指南，涵盖中文规范、材料接收、全书架构、章节类型、章节写作、文献转化、模型与来源、中文表达、审核统稿、交付、示例和协作。[来源与核读范围](skills/chinese-research-monograph/references/reading-basis.md)说明研究依据及限制，不替代使用者当前任务的原件。

五个可选模板位于 `assets/templates/`：章节任务说明、专著审阅报告、模型变化、案例用途、数值说明。只有实际需要时使用，已明确的任务不必再次填写，也不要求每次使用全部模板。

[历史测试任务](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/cases.md)与[合成材料](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/fixtures.md)保持原身份；[历史结果](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/RESULTS.md)不继承成本Beta新测结果。专项验证的实际结果与限制见[Beta公开验证摘要](evals/v0.4-beta/RESULTS.md)。

## 发布底本0.3.0的历史变化

相较 0.2.0，将中文规范优先原则写入入口和专题指南，增加完整使用指南、材料接收说明、来源索引，以及模型变化、约束分组、小例子、风险指标、数值比较、案例用途和综合审核的细化方法，补充自拟中文示例与三个轻量模板。

[0.2.0历史小任务记录](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/RESULTS.md)保持原版本身份；[0.3.0验证说明](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/v0.3/RESULTS.md)保留原结构检查与实际试用身份。选章核读及小任务试用不构成整本专著写作或审核效果验证，也不报告未实测的提升比例。

不设置统一字数、章节结构、文献数或图数。出版社格式由项目指定。本仓库只托管通用规则与合成测试材料，不包含未发表书稿、论文原件或作者私有资料。

本tag为0.4.0-beta.1试用版；发布时默认稳定分支为0.3.0，未经合并。历史eval保留在仓库，独立技能附件仅含通用技能与必要使用说明。许可证仍待作者选择。

[简短试用安装说明](docs/beta-install.md)提供锁定版本和隔离使用方法。

## 试用版验证范围

初轮27项成对任务中26项持平、W01一项候选写作退步，改善0项；一次有限修正后W01、L02两项开发回归均满足且持平。共58个执行会话，并非58道独立测试或一次全部通过。未证明整体优于0.3.0，P16示例未实际加载。最终修正候选仅直接复测W01和L02；自动发现/自动调用及R6、X56、G6仍未测。完整边界见[公开验证摘要](evals/v0.4-beta/RESULTS.md)。
