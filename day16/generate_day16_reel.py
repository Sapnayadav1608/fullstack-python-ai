"""
Day 16: Personal Journey Daily Vlog Reel Generator (Unified Mathematical Grid Edition)
======================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 16/30: What I Learned & Built Today!" (Personal Learning Journey)
       Mastering Python Data Model & Magic (Dunder) Methods

Unified Mathematical Grid Architecture (100% Even Spacing):
  - Top Badge:           Y = 160 to 220 (Height: 60px, Radius: 18)
  - Hero Line 1:         Y = 265 (56px Bold White, anchor="mm")
  - Hero Line 2:         Y = 330 (56px Bold Gold, anchor="mm")
  - Subtitle:            Y = 390 (28px Italic Silver, anchor="mm")
  - Main Card:           Y = 450 to 1050 (Exact 600px Height, Left 60, Right 1020, Radius: 24)
  - Card Title:          Y = 495 (38px Bold Gold, anchor="mm")
  - Card Content:        Y = 535 to 1020 (Available 485px, Symmetrical 30px padding)
  - Bottom Callout Pill: Y = 1080 to 1160 (Exact 80px Height, Left 60, Right 1020, Radius: 22)
  - Animated Progress:   Y = 1200 to 1210 (Clean 10px Bar, Left 80, Right 1000)
  - Safe UI Zone:        Y = 1210 to 1920 (710px completely clear for Instagram/YouTube UI)
  - Pure Silent Video:   audio=False
"""

import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import VideoClip, concatenate_videoclips

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WIDTH, HEIGHT = 1080, 1920
FPS = 24
SCENE_DURATION = 8.0

# Calibrated Unified Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 56)
FONT_CARD_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 30)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 26)
FONT_DESC = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 23)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 25)
FONT_BIG_MATH = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 42)

# High-Contrast Luxury Palette
COLOR_BG_DARK = np.array([8, 8, 12], dtype=np.float32)      # Deep Obsidian
COLOR_CARD_BG = (22, 20, 30, 255)                          # High Contrast Glass Card
COLOR_INNER_BG = (14, 12, 18, 255)                         # Deep Pitch Box

COLOR_WHITE = (255, 255, 255)          # 100% Pure White
COLOR_LIGHT = (226, 232, 240)          # Light Platinum
COLOR_SILVER = (203, 213, 225)         # Bright Silver (#CBD5E1)
COLOR_GOLD = (255, 215, 0)             # Radiant Vivid Gold
COLOR_GREEN = (52, 211, 153)           # Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Vivid Electric Cyan
COLOR_BORDER = (80, 72, 100)           # High Visibility Crisp Border

# Standardized Global Geometry Constants
CARD_X0, CARD_X1 = 60, WIDTH - 60      # Left 60, Right 1020 (Width: 960px)
CARD_Y0, CARD_Y1 = 450, 1050           # Top 450, Bottom 1050 (Height: 600px)
INNER_X0, INNER_X1 = 90, WIDTH - 90    # Left 90, Right 990 (Width: 900px)


def create_base_canvas():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    canvas[:, :] = COLOR_BG_DARK
    return Image.fromarray(canvas)


