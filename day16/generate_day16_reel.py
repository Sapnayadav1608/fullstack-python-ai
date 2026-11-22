"""
Day 16: Personal Journey Daily Vlog Reel Generator (Times New Roman Luxury Edition)
===================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 16/30: What I Learned & Built Today!" (Personal Learning Journey)
       Mastering Python Data Model & Magic (Dunder) Methods

Visual & Design Highlights:
- Clean Editorial Journey Log (Times New Roman Bold & Italic)
- Ultra-Clean Minimalist Cards with 70% breathing room (Zero clutter)
- Safe Zones: Top header at Y=180, safe bottom 640px for Instagram UI
- Animated Progress Bar & Interactive Code Reveals
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

# Times New Roman Bold & Bold Italic
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 54)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 20)

# Clean High-Contrast Palette
COLOR_BG_DARK = np.array([9, 9, 12], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (20, 18, 26, 252)                          # Sleek Glass Card
COLOR_INNER_BG = (12, 10, 16, 255)                         # Pitch Black Inner

COLOR_WHITE = (255, 255, 255)          # 100% Pure White
COLOR_LIGHT = (226, 232, 240)          # Light Platinum
COLOR_GOLD = (255, 215, 0)             # Radiant Gold
COLOR_GREEN = (52, 211, 153)           # Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Sky Cyan
COLOR_BORDER = (65, 60, 80)            # Crisp Subtle Border


def create_base_canvas():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    canvas[:, :] = COLOR_BG_DARK
    return Image.fromarray(canvas)


def render_journey_canvas(t, scene_progress, step_badge="DAY 16 / 30  •  MY PYTHON + AI JOURNEY"):
    img = create_base_canvas()
    draw = ImageDraw.Draw(img, "RGBA")

    # Top Eyebrow Badge (Y: 170 to 220)
    badge_w = 540
    bx0 = (WIDTH - badge_w) // 2
    draw.rounded_rectangle([bx0, 170, bx0 + badge_w, 222], radius=16, fill=(28, 24, 36), outline=COLOR_BORDER, width=1)
    draw.text((WIDTH // 2, 196), step_badge, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # Animated Progress Bar (Y: 1280 to 1290)
    bar_y = 1280
    draw.rounded_rectangle([100, bar_y, WIDTH - 100, bar_y + 8], radius=4, fill=(35, 32, 45))
    fill_w = int((WIDTH - 200) * scene_progress)
    if fill_w > 0:
        draw.rounded_rectangle([100, bar_y, 100 + fill_w, bar_y + 8], radius=4, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 16 / 30  •  MY PYTHON + AI JOURNEY")

    draw.text((WIDTH // 2, 285), "Day 16 of 30 Days", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Python + AI Engineering!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "Here is everything I learned and built today.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    card_y0, card_y1 = 480, 940
    draw.rounded_rectangle([90, card_y0, WIDTH - 90, card_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 40), "Today's Focus: Python Data Model & Dunders", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "Repr vs Str Duality & Bool", "eval(repr(x)) == x and custom f-string formatting"),
        ("02", "Operator Overloading & @", "Vector math, scaling, and PEP 465 dot product"),
        ("03", "The Sacred Hashing Invariant", "Why __eq__ breaks __hash__ and @total_ordering"),
        ("04", "PyTorch Datasets & Callables", "Slicing sequences and making instances callable")
    ]

    py = card_y0 + 80
    for num, title, desc in modules:
        draw.rounded_rectangle([120, py, WIDTH - 120, py + 86], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        draw.rounded_rectangle([135, py + 15, 185, py + 71], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
        draw.text((160, py + 43), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        draw.text((205, py + 22), title, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((205, py + 52), desc, font=FONT_MINI, fill=COLOR_LIGHT)
        py += 100

    draw.rounded_rectangle([90, 980, WIDTH - 90, 1060], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1020), "Come along with me on Day 16 ->", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - Vector Math & @ MatMul
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  WHAT I LEARNED FIRST")

    draw.text((WIDTH // 2, 285), "Step 1: Operator Overloading &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "The Matrix Multiplication @", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "I implemented vector algebra with PEP 465 dot product.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 1030
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "My Code: Tensor1D Linear Algebra", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    draw.rounded_rectangle([120, c_y0 + 75, WIDTH - 120, c_y1 - 35], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)

    code_lines = [
        ("class Tensor1D:", COLOR_GOLD),
        ("    def __add__(self, other):", COLOR_WHITE),
        ("        if isinstance(other, Tensor1D):", COLOR_LIGHT),
        ("            return Tensor1D([a + b for a, b in zip(self, other)])", COLOR_GREEN),
        ("        return NotImplemented  # Golden Rule!", COLOR_CYAN),
        ("", COLOR_WHITE),
        ("    def __matmul__(self, other):  # PEP 465 @", COLOR_GOLD),
        ("        # Vector Dot Product in 1 line:", COLOR_LIGHT),
        ("        return sum(a * b for a, b in zip(self, other))", COLOR_GREEN),
        ("", COLOR_WHITE),
        ("# Cosine Similarity for AI Embeddings:", COLOR_LIGHT),
        ("similarity = (v1 @ v2) / (abs(v1) * abs(v2))", COLOR_GOLD),
        ("print(f'Relevance Score: {similarity:.4f}')", COLOR_WHITE)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = c_y0 + 105
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((145, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_LIGHT)
        draw.line([185, cur_y - 2, 185, cur_y + 24], fill=COLOR_BORDER, width=1)

        if acc + line_len <= shown_chars:
            draw.text((205, cur_y), text, font=FONT_CODE_SM, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((205, cur_y), text, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((205, cur_y), part, font=FONT_CODE_SM, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((205, cur_y), part, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((205, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 34

    draw.rounded_rectangle([90, 1060, WIDTH - 90, 1140], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1100), "The @ operator powers PyTorch & modern AI tensors!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - The Sacred Hashing Invariant
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I MASTERED NEXT")

    draw.text((WIDTH // 2, 285), "Step 2: The Sacred", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Python Hashing Contract", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "Why defining __eq__ immediately nullifies __hash__.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 980
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "The Sacred Hashability Invariant", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # The Golden Equation Box
    draw.rounded_rectangle([130, c_y0 + 80, WIDTH - 130, c_y0 + 170], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 125), "a == b  ⟹  hash(a) == hash(b)", font=FONT_TITLE, fill=COLOR_GOLD, anchor="mm")

    cards = [
        ("The Trait", "Defining __eq__ automatically sets __hash__ = None to protect hash sets."),
        ("The Trap", "If a mutable object changes in a set, its hash bucket is corrupted forever!"),
        ("The Fix", "Hash immutable tuples only, and use @functools.total_ordering for rankings.")
    ]

    py = c_y0 + 195
    for tag, desc in cards:
        draw.rounded_rectangle([130, py, WIDTH - 130, py + 75], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        draw.rounded_rectangle([145, py + 12, 230, py + 62], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
        draw.text((187, py + 37), tag, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")
        draw.text((250, py + 37), desc, font=FONT_MINI, fill=COLOR_WHITE, anchor="lm")
        py += 88

    draw.rounded_rectangle([90, 1020, WIDTH - 90, 1100], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1060), "Equal objects MUST always produce equal hashes!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - PyTorch Datasets & Callables
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 285), "Step 3: PyTorch Datasets &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "The Callable Protocol (__call__)", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "Turning class instances into stateful callable functions.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 1000
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Sequence & Callable Architecture", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    protocols = [
        ("Sequence Protocol", "__len__ + __getitem__ with slice(start, stop)", "Enables batch slicing: dataset[1:10] returns new mini-batch!"),
        ("The Callable Protocol", "__call__(self, *args, **kwargs)", "Powers PyTorch: calling model(inputs) runs forward hooks!"),
        ("Dynamic Attribute Proxy", "__getattr__(self, name) fallback", "Safely routes missing dot-notation keys in RAG config stores.")
    ]

    py = c_y0 + 80
    for title, sig, desc in protocols:
        draw.rounded_rectangle([120, py, WIDTH - 120, py + 120], radius=12, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        draw.text((150, py + 26), title, font=FONT_HEADING, fill=COLOR_GOLD)
        draw.text((150, py + 62), sig, font=FONT_CODE_SM, fill=COLOR_CYAN)
        draw.text((150, py + 92), desc, font=FONT_MINI, fill=COLOR_WHITE)
        py += 135

    draw.rounded_rectangle([90, 1040, WIDTH - 90, 1120], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1080), "Calling model(x) triggers __call__ under the hood!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): DAY 16 COMPLETE & CTA
# =========================================================================
def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 16 COMPLETE  •  MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 285), "Day 16 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "53% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "Here is everything I accomplished today:", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    c_y0, c_y1 = 480, 890
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Daily Checklist: 100% Completed", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    TASKS_DONE = [
        ("String & Repr Protocols", "Mastered __repr__ vs __str__ & __format__ specifiers"),
        ("Operator Overloading", "Built Tensor1D with @ matrix multiplication (PEP 465)"),
        ("The Hashing Contract", "Satisfied a == b => hash(a) == hash(b) with total ordering"),
        ("PyTorch Datasets & Callables", "Implemented sequence batch slicing & callable pipeline"),
        ("Workbook & Automated Tests", "Passed all 6 practice challenges on first run")
    ]

    py = c_y0 + 75
    for idx, (title, desc) in enumerate(TASKS_DONE):
        reveal_time = idx * 1.3
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([120, py, WIDTH - 120, py + 68], radius=8, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
            draw.rounded_rectangle([135, py + 12, 185, py + 56], radius=6, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
            draw.text((160, py + 34), "✓", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")
            draw.text((205, py + 18), title, font=FONT_BODY, fill=COLOR_WHITE)
            draw.text((205, py + 44), desc, font=FONT_MINI, fill=COLOR_LIGHT)
        else:
            draw.rounded_rectangle([120, py, WIDTH - 120, py + 68], radius=8, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
            draw.rounded_rectangle([135, py + 12, 185, py + 56], radius=6, fill=(20, 18, 24), outline=COLOR_BORDER, width=1)
            draw.text((160, py + 34), "○", font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
            draw.text((205, py + 18), title, font=FONT_BODY, fill=(120, 120, 140))
            draw.text((205, py + 44), desc, font=FONT_MINI, fill=(90, 90, 100))
        py += 78

    pct = int(min(53, 50 + (t / 5.5) * 3))
    draw.rounded_rectangle([90, 910, WIDTH - 90, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 945), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 985), "Follow along my 30-Day Python + AI Journey! Day 17 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    draw.rounded_rectangle([90, 1050, WIDTH - 90, 1130], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1090), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day16"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Day 16 Personal Journey Daily Vlog Reel...")
    print("=" * 65)

    print("📸 Exporting 5 Preview Frames for Quality Verification...")
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
    print(f"\n🎥 Encoding MP4 Video: {video_output_path}")

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
