
---

### ✅ **`js_analyzer.py` Code**

```python
import re
import sys
from pathlib import Path

def analyze_js(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return

    print(f"\n🔍 Analyzing: {file_path}\n" + "-"*50)

    # Regex patterns
    url_regex = re.compile(r"https?://[^\s\"'`<>{}]+")
    token_regex = re.compile(r"\b(?:token|auth|key|secret|jwt|session)[a-z0-9_]*\b", re.I)
    dangerous_calls_regex = re.compile(r"\b(eval|document\.write|innerHTML|outerHTML|setTimeout|setInterval|Function)\b")

    # Match findings
    api_urls = sorted(set(url_regex.findall(content)))
    tokens = sorted(set(token_regex.findall(content)))
    dangerous_calls = sorted(set(dangerous_calls_regex.findall(content)))

    # Format results
    output_lines = []
    output_lines.append("🔗 API Endpoints Found:\n")
    output_lines.extend([f"  - {url}" for url in api_urls] or ["  ❌ None found"])
    output_lines.append("\n\n🔐 Tokens / Secrets / Keys:\n")
    output_lines.extend([f"  - {token}" for token in tokens] or ["  ❌ None found"])
    output_lines.append("\n\n⚠️ Dangerous Function Calls:\n")
    output_lines.extend([f"  - {func}" for func in dangerous_calls] or ["  ❌ None found"])

    # Save to single file
    out_file = Path(file_path).stem + "_analysis.txt"
    Path(out_file).write_text("\n".join(output_lines), encoding="utf-8")

    print(f"✅ Results saved to: {out_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Usage: python3 js_analyzer.py <javascript_file.js>")
    else:
        analyze_js(sys.argv[1])