def render_journey_canvas(t, scene_progress, step_badge="DAY 16 / 30  •  MY PYTHON + AI JOURNEY"):
    img = create_base_canvas()
    draw = ImageDraw.Draw(img, "RGBA")

    # 1. Top Eyebrow Badge (Y: 160 to 220)
    badge_w = 580
    bx0 = (WIDTH - badge_w) // 2
    draw.rounded_rectangle([bx0, 160, bx0 + badge_w, 220], radius=18, fill=(32, 28, 42), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 190), step_badge, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # 2. Main Card Shell (Y: 450 to 1050) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([CARD_X0, CARD_Y0, CARD_X1, CARD_Y1], radius=24, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)

    # 3. Bottom Callout Pill (Y: 1080 to 1160) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([CARD_X0, 1080, CARD_X1, 1160], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)

    # 4. Animated Progress Bar (Y: 1200 to 1210) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([80, 1200, WIDTH - 80, 1210], radius=5, fill=(40, 36, 52))
    fill_w = int((WIDTH - 160) * scene_progress)
    if fill_w > 0:
        draw.rounded_rectangle([80, 1200, 80 + fill_w, 1210], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 16 / 30  •  MY PYTHON + AI JOURNEY")

    # Header (Even vertical spacing: 265, 330, 390)
    draw.text((WIDTH // 2, 265), "Day 16 of 30 Days", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Python + AI Engineering!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Mastering Python's Special Dunder Methods", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's 4 Core Breakthroughs", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "String & Repr Protocols", "__repr__ vs __str__ & custom f-string formatting"),
        ("02", "Operator Overloading & @", "Vector algebra & PEP 465 matrix multiplication"),
        ("03", "The Sacred Hashing Invariant", "Why __eq__ breaks __hash__ & total ordering"),
        ("04", "PyTorch Datasets & Callables", "Sequence batch slicing & callable __call__ pipeline")
    ]

    # 4 Boxes: Height 100px each, gap 24px (540, 664, 788, 912) -> ends at 1012 (38px bottom gap!)
    py = 540
    for num, title, desc in modules:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        # Gold Tag
        draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 85, py + 84], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((INNER_X0 + 52, py + 50), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((INNER_X0 + 115, py + 20), title, font=FONT_HEADING, fill=COLOR_WHITE)
        draw.text((INNER_X0 + 115, py + 56), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 124

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "👉 Come along with me on Day 16!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - Vector Math & @ MatMul
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  WHAT I LEARNED FIRST")

    draw.text((WIDTH // 2, 265), "Step 1: Operator Overloading &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "The Matrix Multiplication @", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "I implemented vector algebra with PEP 465 dot product.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "My Code: Tensor1D Linear Algebra", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Code Inner Box: Y = 540 to 1020 (Exact 480px Height, Left 90, Right 990)
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)

    code_lines = [
        ("class Tensor1D:", COLOR_GOLD),
        ("    # 1. Vector addition (v1 + v2):", COLOR_LIGHT),
        ("    def __add__(self, other):", COLOR_WHITE),
        ("        data = [a + b for a, b in zip(self, other)]", COLOR_GREEN),
        ("        return Tensor1D(data)", COLOR_WHITE),
        ("    # 2. Dot Product via @ operator (PEP 465):", COLOR_LIGHT),
        ("    def __matmul__(self, other):", COLOR_GOLD),
        ("        return sum(a * b for a, b in zip(self, other))", COLOR_CYAN),
        ("# AI Cosine Similarity using @:", COLOR_LIGHT),
        ("sim = (v1 @ v2) / (abs(v1) * abs(v2))", COLOR_GOLD)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = 562
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((INNER_X0 + 25, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_SILVER)
        draw.line([INNER_X0 + 65, cur_y - 2, INNER_X0 + 65, cur_y + 28], fill=COLOR_BORDER, width=2)

        if acc + line_len <= shown_chars:
            draw.text((INNER_X0 + 85, cur_y), text, font=FONT_CODE, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 85, cur_y), text, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((INNER_X0 + 85, cur_y), part, font=FONT_CODE, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 85, cur_y), part, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((INNER_X0 + 85, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 44

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⚡ The @ operator powers PyTorch & modern AI tensors!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - The Sacred Hashing Invariant
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I MASTERED NEXT")

    draw.text((WIDTH // 2, 265), "Step 2: The Sacred Python", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Hashing Invariant Contract", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Why defining __eq__ immediately breaks __hash__.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "The Golden Law of Hashing", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Big Equation Box: Y = 540 to 630 (Height: 90px)
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 630], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=3)
    draw.text((WIDTH // 2, 585), "a == b   ⟹   hash(a) == hash(b)", font=FONT_BIG_MATH, fill=COLOR_GOLD, anchor="mm")

    cards = [
        ("The Rule", "Defining __eq__ sets __hash__ = None by default"),
        ("The Trap", "Mutable items in sets corrupt lookup buckets!"),
        ("The Fix", "Hash immutable tuples & use @total_ordering")
    ]

    # 3 Cards: Height 100px each, gap 30px (660, 790, 920) -> ends at 1020 (Exact 30px bottom gap!)
    py = 660
    for tag, desc in cards:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        # Tag
        draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 150, py + 84], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((INNER_X0 + 85, py + 50), tag, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((INNER_X0 + 175, py + 50), desc, font=FONT_BODY, fill=COLOR_WHITE, anchor="lm")
        py += 130

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🔒 Equal objects MUST always have equal hashes!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - PyTorch Datasets & Callables
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 265), "Step 3: PyTorch Datasets &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "The Callable Protocol (__call__)", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Turning class instances into stateful callable functions.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Sequence & Callable Architecture", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    protocols = [
        (
            "1. Sequence Protocol",
            "__len__ + __getitem__ with slice(start, stop)",
            "Enables batch slicing: dataset[1:10] returns mini-batch!"
        ),
        (
            "2. The Callable Protocol",
            "def __call__(self, *args, **kwargs)",
            "Powers PyTorch: calling model(inputs) runs forward pass!"
        ),
        (
            "3. Dynamic Attribute Proxy",
            "def __getattr__(self, name) -> fallback",
            "Safely routes missing dot-notation keys in AI configs."
        )
    ]

    # 3 Cards: Height 135px each, gap 20px (545, 700, 855) -> ends at 990 (60px bottom gap!)
    py = 545
    for title, sig, desc in protocols:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        draw.text((INNER_X0 + 30, py + 22), title, font=FONT_HEADING, fill=COLOR_GOLD)
        draw.text((INNER_X0 + 30, py + 62), sig, font=FONT_CODE, fill=COLOR_CYAN)
        draw.text((INNER_X0 + 30, py + 100), desc, font=FONT_DESC, fill=COLOR_WHITE)
        py += 155

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🧠 Calling model(x) triggers __call__ under the hood!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): DAY 16 COMPLETE & CTA (SPACIOUS & ELEGANT)
# =========================================================================
TASKS_DONE = [
    ("4 Deep Python Modules Mastered", "Dunders, operator overloading, @ matmul & protocols"),
    ("6/6 Practice Tasks Solved", "All automated tests passed in my practice workbook"),
    ("53% Challenge Milestone Unlocked", "16 days down, 14 more exciting days to go!")
]


def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 16 COMPLETE  •  MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 265), "Day 16 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "53% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Here is everything I accomplished today:", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's Achievements & Progress", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # 3 Spacious Boxes: Height 95px each, gap 20px (540, 655, 770)
    py = 540
    for idx, (title, desc) in enumerate(TASKS_DONE):
        reveal_time = idx * 1.5
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 95], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
            # Gold Checkmark Badge
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
            draw.text((INNER_X0 + 48, py + 48), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 95, py + 22), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((INNER_X0 + 95, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        else:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 95], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(28, 24, 36), outline=COLOR_BORDER, width=1)
            draw.text((INNER_X0 + 48, py + 48), "○", font=FONT_HEADING, fill=COLOR_SILVER, anchor="mm")
            draw.text((INNER_X0 + 95, py + 22), title, font=FONT_HEADING, fill=COLOR_SILVER)
            draw.text((INNER_X0 + 95, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 115

    # Milestone Box: Y = 890 to 1010 (Height: 120px, Symmetrical 40px gaps!)
    pct = int(min(53, 50 + (t / 5.5) * 3))
    draw.rounded_rectangle([INNER_X0, 890, INNER_X1, 1010], radius=18, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 930), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 975), "Follow along my 30-Day Python + AI Journey! Day 17 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER (PURE SILENT VIDEO — audio=False)
# =========================================================================
def main():
    out_dir = "D:/learn-python/day16"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Unified Grid Silent Day 16 Vlog Reel...")
    print("=" * 65)

    print("📸 Exporting 5 High-Resolution Preview Frames...")
    previews = [
        ("scene_1.png", make_frame_scene_1(4.5)),
        ("scene_2.png", make_frame_scene_2(4.5)),
        ("scene_3.png", make_frame_scene_3(5.5)),
        ("scene_4.png", make_frame_scene_4(4.5)),
        ("scene_5.png", make_frame_scene_5(5.5)),
    ]
    for filename, frame_arr in previews:
        preview_path = os.path.join(preview_dir, filename)
        Image.fromarray(frame_arr).save(preview_path)
        print(f"  ✓ Saved: {preview_path}")

    clip1 = VideoClip(make_frame_scene_1, duration=SCENE_DURATION)
    clip2 = VideoClip(make_frame_scene_2, duration=SCENE_DURATION)
    clip3 = VideoClip(make_frame_scene_3, duration=SCENE_DURATION)
    clip4 = VideoClip(make_frame_scene_4, duration=SCENE_DURATION)
    clip5 = VideoClip(make_frame_scene_5, duration=SCENE_DURATION)

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])
    video_output_path = os.path.join(out_dir, "day16_reel_video.mp4")
    print(f"\n🎥 Encoding Unified Grid MP4 Video: {video_output_path}")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    print("\n" + "=" * 65)
    print(f"✅ Video Generated Successfully: {video_output_path}")
    print(f"✅ Total Duration: {final_video.duration:.1f}s | FPS: {FPS}")
    print("=" * 65)


if __name__ == "__main__":
    main()
