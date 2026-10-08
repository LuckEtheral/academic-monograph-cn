# 中文研究型专著写作 Skill

名称：`chinese-research-monograph`；版本：`0.1.0`。

帮助以文献和模型为基础的中文研究型专著建立问题链，讲清模型与机制，并完成修订、审阅和跨章衔接。规则提炼自实际中文专著编写经验；本包只包含通用规则，不包含书稿、论文原件、私有路径或作者资料。

适用重点为经济管理、运筹及相近领域。其他学科可按其体裁调整，不强制采用数学模型。单篇期刊论文、纯翻译和单纯排版宜使用对应专门流程。

## 特色

- 以问题组织章节，让来源论文参与本书论证。
- 解释主体、信息、行动顺序和公式的经营含义。
- 保留不同模型的对象和条件，建立实质的章际联系。
- 区分原文内容、本书重推和新增综合解释。
- 减少重复防御性表达，将必要条件融入准确论述。
- 按任务交付完整作品，如实记录来源与检查范围。

专著的学术价值可以来自问题组织、比较和深化解释，不要求每章提出新定理；新增综合判断仍须有依据。不设统一字数、文献数、图数或案例数配额。

## 使用

仓库：[LuckEtheral/academic-monograph-cn](https://github.com/LuckEtheral/academic-monograph-cn)。

安装本仓库的 `skills/chinese-research-monograph` 目录，保留其中的 `SKILL.md`、`agents/` 与 `references/`。可向支持技能安装的 Codex 环境提供仓库链接及这个目录路径；具体安装方式见[官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

在支持 `$skill-installer` 的 Codex 环境中，可以这样请求：

```text
使用 $skill-installer，从 LuckEtheral/academic-monograph-cn 仓库安装
skills/chinese-research-monograph，安装完成后告诉我如何调用。
```

安装后，可显式使用 `$chinese-research-monograph`。以下示例中的输入须由用户实际提供：

```text
使用 $chinese-research-monograph，根据提供的计划、来源论文和前章底本，
完成本章连续可读的中文正文。先明确问题链，解释关键模型与机制，
将学术核查说明独立成文。按本次约定交付并停止。
```

```text
使用 $chinese-research-monograph，局部修订所选小节的中文表达。
保留公式、数值、来源归属和结论条件，改善机制解释与段落推进。
只处理选定范围。
```

```text
使用 $chinese-research-monograph，独立审阅提供的两章。
先依据正文与原件形成判断，再对照历史意见；区分确认错误、
待核疑点和表达偏好，给出有依据的最小修订方案，不改章稿。
```

## 结构

```text
skills/chinese-research-monograph/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── chapter-writing.md
    ├── models-and-sources.md
    ├── chinese-prose.md
    ├── review-and-integration.md
    └── delivery.md
```

入口按任务选择参考文件，避免所有模式同时加载。本技能是写作指导，不附带联网、计算或文档渲染服务；相关检查使用所在环境实际提供的能力。

## 当前状态

初版 `0.1.0`。本仓库公开托管通用规则，开源许可证尚待作者选择。

规则源于具体项目经验，已抽离项目字数、目录和排版参数。结构校验与人工式规则审阅不等于实际章稿行为验证；使用后的真实问题应以小范围修改改进规则。
