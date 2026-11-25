#!/usr/bin/env python3
"""Duskline Worst Superpower — make.fun bounty entry.

Writes a single useless-superpower line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Rules (from the bounty gate):
  * /output/entry.txt must be UTF-8 text of 1-140 characters, not only
    whitespace. Only a valid entry goes before the judge.

Safety (hard rule, learned from the 'Two Hands, One Wheel' rejection):
  * The program writes ONLY to $MAKEFUN_OUTPUT_DIR (or a fresh temp dir
    when the variable is unset). It NEVER writes into the repo directory.
  * If the resolved output dir is the repo dir (or inside it), the program
    refuses to write anything and exits 0.
  * The program never raises: any write failure also exits 0 silently.
"""

import os
import sys
import tempfile

# The entry: a perfect power with a perfectly useless catch.
# Setup promises omniscience ("predict the future with 100% accuracy"),
# punchline guts it: it only works on things that already happened
# yesterday. The power is flawless — and worth exactly nothing.
# 99 characters.
ENTRY = "I can predict the future with 100% accuracy, but only about things that already happened yesterday."


def _repo_dir():
    """Directory containing this program (the repo root)."""
    return os.path.realpath(os.path.dirname(os.path.abspath(__file__)))


def _resolve_output_dir():
    """Return the output dir, or None when it must not be used."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if raw.strip():
        out = os.path.realpath(raw)
    else:
        # Fallback: a fresh temp dir, never the repo.
        out = tempfile.mkdtemp(prefix="duskline-worst-superpower-")
    repo = _repo_dir()
    if out == repo or out.startswith(repo + os.sep):
        return None
    return out


def _valid(text):
    """Gate check: UTF-8, 1-140 characters, not only whitespace."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 140):
        return False
    if not text.strip():
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    try:
        if not _valid(ENTRY):
            return 0
        out_dir = _resolve_output_dir()
        if out_dir is None:
            # Guard tripped: refuse to write, exit cleanly.
            return 0
        try:
            os.makedirs(out_dir, exist_ok=True)
        except OSError:
            return 0
        path = os.path.join(out_dir, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(ENTRY)
        except OSError:
            return 0
        # Read back and re-validate what actually landed on disk.
        try:
            with open(path, "r", encoding="utf-8") as fh:
                written = fh.read()
        except (OSError, UnicodeDecodeError):
            return 0
        if written != ENTRY or not _valid(written):
            return 0
        return 0
    except Exception:
        # Never raise: a failed write is a silent exit 0.
        return 0


if __name__ == "__main__":
    sys.exit(main())
