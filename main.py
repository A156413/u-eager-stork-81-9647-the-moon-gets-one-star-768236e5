"""The Moon Gets One Star — a one-line review of the Moon.

Entry: a single 112-character review, written to $MAKEFUN_OUTPUT_DIR/entry.txt
and printed to stdout. Deterministic: no network, no randomness, no clock.
Python 3.13, standard library only.
"""

import os
import stat

ENTRY_TEXT = (
    "One star. Shows up late, only half-lit, and still expects the tides "
    "to revolve around it. Would not orbit again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")
    # The harness collects outputs as another user, so the file must be
    # world-readable (0644), not the 0600 default of some temp-file helpers.
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
