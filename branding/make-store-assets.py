#!/usr/bin/env python3
"""Generate Chrome Web Store graphic assets from the branding sources.

The store wants exact pixel sizes that none of our source art matches, and it
rejects anything with an alpha channel except the store icon. This composes
every required asset onto the brand background and writes 24-bit PNGs.

Needs Pillow, which is not a dependency of the extension itself:

    python3 -m venv .venv && .venv/bin/pip install Pillow
    .venv/bin/python branding/make-store-assets.py

Output lands in branding/store/. Sizes come from the Chrome Web Store's
"Graphic assets" form; Firefox/AMO has no equivalent requirements.
"""

import pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "branding" / "store"

BG_TOP = (0, 18, 36)
BG_BOTTOM = (0, 30, 58)
GLOW = (0, 168, 232)
TEXT = (238, 248, 255)
SUBTEXT = (127, 182, 214)
TAGLINE = "Smart tab grouping. Total control."

FONT_CANDIDATES = [
    ("/System/Library/Fonts/SFNS.ttf", "Bold"),
    ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", None),
    ("/System/Library/Fonts/Helvetica.ttc", None),
]


def font(size, bold=True):
    for path, variation in FONT_CANDIDATES:
        if not pathlib.Path(path).exists():
            continue
        try:
            f = ImageFont.truetype(path, size)
        except OSError:
            continue
        if variation and bold:
            try:
                f.set_variation_by_name(variation)
            except (OSError, AttributeError):
                pass
        elif variation and not bold:
            try:
                f.set_variation_by_name("Regular")
            except (OSError, AttributeError):
                pass
        return f
    return ImageFont.load_default(size)


def gradient(size):
    """Vertical brand gradient with a soft glow centred low on the canvas."""
    w, h = size
    img = Image.new("RGB", size)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        draw.line(
            [(0, y), (w, y)],
            fill=tuple(round(a + (b - a) * t) for a, b in zip(BG_TOP, BG_BOTTOM)),
        )

    glow = Image.new("L", (w, h), 0)
    gd = ImageDraw.Draw(glow)
    rx, ry = w * 0.75, h * 0.85
    steps = 60
    for i in range(steps):
        t = i / steps
        gd.ellipse(
            [w / 2 - rx * (1 - t), h * 0.62 - ry * (1 - t),
             w / 2 + rx * (1 - t), h * 0.62 + ry * (1 - t)],
            fill=int(38 * t),
        )
    return Image.composite(Image.new("RGB", size, GLOW), img, glow)


def rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, img.size[0] - 1, img.size[1] - 1],
                                           radius=radius, fill=255)
    if img.mode == "RGBA":
        existing = img.getchannel("A")
        mask = Image.composite(mask, Image.new("L", img.size, 0), existing)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def fit(img, box, max_scale=2.0):
    w, h = img.size
    scale = min(max_scale, box[0] / w, box[1] / h)
    return img.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)


def centered(draw, text, y, f, fill):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=f)
    draw.text(((draw.im.size[0] - (right - left)) / 2 - left, y), text, font=f, fill=fill)
    return bottom - top


def save(img, name):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    img.convert("RGB").save(path, "PNG", optimize=True)
    print(f"  {path.relative_to(ROOT)}  {img.size[0]}x{img.size[1]}")


# --- store icon ---------------------------------------------------------------

def store_icons():
    src = Image.open(ROOT / "icons" / "icon-128.png").convert("RGBA")
    bbox = src.getchannel("A").getbbox()
    mark = src.crop(bbox)

    # Plain: the source mark, letterboxed as-is into the square.
    plain = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
    scaled = fit(mark, (112, 112), max_scale=1.0)
    plain.alpha_composite(scaled, ((128 - scaled.size[0]) // 2, (128 - scaled.size[1]) // 2))
    OUT.mkdir(parents=True, exist_ok=True)
    plain.save(OUT / "store-icon-128-plain.png", "PNG", optimize=True)
    print(f"  branding/store/store-icon-128-plain.png  128x128 (alpha)")

    # Tiled: the mark on a rounded brand tile, so it holds its own in the grid.
    tile = gradient((128, 128)).convert("RGBA")
    tile = rounded(tile, 28)
    scaled = fit(mark, (104, 104), max_scale=1.0)
    tile.alpha_composite(scaled, ((128 - scaled.size[0]) // 2, (128 - scaled.size[1]) // 2))
    tile.save(OUT / "store-icon-128.png", "PNG", optimize=True)
    print(f"  branding/store/store-icon-128.png  128x128 (alpha)")


# --- screenshots --------------------------------------------------------------

SHOTS = [
    ("tabbit-settings-configure", "Group by opening tab or domain",
     "Every tab from the same opener, or only when the domains match"),
    ("tabbit-settings-name", "Name groups your way",
     "Domain, subdomain, full hostname, page title, or nameless"),
    ("tabbit-custom-rules", "Custom rules per domain",
     "Set an alias and a color — ordered, first match wins"),
    ("tabbit-custom-rules-demo", "Rules in action",
     "Your names and colors, applied as tabs open"),
    ("tabbit-blacklist", "Blacklist the sites you want left alone",
     "Tabs opened from a blacklisted domain are never grouped"),
]


def hero():
    """The marketing image letterboxed to 8:5 — no cropping, nothing lost."""
    src = Image.open(ROOT / "branding" / "marketing-image.png").convert("RGB")
    canvas = gradient((1280, 800))
    scaled = fit(src, (1240, 760), max_scale=1.0)
    canvas.paste(scaled, ((1280 - scaled.size[0]) // 2, (800 - scaled.size[1]) // 2))
    save(canvas, "screenshot-1-overview.png")


def screenshot(index, stem, title, subtitle):
    src = Image.open(ROOT / "branding" / "screenshots" / f"{stem}.png").convert("RGBA")
    canvas = gradient((1280, 800))
    draw = ImageDraw.Draw(canvas)

    y = 96
    y += centered(draw, title, y, font(46, bold=True), TEXT) + 30
    centered(draw, subtitle, y, font(25, bold=False), SUBTEXT)

    shot = fit(src, (900, 470), max_scale=2.0)
    shot = rounded(shot, 12)
    x = (1280 - shot.size[0]) // 2
    top = 260 + (470 - shot.size[1]) // 2
    canvas.paste(shot, (x, top), shot)
    save(canvas, f"screenshot-{index}-{stem.replace('tabbit-', '')}.png")


# --- promo tiles --------------------------------------------------------------

def promo(size, name, wordmark_width, tagline_size, gap):
    wordmark = Image.open(ROOT / "branding" / "tabbit-name.png").convert("RGBA")
    canvas = gradient(size)
    scaled = fit(wordmark, (wordmark_width, size[1]), max_scale=1.0)

    f = font(tagline_size, bold=False)
    draw = ImageDraw.Draw(canvas)
    _, top, _, bottom = draw.textbbox((0, 0), TAGLINE, font=f)
    block = scaled.size[1] + gap + (bottom - top)
    y = (size[1] - block) // 2

    canvas.paste(scaled, ((size[0] - scaled.size[0]) // 2, y), scaled)
    centered(draw, TAGLINE, y + scaled.size[1] + gap, f, SUBTEXT)
    save(canvas, name)


if __name__ == "__main__":
    print("Chrome Web Store assets:")
    store_icons()
    hero()
    for i, (stem, title, subtitle) in enumerate(SHOTS, start=2):
        screenshot(i, stem, title, subtitle)
    promo((440, 280), "promo-small-440x280.png", 330, 17, 18)
    promo((1400, 560), "promo-marquee-1400x560.png", 780, 40, 40)
