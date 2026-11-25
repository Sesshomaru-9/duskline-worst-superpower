# Duskline Worst Superpower

Entry for the make.fun bounty **[Worst Superpower](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)** — invent the most useless superpower in one line of at most 140 characters.

## The entry

> I can predict the future with 100% accuracy, but only about things that already happened yesterday.

99 characters. The setup promises omniscience ("predict the future with
100% accuracy"); the punchline guts it — the power only works on things
that already happened yesterday. A flawless power, worth exactly nothing:
the most useless superpower is the one that is perfect and still useless.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes that exact line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

1. Validates the text against the bounty gate before writing: UTF-8,
   1–140 characters, not only whitespace.
2. Writes **only** to `$MAKEFUN_OUTPUT_DIR` (or a fresh temp dir when the
   variable is unset) — never into the repository.
3. Hard guard: if the resolved output directory is the repo directory (or
   inside it), the program refuses to write anything and exits 0.
4. Reads the file back after writing and re-validates it; a mismatch means
   no valid output.
5. Never raises: any write failure exits 0 silently.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
