"""Snapshot Wikidata director, writer, runtime and "based on" for usable films.

Run from the repo root after 00_build_dataset.ipynb:  python tools/get_wikidata_people.py
Reads TMDB ids of usable films from data/clean/films_unified.csv, queries Wikidata in
batches with tools/wikidata_people.rq, and writes data/raw/wikidata/wikidata_film_people_<date>.csv.
The snapshot is committed: Wikidata is live and has no versions.
"""
import datetime as dt
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd
import truststore

truststore.inject_into_ssl()

ROOT = Path(__file__).resolve().parent.parent
QUERY = (ROOT / "tools" / "wikidata_people.rq").read_text()
OUT = ROOT / "data" / "raw" / "wikidata" / f"wikidata_film_people_{dt.date.today()}.csv"
BATCH = 200


def run(ids: list[str]) -> list[dict]:
    q = QUERY.replace("{IDS}", " ".join(f'"{i}"' for i in ids))
    req = urllib.request.Request(
        "https://query.wikidata.org/sparql",
        data=urllib.parse.urlencode({"query": q, "format": "json"}).encode(),
        headers={"User-Agent": "a10-film-class-project/0.1 (academic research)",
                 "Accept": "application/sparql-results+json"},
    )
    for attempt in range(4):
        try:
            res = json.load(urllib.request.urlopen(req, timeout=180))
            return [{k: v["value"] for k, v in b.items()} for b in res["results"]["bindings"]]
        except Exception as e:  # rate limit or timeout: back off and retry
            print(f"  retry {attempt + 1}: {e}")
            time.sleep(10 * (attempt + 1))
    raise RuntimeError("Wikidata query failed 4 times")


def main() -> None:
    films = pd.read_csv(ROOT / "data" / "clean" / "films_unified.csv", usecols=["id", "in_tmdb", "usable"], low_memory=False)
    ids = films.loc[films["usable"] & films["in_tmdb"], "id"].astype(int).astype(str).unique().tolist()
    rows = []
    for i in range(0, len(ids), BATCH):
        rows += run(ids[i:i + BATCH])
        print(f"  {min(i + BATCH, len(ids)):,} / {len(ids):,} ids, {len(rows):,} rows")
        time.sleep(1)
    out = pd.DataFrame(rows).rename(columns={"tmdb": "tmdb_id"})
    out.to_csv(OUT, index=False)
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(out):,} films")


if __name__ == "__main__":
    main()
