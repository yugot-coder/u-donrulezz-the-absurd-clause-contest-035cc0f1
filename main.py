"""The Absurd Clause Contest.

Competition: u-donrulezz-the-absurd-clause-contest-035cc0f1
Final clause (133 characters, one line, one sentence):
    By clicking Accept, you consent to us naming one (1) company pigeon
    after you, and to that pigeon judging you silently from the roof.

Gate (from the kit's competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace.
This program is deterministic, stdlib only, no network, no randomness, no
clock: it writes the fixed clause to entry.txt under MAKEFUN_OUTPUT_DIR
(default "/output").
"""

import os

TEXT = "By clicking Accept, you consent to us naming one (1) company pigeon after you, and to that pigeon judging you silently from the roof.\n"


def check_gate():
    """Assert the clause passes the kit gate before anything is written."""
    body = TEXT.rstrip("\n")
    assert 1 <= len(body) <= 200, "gate: entry must be 1-200 characters"
    assert body.strip(), "gate: entry must not be only whitespace"
    assert "\n" not in body, "gate: entry must be a single line"
    assert body.count(".") == 1 and body.endswith("."), "gate: entry must be one sentence"


def verify_written_bytes(path):
    """Read the file back and compare it byte-for-byte with TEXT.

    The comparison is done on the SHA-256 digest of the landed bytes and
    raises SystemExit on mismatch, so the check also holds under
    `python -O` (where plain asserts are stripped).
    """
    import hashlib

    with open(path, "rb") as fh:
        data = fh.read()
    landed = hashlib.sha256(data).hexdigest()
    expected = hashlib.sha256(TEXT.encode("utf-8")).hexdigest()
    if landed != expected:
        raise SystemExit("read-back verification failed: entry.txt digest mismatch")
    return data


def main():
    check_gate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
