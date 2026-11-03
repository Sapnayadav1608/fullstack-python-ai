"""
Day 08: Automated Instagram Reel Video Generator
=================================================
Generates a modern, aesthetic 1080x1920 (9:16) vertical MP4 reel video
covering Day 8: Python Tuples Deep Dive, Benchmarks & GitHub Update.
Duration: 28 seconds (matches the voiceover timing).
"""

import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, concatenate_videoclips

# Configure UTF-8 for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WIDTH, HEIGHT = 1080, 1920
FPS = 24

# Fonts
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 64)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 46)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 36)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 34)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)

# Color Palette (Modern Dark Theme - Developer Aesthetic)
BG_COLOR = (13, 17, 23)        # GitHub Dark
CARD_BG = (22, 27, 34)         # Card Dark
CARD_BORDER = (48, 54, 61)     # Border Grey
ACCENT_CYAN = (88, 166, 255)   # Tech Blue
ACCENT_GREEN = (63, 185, 80)   # Python/Success Green
ACCENT_PURPLE = (187, 128, 247) # AI Purple
TEXT_WHITE = (240, 246, 252)   # Bright White
TEXT_MUTED = (139, 148, 158)   # Muted Grey


def draw_base_canvas(progress_ratio: float, day_text: str = "DAY 08 / 30"):
    """Draws background, top header badge, and bottom progress bar."""
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Top Header Badge
    badge_w, badge_h = 440, 60
    badge_x = (WIDTH - badge_w) // 2
    badge_y = 120
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=30, fill=CARD_BG, outline=CARD_BORDER, width=2)
    draw.text((WIDTH // 2, badge_y + badge_h // 2), day_text, font=FONT_BADGE, fill=ACCENT_CYAN, anchor="mm")

    # Author Subtitle
    draw.text((WIDTH // 2, 210), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

    # Bottom Progress Bar
    bar_y = HEIGHT - 80
    bar_margin = 80
    bar_w = WIDTH - (2 * bar_margin)
    draw.rounded_rectangle([bar_margin, bar_y, bar_margin + bar_w, bar_y + 12], radius=6, fill=CARD_BG)
    fill_w = int(bar_w * progress_ratio)
    if fill_w > 0:
        draw.rounded_rectangle([bar_margin, bar_y, bar_margin + fill_w, bar_y + 12], radius=6, fill=ACCENT_CYAN)

    return img, draw


def create_scene_1():
    """Scene 1 (0-6s): Hook & Week 2 Introduction"""
    img, draw = draw_base_canvas(0.2, "DAY 08 / 30  •  WEEK 2 KICK-OFF")

    # Big Title
    draw.text((WIDTH // 2, 360), "Python Tuples", font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 440), "Deep Dive & Memory Internals", font=FONT_HEADING, fill=ACCENT_PURPLE, anchor="mm")

    # Code Card
    card_x0, card_y0 = 80, 560
    card_x1, card_y1 = WIDTH - 80, 1140
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)

    # Card Window Dots (Mac style)
    draw.ellipse([card_x0 + 30, card_y0 + 30, card_x0 + 50, card_y0 + 50], fill=(255, 95, 86))
    draw.ellipse([card_x0 + 65, card_y0 + 30, card_x0 + 85, card_y0 + 50], fill=(255, 189, 46))
    draw.ellipse([card_x0 + 100, card_y0 + 30, card_x0 + 120, card_y0 + 50], fill=(39, 201, 63))
    draw.text((card_x0 + 150, card_y0 + 40), "01_tuple_fundamentals.py", font=FONT_BADGE, fill=TEXT_MUTED, anchor="lm")

    # Code Content
    code_lines = [
        ("# 1. Comma defines the tuple, not parentheses!", ACCENT_GREEN),
        ("single = (42,)   # <class 'tuple'>", TEXT_WHITE),
        ("not_tup = (42)   # <class 'int'>", TEXT_MUTED),
        ("", TEXT_WHITE),
        ("# 2. Advanced Star (*) Unpacking", ACCENT_GREEN),
        ("stream = (10, 20, 30, 40, 50)", TEXT_WHITE),
        ("first, *middle, last = stream", ACCENT_CYAN),
        ("print(middle)    # [20, 30, 40]", TEXT_WHITE),
        ("", TEXT_WHITE),
        ("# 3. PyTorch Tensor Dimensions", ACCENT_GREEN),
        ("shape = (32, 3, 224, 224)", ACCENT_PURPLE),
    ]

    y_offset = card_y0 + 100
    for text, color in code_lines:
        draw.text((card_x0 + 40, y_offset), text, font=FONT_CODE, fill=color)
        y_offset += 46

    # Bottom Pill
    pill_w, pill_h = 560, 70
    px = (WIDTH - pill_w) // 2
    py = 1300
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=35, fill=CARD_BG, outline=ACCENT_CYAN, width=2)
    draw.text((WIDTH // 2, py + pill_h // 2), "Immutable  •  Memory Safe  •  Fast", font=FONT_SUB, fill=ACCENT_CYAN, anchor="mm")

    return img


def create_scene_2():
    """Scene 2 (6-13s): The Big Question & Live Benchmark"""
    img, draw = draw_base_canvas(0.45, "THE BIG QUESTION")

    draw.text((WIDTH // 2, 350), "Why Tuples When", font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 430), "Lists Already Exist?", font=FONT_TITLE, fill=ACCENT_CYAN, anchor="mm")

    # Benchmark Results Card
    card_x0, card_y0 = 80, 540
    card_x1, card_y1 = WIDTH - 80, 1360
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)

    draw.text((WIDTH // 2, card_y0 + 60), "LIVE BENCHMARK RESULTS", font=FONT_HEADING, fill=ACCENT_PURPLE, anchor="mm")
    draw.text((WIDTH // 2, card_y0 + 120), "Creating 10,000,000 Elements in CPython", font=FONT_SUB, fill=TEXT_MUTED, anchor="mm")

    # List Box
    box_w = (card_x1 - card_x0 - 80) // 2
    b1_x0 = card_x0 + 30
    b1_x1 = b1_x0 + box_w
    draw.rounded_rectangle([b1_x0, card_y0 + 180, b1_x1, card_y0 + 450], radius=16, fill=BG_COLOR, outline=CARD_BORDER)
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 220), "PYTHON LIST", font=FONT_SUB, fill=TEXT_MUTED, anchor="mm")
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 300), "1.088s", font=FONT_TITLE, fill=(255, 120, 117), anchor="mm")
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 380), "Over-allocated RAM", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

    # Tuple Box
    b2_x0 = b1_x1 + 20
    b2_x1 = b2_x0 + box_w
    draw.rounded_rectangle([b2_x0, card_y0 + 180, b2_x1, card_y0 + 450], radius=16, fill=BG_COLOR, outline=ACCENT_GREEN, width=2)
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 220), "PYTHON TUPLE", font=FONT_SUB, fill=ACCENT_GREEN, anchor="mm")
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 300), "0.590s", font=FONT_TITLE, fill=ACCENT_GREEN, anchor="mm")
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 380), "Exact Memory Size", font=FONT_BADGE, fill=TEXT_MUTED, anchor="mm")

    # Speed Highlight Banner
    hl_y = card_y0 + 490
    draw.rounded_rectangle([card_x0 + 30, hl_y, card_x1 - 30, hl_y + 110], radius=16, fill=(35, 134, 54, 60), outline=ACCENT_GREEN, width=2)
    draw.text((WIDTH // 2, hl_y + 55), "⚡ 1.84x FASTER CREATION SPEED", font=FONT_HEADING, fill=TEXT_WHITE, anchor="mm")

    # Bullet Points below
    bullets = [
        "• Constant Folding & Free-List caching in CPython",
        "• Zero dynamic reallocation overhead",
        "• Hashable: Allowed as Dictionary Keys & Sets"
    ]
    by = card_y0 + 640
    for b in bullets:
        draw.text((card_x0 + 40, by), b, font=FONT_SUB, fill=TEXT_WHITE)
        by += 55

    return img


def create_scene_3():
    """Scene 3 (13-21s): Key Concepts Mastered"""
    img, draw = draw_base_canvas(0.75, "TOPICS CONQUERED")

    draw.text((WIDTH // 2, 350), "Key Concepts", font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 430), "Mastered on Day 08", font=FONT_HEADING, fill=ACCENT_PURPLE, anchor="mm")

    cards = [
        ("01", "The Single-Element Comma Rule", "(42,) is a tuple, but (42) is an int!"),
        ("02", "Star (*) Extended Unpacking", "first, *middle, last = numbers"),
        ("03", "Tuples as Dictionary Keys", "Valid keys because tuples are hashable"),
        ("04", "Mutable Object in Tuple Trap", "t = (1, [2, 3]) reference vs state"),
        ("05", "AI Tensor Dimensions", "PyTorch & NumPy immutable shapes")
    ]

    cy = 540
    for num, title, desc in cards:
        draw.rounded_rectangle([80, cy, WIDTH - 80, cy + 125], radius=16, fill=CARD_BG, outline=CARD_BORDER, width=2)
        # Number badge
        draw.rounded_rectangle([105, cy + 25, 175, cy + 95], radius=12, fill=BG_COLOR, outline=ACCENT_CYAN)
        draw.text((140, cy + 60), num, font=FONT_HEADING, fill=ACCENT_CYAN, anchor="mm")

        # Texts
        draw.text((205, cy + 40), title, font=FONT_SUB, fill=TEXT_WHITE, anchor="lm")
        draw.text((205, cy + 85), desc, font=FONT_BADGE, fill=TEXT_MUTED, anchor="lm")
        cy += 145

    return img


def create_scene_4():
    """Scene 4 (21-28s): GitHub Update & Outro CTA"""
    img, draw = draw_base_canvas(1.0, "DAY 08 COMPLETE")

    draw.text((WIDTH // 2, 350), "Code & Workbook", font=FONT_TITLE, fill=TEXT_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 430), "Live on GitHub!", font=FONT_HEADING, fill=ACCENT_GREEN, anchor="mm")

    # GitHub Box
    card_x0, card_y0 = 80, 540
    card_x1, card_y1 = WIDTH - 80, 1260
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=24, fill=CARD_BG, outline=CARD_BORDER, width=2)

    draw.text((WIDTH // 2, card_y0 + 80), "github.com/Sapnayadav1608", font=FONT_HEADING, fill=ACCENT_CYAN, anchor="mm")
    draw.text((WIDTH // 2, card_y0 + 140), "fullstack-python-ai / day8", font=FONT_SUB, fill=TEXT_MUTED, anchor="mm")

    # File checklist
    files = [
        "01_tuple_fundamentals_and_creation.py",
        "02_tuples_vs_lists_memory_and_speed.py",
        "03_tuple_operations_and_unpacking.py",
        "04_tuple_interview_questions.py",
        "my_practice.py (6 Hands-On Tasks)",
        "README.md (Notes & Cheat-Sheet)"
    ]

    fy = card_y0 + 220
    for f in files:
        draw.text((card_x0 + 50, fy), f"[OK]  {f}", font=FONT_CODE, fill=TEXT_WHITE)
        fy += 65

    # Outro Call to Action
    draw.rounded_rectangle([100, 1340, WIDTH - 100, 1460], radius=24, fill=BG_COLOR, outline=ACCENT_PURPLE, width=2)
    draw.text((WIDTH // 2, 1385), "Follow along for Day 09!", font=FONT_HEADING, fill=TEXT_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 1430), "Drop your questions in the comments below 👇", font=FONT_BADGE, fill=ACCENT_CYAN, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day8/day8_reel_video.mp4"
    temp_dir = "D:/learn-python/day8/temp_frames"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating Scene Images...")
    img1 = create_scene_1()
    img2 = create_scene_2()
    img3 = create_scene_3()
    img4 = create_scene_4()

    p1 = os.path.join(temp_dir, "scene1.png")
    p2 = os.path.join(temp_dir, "scene2.png")
    p3 = os.path.join(temp_dir, "scene3.png")
    p4 = os.path.join(temp_dir, "scene4.png")

    img1.save(p1)
    img2.save(p2)
    img3.save(p3)
    img4.save(p4)

    print("Assembling Video Clips (28 seconds total)...")
    clip1 = ImageClip(p1, duration=6)    # 0 - 6s
    clip2 = ImageClip(p2, duration=7)    # 6 - 13s
    clip3 = ImageClip(p3, duration=8)    # 13 - 21s
    clip4 = ImageClip(p4, duration=7)    # 21 - 28s

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4], method="compose")

    print(f"Rendering final MP4 to {output_path}...")
    final_video.write_videofile(
        output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    # Cleanup temp frames
    for p in [p1, p2, p3, p4]:
        if os.path.exists(p):
            os.remove(p)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

    print(f"\n[SUCCESS] Day 8 Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()

