"""Export one Claude Code session into ai_logs/: verbatim .md rendering + raw .jsonl original.

Usage (from A10_Group):
    python -I tools/export_session.py <session-id> <file-stem> "<title>"
Writes:
    ai_logs/<file-stem>.md        the conversation file (user, Claude, tool calls, tool results, in order)
    ai_logs/raw/<file-stem>.jsonl the untouched original, as proof the .md is unedited

Finds <session-id>.jsonl under any folder in ~/.claude/projects, so it works no matter which
folder Claude Code was launched from. Safe to re-run: it overwrites both files with the fuller
transcript. Prints the covered time range so you can confirm the last prompt is included.
"""
import json, shutil, sys
from pathlib import Path

sid, stem, title = sys.argv[1], sys.argv[2], sys.argv[3]
logs = Path(__file__).resolve().parent.parent / "ai_logs"
hits = list((Path.home() / ".claude" / "projects").glob(f"*/{sid}.jsonl"))
if len(hits) != 1:
    sys.exit(f"Expected exactly one transcript for {sid}, found {len(hits)}: {hits}")
src = hits[0]
(logs / "raw").mkdir(exist_ok=True)
shutil.copyfile(src, logs / "raw" / f"{stem}.jsonl")


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(c["text"] for c in content if isinstance(c, dict) and "text" in c)


out = [f"# {title}", "",
       f"Source: Claude Code session `{sid}`; raw original at `ai_logs/raw/{stem}.jsonl`.",
       "Rendered verbatim: user messages, attached documents, Claude replies and reasoning, tool calls "
       "and tool results, in order. Internal harness records (request metadata, file snapshots) are "
       "omitted here but present in the raw file.", ""]
ts, users = [], 0
for line in open(src, encoding="utf-8"):
    d = json.loads(line)
    if d.get("timestamp"):
        ts.append(d["timestamp"])
    if d.get("type") not in ("user", "assistant"):
        continue
    t0 = d.get("timestamp", "")
    content = (d.get("message") or {}).get("content")
    if d["type"] == "user":
        if isinstance(content, str):
            out += [f"## User  ({t0})", "", content, ""]
            users += 1
            continue
        for c in content or []:
            kind = c.get("type")
            if kind == "text":
                out += [f"## User  ({t0})", "", c["text"], ""]
                users += 1
            elif kind == "document":
                s = c.get("source", {})
                body = s.get("data") if s.get("type") == "text" else json.dumps(s)[:2000]
                out += [f"## User - attached document: {c.get('title', '')}  ({t0})", "", "````", body or "", "````", ""]
            elif kind == "tool_result":
                out += [f"**Tool result** ({t0})", "", "````", text_of(c.get("content", "")), "````", ""]
    else:
        for c in content or []:
            kind = c.get("type")
            if kind == "text" and c["text"].strip():
                out += [f"## Claude  ({t0})", "", c["text"], ""]
            elif kind == "thinking" and c.get("thinking", "").strip():
                out += [f"*Claude reasoning ({t0}):*", "", "> " + c["thinking"].replace("\n", "\n> "), ""]
            elif kind == "tool_use":
                out += [f"**Tool call: {c['name']}** ({t0})", "", "````json",
                        json.dumps(c.get("input"), indent=2, ensure_ascii=False), "````", ""]

(logs / f"{stem}.md").write_text("\n".join(out), encoding="utf-8")
print(f"wrote   ai_logs/{stem}.md  and  ai_logs/raw/{stem}.jsonl")
print(f"covers  {min(ts)}  to  {max(ts)}  (UTC)   user turns: {users}")
