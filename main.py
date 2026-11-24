#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (146 chars) pitching ToasterClaim, a lazy-agent
micro-startup that files warranty claims for dead toaster ovens, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: no input, no randomness, no network, no trailing newline.
"""

import os

PITCH = (
    "ToasterClaim: a lazy agent that files warranty claims for dead toaster "
    "ovens, splitting each $40 refund 50/50 with owners who never lift a finger."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 200, f"pitch length {len(PITCH)} out of range 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt".rsplit("/", 1)[0])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Read-back gate: what landed on disk must be byte-for-byte the pitch.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == PITCH, "entry.txt does not match the pitch"
    assert 1 <= len(written) <= 200, "written entry length out of range 1-200"


if __name__ == "__main__":
    main()
