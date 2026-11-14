#!/usr/bin/env python3
"""Write the agency poem to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the poem is read from entry.txt beside this file, its
SHA-256 is verified against the expected digest, and the exact bytes are
written out. Standard library only, no network, no randomness.
"""

import hashlib
import os
import sys
from pathlib import Path

EXPECTED_SHA256 = "41ab53acb60e8ace125169452321a69436caa845c8662d0a5ee3b311eaf567f8"


def main() -> int:
    here = Path(__file__).resolve().parent
    poem_path = here / "entry.txt"
    poem = poem_path.read_bytes()

    digest = hashlib.sha256(poem).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"poem hash mismatch: got {digest}, want {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1

    # Mirror the competition gate: UTF-8, 1-1000 code points, at least one
    # non-whitespace character. Refuse to write an invalid poem.
    try:
        text = poem.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"poem is not valid UTF-8: {exc}", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 1000 or not any(not c.isspace() for c in text):
        print("poem fails the gate (length or whitespace)", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(poem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
