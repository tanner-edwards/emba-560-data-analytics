"""Redact gmail/cricut email addresses in transcript files, keeping any JSON escape (\\n, \\uXXXX) that precedes them."""
import json
import re
import sys

pat = re.compile(r'(\\(?:[nrtbf]|u[0-9a-fA-F]{4}))?[\w.+-]+@(?:gmail|cricut)\.com', re.I)
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8", newline="").read()
    s2, n = pat.subn(lambda m: (m.group(1) or "") + "[redacted email]", s)
    open(f, "w", encoding="utf-8", newline="").write(s2)
    print(f, "redacted:", n, "left:", len(re.findall(r'@(?:gmail|cricut)\.com', s2, re.I)))
    if f.endswith(".jsonl"):
        for line in s2.splitlines():
            json.loads(line)
        print("  jsonl still valid")
