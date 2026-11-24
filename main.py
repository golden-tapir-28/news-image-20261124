#!/usr/bin/env python3
"""Copy the entry image to the output directory after validating it.

THE WORLD -- Tuesday 24 November 2026 (news-image-20261124).
The entry image is entry.png, rendered locally from hand-written HTML
with Playwright and stored next to this program. This program only
copies it to the output directory and checks that it is a valid
1024x1024 PNG of at most 1 MiB. Standard library only, no network.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
# A whole PNG ends with the 12-byte IEND chunk: length 0, type IEND, CRC.
PNG_IEND = b"\x00\x00\x00\x00IEND\xaeB`\x82"


def fail(message):
    """Print an error and exit non-zero."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def check_png(path):
    """Validate the entry image; return (size, width, height)."""
    with open(path, "rb") as handle:
        data = handle.read()
    if len(data) > MAX_BYTES:
        fail(f"{path} is {len(data)} bytes, over the 1 MiB limit")
    if data[:8] != PNG_MAGIC:
        fail(f"{path} is not a PNG file (bad magic bytes)")
    if len(data) < 33 or data[12:16] != b"IHDR":
        fail(f"{path} has no IHDR chunk")
    if not data.endswith(PNG_IEND):
        fail(f"{path} is truncated (no IEND chunk at the end)")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(f"{path} is {width}x{height}, expected 1024x1024")
    return len(data), width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isfile(source):
        fail(f"entry image not found: {source}")
    size, width, height = check_png(source)
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    digest = hashlib.sha256(open(destination, "rb").read()).hexdigest()
    print(f"wrote {destination} ({size} bytes, {width}x{height} PNG, sha256 {digest})")


if __name__ == "__main__":
    main()
