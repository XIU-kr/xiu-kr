#!/usr/bin/env python3
"""Build assets/readme-hero.svg — the XIU profile card.

Fetches the current GitHub avatar, base64-embeds it into an SVG, and
writes the result to assets/readme-hero.svg. The aesthetic mirrors
xiu.kr: deep navy background, warm gold accents, teal secondary, a
subtle dotted grid overlay, and a gold→light gradient wordmark.

Run locally (`python scripts/build-hero.py`) or via
.github/workflows/sync-avatar.yml.
"""
from __future__ import annotations

import base64
import hashlib
import io
import re
import sys
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image

USER = "XIU-kr"
AVATAR_URL = f"https://github.com/{USER}.png?size=560"

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "readme-hero.svg"
README = ROOT / "README.md"

# ─── Palette (lifted from xiu.kr) ──────────────────────────────────────────
BG = "#07070b"
LAYER = "#0e0e15"
GOLD = "#d4a016"
GOLD_DIM = "#8a6810"
TEAL = "#2dd4a8"
TEXT = "#e4e4ec"
MUTED = "#8a8aa6"
BORDER = "#1e1e30"

# ─── Font stacks ───────────────────────────────────────────────────────────
# Attempts Syne/Outfit/Fira (used on xiu.kr); falls through to modern
# system sans on GitHub where web fonts cannot be loaded from SVG.
DISPLAY = "'Syne','Inter',-apple-system,system-ui,'Segoe UI','Helvetica Neue',Arial,sans-serif"
BODY = "'Outfit','Inter',-apple-system,system-ui,'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'Fira Code','JetBrains Mono','SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# ─── Content ───────────────────────────────────────────────────────────────
# Left column — Web Sites with three sub-groups
WEB_SITES = [
    ("Personal", [
        ("xiu.kr", "personal portfolio"),
        ("quon.xiu.kr", "free QR code generator"),
    ]),
    ("Church", [
        ("dongtanms.kr", "Church Site · Rhymix CMS"),
        ("repentanceheaven.kr", "mission organization site"),
        ("shop.repentanceheaven.kr", "online bookstore · WooCommerce"),
    ]),
    ("Community", [
        ("cs2.kr", "Korea Counter-Strike 2 community"),
        ("bbangyadan.kr", "Valorant clan platform"),
    ]),
]

# Right column — flat list of categories
RIGHT_CATEGORIES = [
    ("Web Apps", [
        ("Vora AI", "browser-based AI image editor"),
        ("CornerBrand", "local-first image watermarking"),
    ]),
    ("Church Apps", [
        ("Phos", "worship PPT auto-generator"),
        ("Poima", "church membership & finance management"),
    ]),
    ("Android Apps", [
        ("Quon", "QR code generator"),
        ("Parking Management", "for Dongtan Myungsung Church"),
        ("Church App", "official Dongtan Myungsung Church app"),
    ]),
    ("Game Server Plugins", [
        ("GrenadeBoost", "custom-physics grenade boosting"),
        ("AutoRestart", "timezone-aware scheduled restart"),
        ("DU-NicknameSync", "Steam \u2194 Discord nickname sync"),
    ]),
]


# ─── Avatar fetch ──────────────────────────────────────────────────────────
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


# ─── SVG helpers ───────────────────────────────────────────────────────────
def cat_header(text: str, x: int, y: int) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="19" '
        f'letter-spacing="3.4" fill="{GOLD}" font-weight="600">'
        f'{escape(text.upper())}'
        f'</text>'
    )


def sub_header(text: str, x: int, y: int) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="14" '
        f'letter-spacing="2.4" fill="{TEAL}" opacity="0.85">'
        f'&#8213;&#160;&#160; {escape(text.lower())}'
        f'</text>'
    )


def item_line(name: str, desc: str, x: int, y: int) -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="{BODY}" font-size="16.5" fill="{TEXT}" font-weight="500">'
        f'{escape(name)}'
        f'<tspan fill="{MUTED}" font-weight="400">&#160;&#160;&#8212;&#160;&#160;{escape(desc)}</tspan>'
        f'</text>'
    )


def build_left_column(x: int, y0: int) -> tuple[str, int]:
    parts: list[str] = []
    y = y0
    parts.append(cat_header("Web Sites", x, y))
    y += 42

    for sub_name, items in WEB_SITES:
        parts.append(sub_header(sub_name, x + 4, y))
        y += 28
        for name, desc in items:
            parts.append(item_line(name, desc, x + 22, y))
            y += 28
        y += 14

    return "\n  ".join(parts), y


def build_right_column(x: int, y0: int) -> tuple[str, int]:
    parts: list[str] = []
    y = y0

    for i, (cat_name, items) in enumerate(RIGHT_CATEGORIES):
        parts.append(cat_header(cat_name, x, y))
        y += 40
        for name, desc in items:
            parts.append(item_line(name, desc, x + 18, y))
            y += 28
        if i < len(RIGHT_CATEGORIES) - 1:
            y += 18

    return "\n  ".join(parts), y


