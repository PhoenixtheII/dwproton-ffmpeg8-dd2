#!/usr/bin/env python3
"""Patch a Proton build tree for the Steam Runtime's Python 3.9.

Usage: patch-python39.py /path/to/dwproton-ffmpeg8
"""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit(f"usage: {sys.argv[0]} /path/to/proton-build")

root = Path(sys.argv[1])
if not (root / "proton").exists():
    raise SystemExit(f"not a Proton build tree: {root}")


def add_future(path: str, after: int = 0) -> None:
    file = root / path
    lines = file.read_text().splitlines()
    if "from __future__ import annotations" not in lines:
        lines.insert(after, "from __future__ import annotations")
        file.write_text("\n".join(lines) + "\n")
        print(f"patched {file}")


add_future("vulkan.py", 0)
vulkan = root / "vulkan.py"
text = vulkan.read_text()
text = text.replace(
    "from typing import Self\n",
    """try:
    from typing import Self
except ImportError:
    Self = object
""",
)
vulkan.write_text(text)

add_future("utilities.py", 1)
add_future("proton", 1)
add_future("protonfixes/upscalers.py", 1)
