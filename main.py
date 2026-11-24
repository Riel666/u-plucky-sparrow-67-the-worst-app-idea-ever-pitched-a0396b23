"""One sentence pitching the worst, most useless app idea imaginable, under 240 characters.
"""

import os

TEXT = "SyncSink: an app that syncs your to-do list across all your devices so you can feel guilty about the same unfinished tasks everywhere, in real time, with push notifications."


def main():
    assert 1 <= len(TEXT) <= 240, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
