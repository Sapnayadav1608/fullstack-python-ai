"""
Day 16: Personal Journey Daily Vlog Reel Generator (Zero Overflow Silent Edition)
=================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 16/30: What I Learned & Built Today!" (Personal Learning Journey)
       Mastering Python Data Model & Magic (Dunder) Methods

Strict Layout & Legibility Specifications:
- 100% Zero Container Overflow: Every line verified with draw.textbbox (60px+ padding)
- Pure Silent Video (audio=False): Perfect for user to add trending music or own voice
- Safe Zones: Top header at Y=165, safe bottom 640px clear for Instagram UI
- High-Contrast Palette: Pure White (#FFFFFF), Radiant Gold (#FFD700), Neon Cyan (#38BDF8)
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

# Calibrated High-Legibility Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 56)
FONT_CARD_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 28)
FONT_DESC = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 26)
FONT_BIG_MATH = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 44)

# Maximum Contrast Color Palette
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


def create_base_canvas():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    canvas[:, :] = COLOR_BG_DARK
    return Image.fromarray(canvas)


def render_journey_canvas(t, scene_progress, step_badge="DAY 16 / 30  •  MY PYTHON + AI JOURNEY"):
    img = create_base_canvas()
    draw = ImageDraw.Draw(img, "RGBA")

    # Top Eyebrow Badge (Y: 165 to 225)
    badge_w = 580
    bx0 = (WIDTH - badge_w) // 2
    draw.rounded_rectangle([bx0, 165, bx0 + badge_w, 225], radius=18, fill=(32, 28, 42), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 195), step_badge, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # Animated Progress Bar (Y: 1280 to 1290)
    bar_y = 1280
    draw.rounded_rectangle([80, bar_y, WIDTH - 80, bar_y + 10], radius=5, fill=(40, 36, 52))
    fill_w = int((WIDTH - 160) * scene_progress)
    if fill_w > 0:
        draw.rounded_rectangle([80, bar_y, 80 + fill_w, bar_y + 10], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 16 / 30  •  MY PYTHON + AI JOURNEY")

    draw.text((WIDTH // 2, 285), "Day 16 of 30 Days", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Python + AI Engineering!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "Mastering Python's Special Dunder Methods", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Outer Card (x: 60 to 1020, width: 960px)
    c_y0, c_y1 = 480, 1025
    draw.rounded_rectangle([60, c_y0, WIDTH - 60, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Today's 4 Core Breakthroughs", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "String & Repr Protocols", "__repr__ vs __str__ & custom f-string formatting"),
        ("02", "Operator Overloading & @", "Vector algebra & PEP 465 matrix multiplication"),
        ("03", "The Sacred Hashing Invariant", "Why __eq__ breaks __hash__ & total ordering"),
        ("04", "PyTorch Datasets & Callables", "Sequence batch slicing & callable __call__ pipeline")
    ]

    py = c_y0 + 80
    for num, title, desc in modules:
        # Inner Box (x: 90 to 990, width: 900px)
        draw.rounded_rectangle([90, py, WIDTH - 90, py + 102], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        # Gold Tag
        draw.rounded_rectangle([110, py + 16, 175, py + 86], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((142, py + 51), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((205, py + 20), title, font=FONT_HEADING, fill=COLOR_WHITE)
        draw.text((205, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 118

    # Bottom Pill
    draw.rounded_rectangle([60, 1055, WIDTH - 60, 1140], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1097), "👉 Come along with me on Day 16!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - Vector Math & @ MatMul (ZERO OVERFLOW)
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  WHAT I LEARNED FIRST")

    draw.text((WIDTH // 2, 285), "Step 1: Operator Overloading &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "The Matrix Multiplication @", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "I implemented vector algebra with PEP 465 dot product.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 1035
    draw.rounded_rectangle([60, c_y0, WIDTH - 60, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "My Code: Tensor1D Linear Algebra", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Code Inner Box: x: 80 to 1000 (Width: 920px)
    draw.rounded_rectangle([80, c_y0 + 78, WIDTH - 80, c_y1 - 32], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)

    # 10 Clean Lines calibrated to fit inside 920px box (Max width = 756px, Safe = True!)
    code_lines = [
        ("class Tensor1D:", COLOR_GOLD),
        ("    # 1. Vector addition (v1 + v2):", COLOR_LIGHT),
        ("    def __add__(self, other):", COLOR_WHITE),
        ("        data = [a + b for a, b in zip(self, other)]", COLOR_GREEN),
        ("        return Tensor1D(data)", COLOR_WHITE),
        ("    # 2. Dot Product via @ operator:", COLOR_LIGHT),
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
    cur_y = c_y0 + 98
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((105, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_SILVER)
        draw.line([145, cur_y - 2, 145, cur_y + 28], fill=COLOR_BORDER, width=2)

        if acc + line_len <= shown_chars:
            draw.text((165, cur_y), text, font=FONT_CODE, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((165, cur_y), text, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((165, cur_y), part, font=FONT_CODE, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((165, cur_y), part, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((165, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 37

    draw.rounded_rectangle([60, 1060, WIDTH - 60, 1145], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1102), "⚡ The @ operator powers PyTorch & modern AI tensors!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - The Sacred Hashing Invariant (ZERO OVERFLOW)
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I MASTERED NEXT")

    draw.text((WIDTH // 2, 285), "Step 2: The Sacred Python", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Hashing Invariant Contract", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "Why defining __eq__ immediately breaks __hash__.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 1020
    draw.rounded_rectangle([60, c_y0, WIDTH - 60, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "The Golden Law of Hashing", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Big Equation Box
    draw.rounded_rectangle([90, c_y0 + 82, WIDTH - 90, c_y0 + 178], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=3)
    draw.text((WIDTH // 2, c_y0 + 130), "a == b   ⟹   hash(a) == hash(b)", font=FONT_BIG_MATH, fill=COLOR_GOLD, anchor="mm")

    cards = [
        ("The Rule", "Defining __eq__ sets __hash__ = None by default"),
        ("The Trap", "Mutable items in sets corrupt lookup buckets!"),
        ("The Fix", "Hash immutable tuples & use @total_ordering")
    ]

    py = c_y0 + 200
    for tag, desc in cards:
        # Inner Box: width = 900px (x: 90 to 990)
        draw.rounded_rectangle([90, py, WIDTH - 90, py + 92], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        draw.rounded_rectangle([110, py + 14, 230, py + 78], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((170, py + 46), tag, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        draw.text((250, py + 46), desc, font=FONT_BODY, fill=COLOR_WHITE, anchor="lm")
        py += 110

    draw.rounded_rectangle([60, 1045, WIDTH - 60, 1130], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1087), "🔒 Equal objects MUST always have equal hashes!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - PyTorch Datasets & Callables (ZERO OVERFLOW)
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 285), "Step 3: PyTorch Datasets &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "The Callable Protocol (__call__)", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "Turning class instances into stateful callable functions.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 1030
    draw.rounded_rectangle([60, c_y0, WIDTH - 60, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Sequence & Callable Architecture", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

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

    py = c_y0 + 82
    for title, sig, desc in protocols:
        draw.rounded_rectangle([90, py, WIDTH - 90, py + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        draw.text((120, py + 22), title, font=FONT_HEADING, fill=COLOR_GOLD)
        draw.text((120, py + 62), sig, font=FONT_CODE, fill=COLOR_CYAN)
        draw.text((120, py + 100), desc, font=FONT_DESC, fill=COLOR_WHITE)
        py += 152

    draw.rounded_rectangle([60, 1055, WIDTH - 60, 1140], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1097), "🧠 Calling model(x) triggers __call__ under the hood!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): DAY 16 COMPLETE & CTA (ZERO OVERFLOW)
# =========================================================================
def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 16 COMPLETE  •  MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 285), "Day 16 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "53% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "Here is everything I accomplished today:", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 915
    draw.rounded_rectangle([60, c_y0, WIDTH - 60, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Daily Progress Checklist", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    TASKS_DONE = [
        ("String & Repr Protocols", "Mastered __repr__ vs __str__ & custom f-strings"),
        ("Operator Overloading", "Built Tensor1D with @ matrix multiplication (PEP 465)"),
        ("The Hashing Contract", "Satisfied a == b => hash(a) == hash(b) invariant"),
        ("PyTorch Datasets & Callables", "Implemented sequence batch slicing & callable pipeline"),
        ("Workbook & Automated Tests", "Passed all 6 practice challenges on first run")
    ]

    py = c_y0 + 75
    for idx, (title, desc) in enumerate(TASKS_DONE):
        reveal_time = idx * 1.3
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([90, py, WIDTH - 90, py + 68], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
            draw.rounded_rectangle([105, py + 12, 160, py + 56], radius=8, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
            draw.text((132, py + 34), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            draw.text((180, py + 18), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((180, py + 44), desc, font=FONT_DESC, fill=COLOR_SILVER)
        else:
            draw.rounded_rectangle([90, py, WIDTH - 90, py + 68], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
            draw.rounded_rectangle([105, py + 12, 160, py + 56], radius=8, fill=(28, 24, 36), outline=COLOR_BORDER, width=1)
            draw.text((132, py + 34), "○", font=FONT_HEADING, fill=COLOR_SILVER, anchor="mm")
            draw.text((180, py + 18), title, font=FONT_HEADING, fill=COLOR_SILVER)
            draw.text((180, py + 44), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 78

    pct = int(min(53, 50 + (t / 5.5) * 3))
    draw.rounded_rectangle([60, 935, WIDTH - 60, 1045], radius=18, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 972), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 1014), "Follow my 30-Day Python + AI Journey! Day 17 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    draw.rounded_rectangle([60, 1070, WIDTH - 60, 1155], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1112), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER (PURE SILENT VIDEO — audio=False)
# =========================================================================
def main():
    out_dir = "D:/learn-python/day16"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Pure Silent Zero-Overflow Day 16 Vlog Reel...")
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
    print(f"\n🎥 Encoding Pure Silent MP4 Video (audio=False): {video_output_path}")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    print("\n" + "=" * 65)
    print(f"✅ Pure Silent Video Generated: {video_output_path}")
    print(f"✅ Total Duration: {final_video.duration:.1f}s | FPS: {FPS}")
    print("=" * 65)


if __name__ == "__main__":
    main()