# ─── SVG build ─────────────────────────────────────────────────────────────
def build_svg(avatar_data_uri: str) -> str:
    canvas_w = 1200
    canvas_h = 900

    left_svg, _ = build_left_column(x=80, y0=306)
    right_svg, _ = build_right_column(x=640, y0=306)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas_w} {canvas_h}" role="img" aria-labelledby="title">
  <title id="title">XIU — a curious developer from Seoul</title>

  <defs>
    <!-- avatar clip -->
    <clipPath id="avatar-clip"><circle cx="160" cy="160" r="80"/></clipPath>

    <!-- wordmark gradient: gold → light -->
    <linearGradient id="wordmark-grad" x1="0" y1="0" x2="1" y2="0.4">
      <stop offset="0" stop-color="{GOLD}"/>
      <stop offset="0.55" stop-color="#f2d67b"/>
      <stop offset="1" stop-color="{TEXT}"/>
    </linearGradient>

    <!-- ambient radial glow behind the identity -->
    <radialGradient id="glow" cx="0.16" cy="0.22" r="0.55">
      <stop offset="0" stop-color="{GOLD}" stop-opacity="0.18"/>
      <stop offset="0.45" stop-color="{GOLD}" stop-opacity="0.05"/>
      <stop offset="1" stop-color="{GOLD}" stop-opacity="0"/>
    </radialGradient>

    <!-- teal glow far right for secondary warmth -->
    <radialGradient id="glow-teal" cx="0.9" cy="0.08" r="0.4">
      <stop offset="0" stop-color="{TEAL}" stop-opacity="0.10"/>
      <stop offset="1" stop-color="{TEAL}" stop-opacity="0"/>
    </radialGradient>

    <!-- fine dotted grid overlay -->
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.8" fill="{TEXT}" opacity="0.06"/>
    </pattern>

    <!-- avatar ring gradient -->
    <linearGradient id="ring-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{GOLD}" stop-opacity="0.95"/>
      <stop offset="1" stop-color="{GOLD}" stop-opacity="0.25"/>
    </linearGradient>

    <!-- divider gradient -->
    <linearGradient id="divider-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{GOLD}" stop-opacity="0"/>
      <stop offset="0.15" stop-color="{GOLD}" stop-opacity="0.6"/>
      <stop offset="0.85" stop-color="{GOLD}" stop-opacity="0.6"/>
      <stop offset="1" stop-color="{GOLD}" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- stage -->
  <rect width="{canvas_w}" height="{canvas_h}" fill="{BG}"/>
  <rect width="{canvas_w}" height="{canvas_h}" fill="url(#glow)"/>
  <rect width="{canvas_w}" height="{canvas_h}" fill="url(#glow-teal)"/>
  <rect width="{canvas_w}" height="{canvas_h}" fill="url(#dots)"/>

  <!-- inner frame hairline -->
  <rect x="48" y="48" width="{canvas_w - 96}" height="{canvas_h - 96}"
        fill="none" stroke="{BORDER}" stroke-width="1" rx="2"/>

  <!-- ─── Identity ──────────────────────────────────────────────── -->

  <!-- avatar soft glow -->
  <circle cx="160" cy="160" r="92" fill="{GOLD}" opacity="0.12"/>
  <circle cx="160" cy="160" r="86" fill="{BG}"/>

  <!-- avatar image -->
  <image href="{avatar_data_uri}" x="80" y="80" width="160" height="160"
         clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice"/>

  <!-- avatar ring -->
  <circle cx="160" cy="160" r="80" fill="none" stroke="url(#ring-grad)" stroke-width="1.6"/>

  <!-- wordmark -->
  <text x="280" y="180" font-family="{DISPLAY}" font-weight="700" font-size="120"
        fill="url(#wordmark-grad)" letter-spacing="-2">XIU</text>

  <!-- tagline -->
  <text x="284" y="216" font-family="{BODY}" font-size="19"
        fill="{MUTED}">a curious developer &#160;·&#160; makes things he wants to use</text>

  <!-- handle -->
  <text x="284" y="244" font-family="{MONO}" font-size="13"
        fill="{GOLD}" letter-spacing="1.2" opacity="0.9">&#x2192;&#160; github.com/{escape(USER)}</text>

  <!-- divider -->
  <line x1="80" y1="274" x2="{canvas_w - 80}" y2="274"
        stroke="url(#divider-grad)" stroke-width="1"/>

  <!-- ─── Category grid ────────────────────────────────────────── -->

  <!-- vertical column separator -->
  <line x1="614" y1="300" x2="614" y2="832"
        stroke="{BORDER}" stroke-width="1" opacity="0.8"/>

  <!-- left column: Web Sites -->
  {left_svg}

  <!-- right column: 5 categories -->
  {right_svg}

  <!-- ─── Bottom rule ──────────────────────────────────────────── -->
  <line x1="80" y1="844" x2="{canvas_w - 80}" y2="844"
        stroke="{BORDER}" stroke-width="1" opacity="0.8"/>

  <text x="80" y="870" font-family="{MONO}" font-size="11"
        letter-spacing="2.8" fill="{GOLD}" opacity="0.85">&#x2192;&#160;&#160; click anywhere to get in touch</text>
  <text x="{canvas_w - 80}" y="870" text-anchor="end" font-family="{MONO}" font-size="11"
        letter-spacing="2.8" fill="{MUTED}" opacity="0.72">xiu.kr</text>
</svg>
'''


def sync_readme_cachebuster(svg: str) -> None:
    """Rewrite README's hero <img src="...?v=HASH"> with a hash of the SVG.

    GitHub's camo image proxy caches images by URL. Without a new query
    string the README keeps serving the stale SVG even after the file
    changes on disk. Hashing the SVG means the query only changes when
    the image actually changes — no churn on idle rebuilds.
    """
    if not README.exists():
        return

    token = hashlib.sha256(svg.encode("utf-8")).hexdigest()[:10]
    text = README.read_text(encoding="utf-8")

    pattern = re.compile(r'(readme-hero\.svg)(\?v=[A-Za-z0-9]+)?')
    new_text, n = pattern.subn(rf"\1?v={token}", text, count=1)

    if n and new_text != text:
        README.write_text(new_text, encoding="utf-8")
        print(f"updated README cache buster → v={token}")


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

    sync_readme_cachebuster(svg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
