#!/usr/bin/env python3
"""Build assets/readme-hero.svg with the current GitHub avatar embedded.

Run locally or via .github/workflows/sync-avatar.yml. The avatar is
fetched from https://github.com/{USER}.png, resized, and base64-embedded
directly into the SVG so it renders on GitHub without external fetches.
"""
from __future__ import annotations

import base64
import io
import sys
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image

USER = "XIU-kr"
AVATAR_URL = f"https://github.com/{USER}.png?size=560"

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "readme-hero.svg"

# Edit this list to change what appears in the card.
PROJECTS: list[tuple[str, str, str]] = [
    ("01", "Vora AI",     "Browser-based AI image editor — inpainting, segmentation, masks"),
    ("02", "Quon",        "Ad-light QR code generator — web + native Android"),
    ("03", "bbangyadan",  "Discord clan operations platform — points, voice, embeds"),
    ("04", "Phos",        "Worship-PPT auto-generator — 645 hymns + Korean Bible"),
    ("05", "CornerBrand", "Local-first watermarking for images, PDFs and PPTX"),
    ("06", "CS2 Plugins", "Open-source plugins for the cs2.kr community server"),
]

DISPLAY = "'Didot','Bodoni 72','Playfair Display','Hoefler Text',Georgia,'Times New Roman',serif"
SANS = "'Helvetica Neue',-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif"

PAPER = "#f7f3ea"
INK = "#141216"
MUTED = "#7a7368"


def fetch_avatar_data_uri() -> str:
    req = urllib.request.Request(
        AVATAR_URL,
        headers={"User-Agent": f"{USER}-readme-builder/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()

    img = Image.open(io.BytesIO(raw)).convert("RGB")
    img.thumbnail((280, 280), Image.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=86, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return "data:image/jpeg;base64," + b64


def project_row(num: str, name: str, desc: str, y: int) -> str:
    return (
        f'  <g transform="translate(80 {y})">\n'
        f'    <text font-family="{SANS}" font-size="11" letter-spacing="1.8" '
        f'fill="{MUTED}">{escape(num)}</text>\n'
        f'    <text x="52" font-family="{DISPLAY}" font-weight="400" font-size="20" '
        f'fill="{INK}">{escape(name)}</text>\n'
        f'    <text x="232" font-family="{SANS}" font-size="13" '
        f'fill="{MUTED}">— {escape(desc)}</text>\n'
        f'  </g>'
    )


def build_svg(avatar_data_uri: str) -> str:
    row_y0 = 348
    row_gap = 34
    rows = "\n".join(
        project_row(num, name, desc, row_y0 + i * row_gap)
        for i, (num, name, desc) in enumerate(PROJECTS)
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" role="img" aria-labelledby="title">
  <title id="title">XIU — a curious developer from Seoul</title>
  <defs>
    <clipPath id="avatar-clip"><circle cx="160" cy="164" r="80"/></clipPath>
  </defs>

  <!-- paper -->
  <rect width="1200" height="560" fill="{PAPER}"/>

  <!-- avatar -->
  <image href="{avatar_data_uri}" x="80" y="84" width="160" height="160"
         clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>
  <circle cx="160" cy="164" r="80" fill="none" stroke="{INK}" stroke-width="1" opacity="0.18"/>

  <!-- identity -->
  <text x="280" y="178" font-family="{DISPLAY}" font-weight="400" font-size="108"
        fill="{INK}" letter-spacing="3">XIU</text>
  <text x="280" y="208" font-family="{DISPLAY}" font-style="italic" font-size="20"
        fill="{MUTED}">a curious developer</text>
  <text x="280" y="234" font-family="{SANS}" font-size="11" letter-spacing="2.6"
        fill="{MUTED}">GITHUB.COM &#160;/&#160; {escape(USER.upper())}</text>

  <!-- top-right metadata -->
  <text x="1120" y="102" text-anchor="end" font-family="{SANS}" font-size="11"
        letter-spacing="2.6" fill="{MUTED}">SEOUL &#160;·&#160; REPUBLIC OF KOREA</text>
  <text x="1120" y="122" text-anchor="end" font-family="{SANS}" font-size="11"
        letter-spacing="2.6" fill="{MUTED}">ESTABLISHED &#160;·&#160; MMXXVI</text>

  <!-- divider -->
  <line x1="80" y1="272" x2="1120" y2="272" stroke="{INK}" stroke-width="0.6" opacity="0.18"/>

  <!-- section label -->
  <text x="80" y="306" font-family="{SANS}" font-size="11" letter-spacing="3.6"
        fill="{MUTED}">— &#160; SELECTED WORK</text>

{rows}
</svg>
'''


def main() -> int:
    try:
        uri = fetch_avatar_data_uri()
    except Exception as e:  # noqa: BLE001
        print(f"failed to fetch avatar: {e}", file=sys.stderr)
        return 1

    svg = build_svg(uri)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(svg)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
