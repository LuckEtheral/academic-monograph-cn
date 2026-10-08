# 0.4.0-beta.1试用说明

本版为GitHub Pre-release，发布时默认main保持稳定版0.3.0；不会自动升级日常环境。Skill名称和调用名均为`chinese-research-monograph`。

安装时同时指定仓库`LuckEtheral/academic-monograph-cn`、tag `v0.4.0-beta.1`及路径`skills/chinese-research-monograph`。可向安装器提供完整路径：

```text
使用 $skill-installer，从
https://github.com/LuckEtheral/academic-monograph-cn/tree/v0.4.0-beta.1/skills/chinese-research-monograph
安装到独立试用位置；不要覆盖已有同名技能。
```

也可下载本Release的技能ZIP，将其中`skills/chinese-research-monograph/`复制到一次性Codex CLI项目的`.agents/skills/chinese-research-monograph/`，在该项目显式调用`$chinese-research-monograph`。实际加载时确认入口`metadata.version`为`0.4.0-beta.1`；宿主能力及其他安装位置服从其[官方说明](https://learn.chatgpt.com/docs/build-skills)。

本次隔离显式调用冒烟已完成；自动发现/自动调用未测。58个专项执行会话不等于58项独立测试，也未证明整体优于0.3.0。完整边界见[公开验证摘要](../evals/v0.4-beta/RESULTS.md)。R6/X56后续决定是否转为默认稳定版；G6另按来源与授权安排。许可证维持作者尚未选择的状态。
