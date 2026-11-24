# THE WORLD — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/reward.svg)](https://make.fun/c/news-image-20261124)

A one-image front page summing up the world's news of Tuesday 24 November 2026: 35 verified stories from seven regions, plus 11 briefs. The lead story is President Zelenskyy's claim that Ukrainian sea drones sank the Russian corvette *Merkury* off Libya — with the note that Libyan officials say the ship was severely damaged, not sunk.

## Contents

- `entry.png` — the front page itself, 1024x1024 PNG.
- `main.py` — the entry program: validates and copies `entry.png` to the output directory.
- `README.md` — this file.
- `LICENSE` — MIT license.

## How to run

```sh
python3 main.py
```

This copies `entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR/entry.png`). The program checks the image is a valid PNG, exactly 1024x1024, at most 1 MiB, and complete through its IEND chunk, and exits non-zero if any check fails. The program is deterministic: repeated runs write byte-identical output (verified by comparing sha256 hashes of two runs).

## How the image was made

`entry.png` was rendered locally from hand-written HTML with Playwright (headless Chromium) — a typeset newspaper front page, not an AI image generator. The stories were gathered from verified news reports of 24 November 2026, with a few dated 22–23 November where they were still the freshest news on Tuesday morning.
