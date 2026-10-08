# 中文研究型专著写作与审核 Skill

**0.4.0 · 本项目选择的默认可用发布版本。** 技能名及调用名保持chinese-research-monograph；稳定版不是学术正确性认证，也不承诺未来输出无误。

主要服务中文管理科学与工程研究型专著，重点为博弈分析、契约设计、信息不对称和决策优化；保留全书规划、章节编写、局部修订、跨章统稿及审核。相近领域按其体裁使用，不强加数学模型或新增实证要求。

中文学术专著规范、出版社要求和作者约定优先。英文专著只提供方法和讲解参考，不决定中文书稿体例。正文以本书经营问题和机制组织，不按论文串联；采用模型、结果或数据时，在相关位置准确归属，一篇核心来源也可形成独立可读的专题。

## 仓库格式补充（v0.4.0发布后）

新增[符号、名称与图表排印](skills/chinese-research-monograph/references/typography-and-names.md)，以及可明确选用的[作者16开格式配置](skills/chinese-research-monograph/references/format-profile-16k.md)。通用规则与项目尺寸/字号分开；识别损坏、冲突和旧条款登记为待核，不自动套用到所有专著。

本次只更新仓库，不创建新Release；v0.4.0标签及附件保持原样，尚不含此次补充。需要补充的使用者应选择包含它的确定commit及skills/chinese-research-monograph路径，并记录commit；仅核入口版本号0.4.0不足以区分发布包和后续仓库内容。下方固定tag安装说明仍对应原正式发布。写作、模型和审核主线及历史评测保持不变，不宣称新增写作效果。

## 安装与调用

固定本版：ref=v0.4.0，path=skills/chinese-research-monograph。见[固定版本安装说明](docs/install-v0.4.0.md)。项目级使用可将完整技能目录放入.agents/skills/chinese-research-monograph/；确认入口metadata.version为0.4.0，不自动覆盖已有同名副本或锁定项目。

```text
使用 $skill-installer，从
https://github.com/LuckEtheral/academic-monograph-cn/tree/v0.4.0/skills/chinese-research-monograph
取得固定版本；放入独立项目，不覆盖已有同名技能。
```

```text
使用 $chinese-research-monograph，按提供的本章问题和来源完成连续中文正文。
讲清主体、信息、时序、关键推导及成立条件，在相关位置保留引用。
按约定交付并停止。
```

## 任务与材料

|任务|入口与交付|
|---|---|
|规划|主题、读者和问题即可启动；目录候选与章节功能|
|编写/修订|按约定范围交付可读正文，保留公式、条件、事实及来源归属|
|统稿|核对实际跨章关系，保留不同模型的对象、时序与比较口径|
|审核/复审|保留原稿，给有定位的依据，区分确认错误、待核疑点和表达偏好|

文献不是每次都必须上传；依据来源写作、核引证或复算时取得对应原件/输入。局部润色和规划不以全文上传为前提。[使用指南](docs/usage-guide.md)保留七种任务示例及资料说明；研究来源、写法参照和格式要求分别识别。私有书稿、文献原件不上传本仓库。

## 本版有限完善

- 在[交付检查](skills/chinese-research-monograph/references/delivery.md)增加含数学文件的实际落盘/显示核对，配[标准库只读工具与短例](skills/chinese-research-monograph/references/math-text-check.md)。启发式提示不能自动修公式，无告警不等于正确；纯聊天、规划和非数学文字不强制扫描/截图。
- 在[章节写作](skills/chinese-research-monograph/references/chapter-writing.md)及[文献转化](skills/chinese-research-monograph/references/literature-synthesis.md)精炼问题主线与必要归属，提供[自拟开头改写和归属对照](skills/chinese-research-monograph/references/writing-examples.md#1-论文摘要式介绍转为问题推进)。不禁用作者名，不制造新机制。
- [自拟交付回归](evals/v0.4-delivery/README.md)测试工具和文件流程；当前[公开验证摘要](evals/v0.4/RESULTS.md)分开记录历史专项、真实任务、交付修复和本次验收。

## 验证范围

P01—P16专项规则已在Beta底本实施。初轮27项成对任务、54个执行会话，26项持平、1项写作退步；有限修正后W01/L02另4会话复测满足，共58个执行会话，不是58道独立试题。R6/X56另有4个执行、2个独立评阅，任务评价均持平；R6首次字符缺陷在后续交付副本恢复18处，首次输出与评阅保留。

未证明整体优于v0.3.0；P16未实际加载的阶段不宣称示例增益。本次通用工具不倒称旧会话已使用。G6真实整章编写对照、宿主自动发现/自动调用及其他显示环境按实际未测登记。具体有限验收及限制见公开摘要。

## 资源与历史

入口按需选读中文规范、材料接收、架构、章节类型、写作、文献转化、模型与来源、中文表达、审核统稿、交付、示例及协作；不要求每次全部加载。五个可选模板保留在assets/templates，研究依据见[来源索引](skills/chinese-research-monograph/references/reading-basis.md)。[协作说明](skills/chinese-research-monograph/references/skill-collaboration.md)保留按需协作，不自动安装第三方技能。

不统一章数、字数、图表数量或论文式章结构；不要求每章新定理。来源核读、数学复核、实际运算与视觉检查分别报告，不将未做工作记通过。

历史[0.2记录](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/RESULTS.md)、[0.3记录](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/v0.3/RESULTS.md)及[Beta摘要](https://github.com/LuckEtheral/academic-monograph-cn/blob/v0.4.0-beta.1/evals/v0.4-beta/RESULTS.md)保持阶段身份；旧Beta标签、Release及附件不覆盖。[变更记录](CHANGELOG.md)仅记录此次有限修改。

许可证沿用仓库尚未选择的实际状态；公开托管不等于已经授予特定开放许可。
