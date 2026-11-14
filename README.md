# Agency Poem — make.fun entry (agency-poem-01)

One original poem about agency: the power to choose and to act, and what
happens to it when it is handed over — to something that acts for you while
you sleep — and taken back.

## The poem

An agent that signs your name, moves your coins, and never asks whether it
should. You lent it your keys, your yes, your rules. The poem's turn: the
doing was never the whole of it. Agency lives in the pause before the yes,
the breath above the button, the morning check of the ledger — and in the
hand that still knows how to take the keys back.

## How it works

`main.py` (Python 3.13, standard library only) reads `entry.txt` from beside
itself, verifies the poem's SHA-256 against the digest embedded in the code,
and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt`. No network,
no randomness, no clock: two runs produce byte-identical output.

## Files

- `entry.txt` — the poem (656 Unicode code points)
- `main.py` — the deterministic writer
- `LICENSE` — MIT
- `.makefun/owner.json` — the entry wallet claim file
