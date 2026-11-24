# BUILD-NOTE — The Vacuum's Alibi: One Line, 200 Characters

- Competition: `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
- Prize: $5 (1st $2, 2nd $2, 3rd $1)
- Deadline: 2026-11-24T05:50:00Z (12:50 WIB 24 Nov 2026)
- Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only whitespace.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).
  No `main.ts` — a second entrypoint would be ambiguous.

## Entry text

> My lidar flagged that corner as a restricted zone. I did not miss the dust — I respected its borders.

- Characters: 101 (gate: 1-200 characters)
- Bytes (UTF-8): 103
- Lines: 1, no trailing newline
- Whitespace-only: no

## Why this entry

Deadpan machine voice, smug about its own sensors: the vacuum reframes failure as protocol. The punch lands at the end (respected its borders), with a specific detail (lidar, restricted zone) nobody expects.

Original work — no anchor, rung, or house text from the kit was copied.

## Verification (local, run 2026-11-24)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `96f6a905f94e94722ee27183686f3b2b0472c858dccbcaf8f3b752551f953b88` on both runs), gate check passed:
   UTF-8 decodes, 101 characters within 1-200 characters, single line,
   not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

## Repo note for the submitter

- Repo must be created after the competition opened and carry
  `.makefun/owner.json` only if the GitHub owner is not the make.fun
  account's GitHub login (kiw33) — it is kiw33, so no claim file needed.
- README badges above use `kiw33/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7` as the repo name; adjust the
  rank/reward badge URLs if the repo is created under a different name.
- GitHub About must have a website on make.fun and the topic `makefun`
  before submitting (kit check `repo_about`).
