from __future__ import annotations

import html
from dataclasses import dataclass
from pathlib import Path

MEDIA_TYPES = {
    "video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "audio": {".mp3", ".flac", ".m4a", ".ogg", ".wav"},
}


@dataclass(frozen=True)
class MediaItem:
    path: str
    kind: str
    title: str


def classify(path: Path) -> str:
    ext = path.suffix.lower()
    for kind, exts in MEDIA_TYPES.items():
        if ext in exts:
            return kind
    return "other"


def scan(root: str | Path) -> list[MediaItem]:
    base = Path(root)
    items: list[MediaItem] = []
    all_exts = set().union(*MEDIA_TYPES.values())
    for path in sorted(p for p in base.rglob("*") if p.suffix.lower() in all_exts):
        rel = path.relative_to(base).as_posix()
        items.append(MediaItem(rel, classify(path), path.stem.replace(".", " ")))
    return items


def render_html(items: list[MediaItem], title: str = "medialoom") -> str:
    rows = "\n".join(
        f"<li data-kind='{html.escape(item.kind)}'>{html.escape(item.title)} <code>{html.escape(item.path)}</code></li>"
        for item in items
    )
    return f"<!doctype html><title>{html.escape(title)}</title><h1>{html.escape(title)}</h1><ul>{rows}</ul>"
