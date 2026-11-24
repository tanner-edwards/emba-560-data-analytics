"""Download the A10 raw datasets from Kaggle into data/raw/.

Run from the repo root:  python tools/get_data.py
Files are gitignored; every collaborator runs this once on their own machine.
data/raw/ is treated as read-only after download — never edit these files.
"""
import shutil
import urllib.request
from pathlib import Path

import truststore

# Use the OS certificate store so downloads work behind TLS-inspecting proxies (e.g. Zscaler)
truststore.inject_into_ssl()

import kagglehub  # noqa: E402

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"

# Kaggle handle -> (subfolder of data/raw, files expected). Recorded in the Data Receipt.
# stefanoleone992 gets its own subfolder: its rotten_tomatoes_movies.csv shares a
# filename with the (different) andrezaza file Matt's plan already uses.
DATASETS = {
    "asaniczka/tmdb-movies-dataset-2023-930k-movies": ("", ["TMDB_movie_dataset_v11.csv"]),
    "priyamchoksi/rotten-tomato-movie-reviews-1-44m-rows": ("", ["rotten_tomatoes_movie_reviews.csv"]),
    "andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews": ("", ["rotten_tomatoes_movies.csv"]),
    "stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset": (
        "stefanoleone992",
        ["rotten_tomatoes_movies.csv", "rotten_tomatoes_critic_reviews.csv"],
    ),
    # Scraped from the-numbers.com: budget, domestic/intl/worldwide gross, plus pre-release fields
    "michaelmatta0/movies-ultimate-metrics-features-and-metadata": (
        "the_numbers",
        ["Top Movies (Cleaned Data).csv"],
    ),
}

# Non-Kaggle direct downloads: (subfolder, filename) -> URL
URL_FILES = {
    # Box Office Mojo daily domestic grosses, scraped by github.com/tjwaterman99/boxofficemojo-scraper
    ("boxofficemojo", "revenues_per_day.csv.gz"):
        "https://github.com/tjwaterman99/boxofficemojo-scraper/releases/latest/download/revenues_per_day.csv.gz",
}


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    for (subdir, name), url in URL_FILES.items():
        print(f"\n== {url}")
        dst = RAW / subdir / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            print(f"  exists, skipping: {name}")
            continue
        urllib.request.urlretrieve(url, dst)
        print(f"  downloaded {name} ({dst.stat().st_size / 1e6:,.0f} MB)")
    for handle, (subdir, wanted) in DATASETS.items():
        print(f"\n== {handle}")
        src = Path(kagglehub.dataset_download(handle))
        dest_dir = RAW / subdir
        dest_dir.mkdir(parents=True, exist_ok=True)
        for name in wanted:
            dst = dest_dir / name
            if dst.exists():
                print(f"  exists, skipping: {dst.name}")
                continue
            matches = list(src.rglob(name))
            if not matches:
                available = sorted(p.name for p in src.rglob("*") if p.is_file())
                print(f"  NOT FOUND: {name}. Files in download: {available}")
                continue
            shutil.copy2(matches[0], dst)
            print(f"  copied {name} ({dst.stat().st_size / 1e6:,.0f} MB)")


if __name__ == "__main__":
    main()
