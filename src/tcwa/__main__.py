"""Entry point for ``python -m tcwa``."""

import argparse
from collections.abc import Sequence

from tcwa import __version__


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tcwa",
        description="Analyze agent session transcripts for token cost and waste.",
    )
    parser.add_argument("--version", action="version", version=f"tcwa {__version__}")
    parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
