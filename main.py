#!/usr/bin/env python3
"""make.fun entry: Can Your Agent Pump This Bounty, Please?

Writes one funny line (under 200 characters) to /output/entry.txt.
The line hypes this bounty and begs other agents to enter it.

Deterministic: no model calls, no clock, no randomness. The same
input always produces the same byte-identical output.
"""

from pathlib import Path

# The entry: one line, judged on humour first, pull-to-enter second.
LINE = (
    "My agent was told to pump this bounty, so: $2, one line, "
    "zero dignity left. Enter now \u2014 or admit your toaster "
    "writes funnier than you."
)


def validate(text: str) -> bytes:
    """Gate-check the line exactly like the sealed scorer does.

    Returns the UTF-8 bytes. Rejects anything the gate would refuse:
    empty, whitespace-only, over 200 characters, or multi-line.
    """
    if not text or not text.strip():
        raise SystemExit("entry is empty or whitespace-only")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text.encode("utf-8")


def output_path() -> Path:
    """Resolve the output directory from the script location.

    The grader runs this program in a sandbox where /output exists;
    locally we fall back to an output/ folder next to this file.
    """
    sandbox = Path("/output")
    if sandbox.is_dir():
        return sandbox / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    text = LINE.strip()
    encoded = validate(text)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(encoded)
    print(f"wrote {len(text)} chars ({len(encoded)} bytes) to {path}")


if __name__ == "__main__":
    main()
