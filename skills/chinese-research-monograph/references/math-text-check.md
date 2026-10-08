# 数学文件的落盘与显示检查

含数学的文件交付时按需使用[只读扫描工具](../scripts/check_math_text.py)：

```sh
python scripts/check_math_text.py --json output.md
```

从技能目录运行上述命令，或明确给出脚本及文件路径。工具只读取这些实参，不递归项目、不解析正文链接、不修改输入；拒绝目录和直接符号链接文件。输出路径、行号、片段及复核理由；`read_failed`为实际读取失败，`needs_context_review`仅为启发式提示。后者退出码仍为0，读取失败为2；不要把退出码或提示数量当学术评分。

有限扫描支持美元和反斜杠数学分隔符、简单括号内ASCII数学，排除Markdown围栏与行内代码。正常表格缩进、普通英文和ASCII变量不自动改写。部分控制字符、命令残片、短符号与运算符粘连及括号缺项会提示；特殊定界符、其他数学环境和合法变量仍可能漏报或误报。按上下文确认，不能自动补公式，无告警不证明正确。

安全写入的短例（仅说明当前Python/JSON层级）：

```python
from pathlib import Path
import json

text = r"$\beta\ne0,\quad y=\frac{\theta}{2}$" + "\n"
wire = json.dumps({"text": text}, ensure_ascii=False)
restored = json.loads(wire)["text"]
target = Path("output.md")
target.write_bytes(restored.encode("utf-8"))
assert target.read_bytes() == text.encode("utf-8")
```

序列化负责JSON层转义，UTF-8回读负责实际文件字节；若外层还有shell、模板或其他语言，分别核对该层，不把raw string当万能方法。然后回读实际表达式，对照既定目标、函数括号、偏导和上下标，在实际交付的显示路径查看关键公式。分隔符配对、扫描成功和渲染成功不能代替语义核对。未测宿主如实说明。

纯聊天、目录规划及不含数学的局部文字任务不强制运行此工具、截图或建立检查包。只交Markdown不强制新建Word；交Word仍按交付指南检查最终文件页面。工具是交付实现，不是数学模型证明或未来输出无损保证。
