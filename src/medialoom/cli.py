from __future__ import annotations

import argparse
from .core import render_html, scan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a static local media catalog.")
    parser.add_argument("directory")
    args = parser.parse_args(argv)
    print(render_html(scan(args.directory)))
    return 0
