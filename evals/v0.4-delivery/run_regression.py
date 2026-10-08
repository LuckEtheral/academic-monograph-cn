"""Small standard-library delivery regression. No models, browser or CI.
Copies self-written fixtures to a temporary directory; input is not modified.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

E=Path(__file__).resolve().parent
script=E.parents[1]/"skills/chinese-research-monograph/scripts/check_math_text.py"
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expect=json.loads((E/"expected/expectations.json").read_text())
sources={p.name:H(p) for p in (E/"inputs").glob("*.md")}
records=[]
with tempfile.TemporaryDirectory(prefix="monograph-delivery-") as tmp:
    T=Path(tmp)
    for name in sources:
        shutil.copyfile(E/"inputs"/name,T/name)
    normal=(T/"normal.md").read_text()
    wire=json.dumps({"text":normal},ensure_ascii=False)
    restored=json.loads(wire)["text"]
    (T/"roundtrip.md").write_bytes(restored.encode("utf-8"))
    assert (T/"roundtrip.md").read_bytes()==(T/"normal.md").read_bytes()
    (T/"directory").mkdir()
    (T/"link.md").symlink_to(T/"normal.md")
    for name,want in expect.items():
        before=H(T/name) if name in sources else None
        run=subprocess.run([sys.executable,str(script),"--json",name],cwd=T,
                           capture_output=True,text=True)
        data=json.loads(run.stdout)
        item=data["results"][0]
        assert item["status"]==want["status"],(name,item)
        assert run.returncode==want.get("exit_code",0)
        if "required_lines" in want:
            assert set(want["required_lines"]) <= {f["line"] for f in item["findings"]}
            assert set(want["categories"]) <= {f["category"] for f in item["findings"]}
        elif want.get("categories")==[]:
            assert not item["findings"],(name,item)
        unchanged=before==H(T/name) if name in sources else True
        assert unchanged
        records.append({"input":name,"exit_code":run.returncode,"actual":item,"input_unchanged":unchanged})
    assert "\tprint" in (T/"control.md").read_text()
    assert "\t |" in (T/"control.md").read_text()
assert sources=={p.name:H(p) for p in (E/"inputs").glob("*.md")}
result={"identity":"self-written delivery/tool regression, not scientific capability evaluation",
        "utf8_JSON_file_roundtrip":"PASS","cases":records,
        "normal_code_and_table_tabs_retained":True,"source_fixtures_unchanged":True,
        "model_sessions":0,"limit":"finite heuristic examples; no universal LaTeX/renderer coverage claim"}
(E/"outputs/actual.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"roundtrip":"PASS","cases":len(records),"inputs_unchanged":True,"model_sessions":0}))
