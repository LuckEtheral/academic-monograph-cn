# 可选技能协作

只有当前任务确有需要时读取。本技能自包含核心写作与审核，专项技能不构成统一前置依赖。

## 路由与交付边界

|技能|触发条件|提供给协作技能|接收并复核|
|---|---|---|---|
|humanizer-zh|中文润色或表达专项|指定文本、含义和条件保留要求|修改稿及必要说明，检查语义保留|
|documents、pdf|Word/PDF读取、生成或视觉核查|指定文件、版式约定和读写范围|文件、渲染和实际覆盖，核对内容与版面|
|econ-table-figure-design|经济管理图表信息与视觉检查|对象定义、参数或数据、图表用途|标签、注释、图表和渲染结果，不改变数值|
|peer-review|适用要求明确的独立学术评估|授权材料、委托范围与适用规则|有依据的审阅草稿与实际限制|
|anti-defensive-writing-zephyr|贡献组织或防御性表达检查|当前贡献、证据及必须保留条件|突出价值的文本，复核条件与强度|
|or-writing-polishing|运筹模型、算法、实验的专业表达|问题、方法、结果及当前章任务|专业解释，不引入期刊固定结构|
|literature-review-econ-skill|明确需要新增相近文献调研|检索问题、材料范围和贡献判断任务|已核读来源与定位，检查实质相关性|

先确认技能在当前环境确实可用并读取其说明。按作者意图、专著体裁和本次范围组织任务，遵循协作技能实际要求；若其完整流程不适合任务，不通过复制片段绕过要求，而选择本技能流程或明确适用的另一能力。

## 获取链接与名称差异

核对日期：2026-10-08。以下是公开来源入口，不包含第三方技能副本。取得完整目录及支持资源，不只复制SKILL.md；按上游说明核对依赖、许可、宿主和实际name，记录所选commit。链接内容可能更新，本项目不自动同步。

|协作名称|公开获取入口|取得范围与说明|
|---|---|---|
|humanizer-zh|[Humanizer-zh](https://github.com/op7418/Humanizer-zh)|仓库根目录|
|econ-table-figure-design|[经济管理图表技能](https://github.com/juliaError/econ-TopJournal-writing-Skill/tree/main/skills/econ-table-figure-design)|skills/econ-table-figure-design完整目录|
|or-writing-polishing|[OR-Writing](https://github.com/raichll/OR-Writing)|仓库根目录|
|literature-review-econ-skill|[文献综述技能](https://github.com/caodoudou99/literature-review-econ-skill/tree/main/literature-review-econ-skill)|literature-review-econ-skill完整目录|
|peer-review|[Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/peer-review)|skills/peer-review完整目录；项目已从claude-scientific-skills更名|
|anti-defensive-writing-zephyr|[公开同类技能anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing/tree/main/skill/anti-defensive-writing)|不保证与本机zephyr副本一致；公开name为anti-defensive-writing，不冒称zephyr的直接安装源|
|documents|[公开替代技能docx](https://github.com/anthropics/skills/tree/main/skills/docx)|宿主documents能力不等于该目录；该替代技能name为docx，工具及许可单独核对|
|pdf|[OpenAI公开PDF技能](https://github.com/openai/skills/tree/main/skills/.curated/pdf)|skills/.curated/pdf完整目录；不保证与宿主插件版本一致|

先检查宿主已提供的documents/pdf能力。缺失时可考虑公开替代，不能声称安装了原插件。仅看到本机同名技能不等于已核实其公开获取源或所有环境可用。名称差异不通过改frontmatter掩盖。

安装可将本表链接交给当前环境支持的技能安装器，明确安装作用域和保留已有副本。用户操作示例见[使用指南](../../../docs/usage-guide.md#推荐配套技能怎样选用)。这些链接说明可获取性，不证明配套技能与本项目的全部组合效果；按当前任务读取其完整要求，不强制加载所有技能或指南。

## 默认与缺失处理

作者对自己专著自查使用本技能审核模式。peer-review有独立的正式评阅要求，不默认套用到普通作者自查；正式委托时按其适用要求处理。

第三方技能缺失时不自动安装，也不声称已调用。继续核心工作；若缺少所需渲染、计算或检索能力，则明确该专项未完成。用户要求安装时另按授权实施。

不默认全量加载，不要求任务使用所有技能，不强制并行代理。按实际需要协作，并如实记录何种能力完成了什么检查。

## 文件与内容

引用和调用第三方技能，保持独立更新与来源，不将整包内容复制到本仓库。确需再分发时先核实许可、来源和版本，不能以公开仓库代替许可判断。

协作输出进入正文前由主流程核对：对象、数值、条件和来源是否保留；是否误套论文结构；是否扩展范围；是否把检查限制写成重复的读者提醒。

审阅文件保持原样；授权的修改另存候选。只有本任务允许的材料可以交给相关能力，不扩大外部上传范围。
