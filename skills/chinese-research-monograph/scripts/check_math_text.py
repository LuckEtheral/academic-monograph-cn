#!/usr/bin/env python3
"""Read-only, limited heuristics for UTF-8 mathematical text; no auto-repair.
Only explicit file arguments are read; Markdown links are not followed.
Fenced/inline code is excluded. Findings require contextual review.
"""
import argparse
import json
from pathlib import Path
import re


def without_code(text):
    parts, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            parts.append("".join("\n" if c == "\n" else " " for c in line))
        elif fence:
            parts.append("".join("\n" if c == "\n" else " " for c in line))
        else:
            parts.append(re.sub(r"(`+)([^\n]*?)\1", lambda m: " " * len(m.group()), line))
    return "".join(parts)


def scan_text(text, path):
    view = without_code(text)
    findings, spans = [], []

    def flag(pos, fragment, reason, category):
        findings.append({
            "path": str(path), "line": text.count("\n", 0, pos) + 1,
            "column": pos - text.rfind("\n", 0, pos),
            "fragment": repr(fragment), "category": category,
            "certainty": "needs_context_review", "reason": reason,
        })

    # Limited Markdown/TeX delimiters; this is not a general TeX parser.
    pairs = {"$": "$", "$$": "$$", r"\(": r"\)", r"\[": r"\]"}
    opened = None
    for m in re.finditer(r"(?<!\\)(?:\$\$|\$|\\\(|\\\)|\\\[|\\\])", view):
        token = m.group()
        if opened is None:
            if token in pairs:
                opened = (token, m.start(), m.end())
            else:
                flag(m.start(), token, "发现孤立数学结束标记；核对所用显示记法。", "delimiter")
        elif token == pairs[opened[0]]:
            spans.append((opened[2], m.start()))
            opened = None
    if opened:
        flag(opened[1], opened[0], "数学标记未闭合；跨行公式或特殊记法需人工确认。", "delimiter")
        spans.append((opened[2], len(view)))
    # Simple parenthesized ASCII math; retain ordinary words and variable names.
    for m in re.finditer(r"\([^()\n]*\)", view):
        body = m.group()
        if re.search(r"[=^_+*/<>≤≥∈-]", body) or re.search(r"\b[A-Za-z](?:ge|le|in)(?=\s|[\[(])", body):
            if not any(a <= m.start() < b for a, b in spans):
                spans.append((m.start()+1, m.end()-1))

    seen = set()
    for start, end in spans:
        body = view[start:end]
        for m in re.finditer(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]|\t(?:heta|imes)(?=[^A-Za-z_]|$)", body):
            pos = start + m.start()
            if pos in seen:
                continue
            seen.add(pos)
            flag(pos, m.group(), "数学语境中有可疑控制字符/命令残片；先核对上下文，不自动删除。", "control")
        for pattern, reason in [
            (r"(?<![A-Za-z0-9_])[A-Za-z](?:_[A-Za-z0-9]+)?(?:ge|le)\s+[A-Za-z](?![A-Za-z0-9_])",
             "短符号与ge/le粘连，可能缺少比较运算符；也可能是变量名，不能自动替换。"),
            (r"(?<![A-Za-z0-9_])[A-Za-z](?:_[A-Za-z0-9]+)?in(?=\s*[\[(])",
             "短符号与in及区间括号粘连，可能缺少集合归属符；不能据此自动判错。"),
            (r"\bpartial[A-Za-z]+(?:[_^][A-Za-z{}]+)*\s*/\s*partial\s*[A-Za-z]",
             "表达式类似丢失命令的偏导；需核对对象、分母和所用ASCII记法。"),
        ]:
            for m in re.finditer(pattern, body):
                pos = start + m.start()
                if pos not in seen:
                    seen.add(pos)
                    flag(pos, m.group(), reason, "possible_operator_loss")
        # Combined counts allow valid half-open intervals.
        if r"\left." not in body and r"\right." not in body:
            if sum(body.count(c) for c in "([") != sum(body.count(c) for c in ")]"):
                flag(start, body[:160], "函数/分组括号数量不一致；检查跨行范围、区间及特殊定界符，不自动补括号。", "function_structure")
    unique = {(f["line"], f["column"], f["category"], f["fragment"]): f for f in findings}
    return sorted(unique.values(), key=lambda f: (f["line"], f["column"], f["category"]))


def scan_file(path):
    p = Path(path)
    try:
        if p.is_symlink():
            raise OSError("拒绝直接符号链接文件；请明确提供实际文件。")
        if not p.is_file():
            raise OSError("不是可读取的普通文件（不存在、目录或权限限制）。")
        text = p.read_bytes().decode("utf-8-sig")
    except (OSError, UnicodeError) as exc:
        return {"path": str(path), "status": "read_failed", "error": str(exc), "findings": []}
    findings = scan_text(text, path)
    return {"path": str(path), "status": "needs_context_review" if findings else "no_flags", "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="明确的UTF-8文件路径；不递归、不跟随正文链接")
    parser.add_argument("--json", action="store_true", help="打印JSON；不写输出文件或修改输入")
    args = parser.parse_args()
    results = [scan_file(p) for p in args.files]
    result = {"readonly": True, "results": results,
              "limit": "启发式提示需上下文确认；未覆盖所有LaTeX、控制字符或转换器；无告警不等于数学正确。"}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(f'{r["path"]}: {r["status"]}')
            if r.get("error"):
                print("  读取失败: " + r["error"])
            for f in r["findings"]:
                print(f'  {f["line"]}:{f["column"]} {f["fragment"]} — {f["reason"]}')
        print(result["limit"])
    return 2 if any(r["status"] == "read_failed" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
