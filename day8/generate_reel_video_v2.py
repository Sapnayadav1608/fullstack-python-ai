"""
Day 08: Premium Animated Instagram Reel Video Generator (V2 - Ultra Aesthetic)
==============================================================================
Creates a high-end, 1080x1920 (9:16) vertical Reel with:
- Cyberpunk / Linear-style dark ambient gradient background with glowing light orbs & tech mesh
- Glassmorphism frosted cards with neon gradient borders
- Rich syntax-highlighted code blocks
- Hero KPI benchmark comparison (1.84x speedup)
- Clean typography and glowing badges
"""

import os
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, concatenate_videoclips

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

WIDTH, HEIGHT = 1080, 1920
FPS = 24

# Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 68)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 52)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 42)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 34)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 32)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)

# Vibrant Color Palette
COLOR_TEXT_MAIN = (248, 250, 252)     # Crisp White
COLOR_TEXT_MUTED = (148, 163, 184)   # Slate Grey
COLOR_CYAN = (6, 182, 212)           # Neon Cyan
COLOR_PURPLE = (168, 85, 247)        # Neon Violet
COLOR_PINK = (236, 72, 153)          # Hot Pink
COLOR_GREEN = (34, 197, 94)          # Emerald Neon
COLOR_YELLOW = (250, 204, 21)        # Gold/Yellow
COLOR_RED = (244, 63, 94)            # Rose/Red


def generate_ambient_background():
    """Generates an ultra-modern dark mesh gradient with dual-color ambient glowing orbs."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    
    # Deep space obsidian/navy base
    base[:, :] = [11, 14, 27]

    # Orb 1: Neon Violet / Purple ambient glow (Top-Left)
    d1 = np.sqrt((x - 180)**2 + (y - 320)**2)
    w1 = (np.clip(1.0 - d1 / 750.0, 0, 1) ** 2.2)[:, :, None]
    base += w1 * np.array([139, 92, 246], dtype=np.float32) * 0.9

    # Orb 2: Neon Cyan / Blue ambient glow (Bottom-Right)
    d2 = np.sqrt((x - 900)**2 + (y - 1580)**2)
    w2 = (np.clip(1.0 - d2 / 800.0, 0, 1) ** 2.2)[:, :, None]
    base += w2 * np.array([6, 182, 212], dtype=np.float32) * 0.85

    # Orb 3: Subtle Hot Pink highlight (Mid-Right)
    d3 = np.sqrt((x - 980)**2 + (y - 750)**2)
    w3 = (np.clip(1.0 - d3 / 550.0, 0, 1) ** 2.5)[:, :, None]
    base += w3 * np.array([236, 72, 153], dtype=np.float32) * 0.65

    # Ambient Tech Grid Dots
    dot_mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    dot_mask[::50, ::50] = True
    base[dot_mask] = np.clip(base[dot_mask] + 45, 0, 255)

    base = np.clip(base, 0, 255).astype(np.uint8)
    return Image.fromarray(base)


# Cache base background image
CACHED_BG = generate_ambient_background()


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 08 / 30"):
    """Copies base ambient background and paints header badge and progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Glass pill with purple/cyan border)
    badge_w, badge_h = 480, 64
    bx0 = (WIDTH - badge_w) // 2
    by0 = 110
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=32, fill=(20, 24, 45, 230), outline=(139, 92, 246, 200), width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_TEXT_MAIN, anchor="mm")

    # Subtitle Pill
    draw.text((WIDTH // 2, 205), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Glowing Progress Bar at Bottom
    bar_y = HEIGHT - 80
    bar_w = WIDTH - 160
    draw.rounded_rectangle([80, bar_y, 80 + bar_w, bar_y + 14], radius=7, fill=(20, 25, 45, 220), outline=(40, 50, 80, 150))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([80, bar_y, 80 + fill_len, bar_y + 14], radius=7, fill=COLOR_CYAN)

    return img, draw


def create_scene_1():
    """Scene 1 (0-6s): Hook & Week 2 Introduction"""
    img, draw = draw_canvas(0.2, "DAY 08 / 30  •  WEEK 2 KICK-OFF")

    # Big Glowing Title
    draw.text((WIDTH // 2, 340), "Python Tuples", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 420), "Deep Dive & Memory Architecture", font=FONT_TITLE, fill=COLOR_PURPLE, anchor="mm")

    # Glass Code Window Card
    c_x0, c_y0 = 70, 530
    c_x1, c_y1 = WIDTH - 70, 1260
    draw.rounded_rectangle([c_x0, c_y0, c_x1, c_y1], radius=28, fill=(18, 22, 42, 240), outline=(139, 92, 246, 120), width=2)

    # Window Header (Mac Glass style)
    draw.ellipse([c_x0 + 35, c_y0 + 35, c_x0 + 55, c_y0 + 55], fill=(255, 95, 86))
    draw.ellipse([c_x0 + 72, c_y0 + 35, c_x0 + 92, c_y0 + 55], fill=(255, 189, 46))
    draw.ellipse([c_x0 + 109, c_y0 + 35, c_x0 + 129, c_y0 + 55], fill=(39, 201, 63))
    draw.text((c_x0 + 160, c_y0 + 45), "01_tuples_fundamentals.py", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="lm")

    # Divider line
    draw.line([c_x0 + 20, c_y0 + 75, c_x1 - 20, c_y0 + 75], fill=(40, 50, 80, 180), width=1)

    # Syntax Highlighted Code Lines
    code = [
        ("# 1. The Single-Element Comma Trap!", COLOR_GREEN),
        ("single_tup = (42,)   ", COLOR_TEXT_MAIN),
        ("not_a_tuple = (42)    ", COLOR_PINK),
        ("", COLOR_TEXT_MAIN),
        ("# 2. Pythonic Star (*) Unpacking", COLOR_GREEN),
        ("stream = (10, 20, 30, 40, 50)", COLOR_TEXT_MAIN),
        ("first, *middle, last = stream", COLOR_CYAN),
        ("print(middle)  # [20, 30, 40]", COLOR_YELLOW),
        ("", COLOR_TEXT_MAIN),
        ("# 3. PyTorch AI Tensor Dimensions", COLOR_GREEN),
        ("tensor_shape = (32, 3, 224, 224)", COLOR_PURPLE),
    ]

    y_pos = c_y0 + 110
    for line, color in code:
        draw.text((c_x0 + 45, y_pos), line, font=FONT_CODE, fill=color)
        y_pos += 54

    # Bottom Pill
    pill_w, pill_h = 620, 76
    px = (WIDTH - pill_w) // 2
    py = 1350
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=38, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, py + pill_h // 2), "🔒 Immutable  •  ⚡ Faster  •  📦 RAM Efficient", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img


def create_scene_2():
    """Scene 2 (6-13s): The Big Question & Live Benchmark"""
    img, draw = draw_canvas(0.48, "THE BIG INTERVIEW QUESTION")

    draw.text((WIDTH // 2, 330), "Why Tuples When", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 415), "Lists Already Exist?", font=FONT_TITLE, fill=COLOR_CYAN, anchor="mm")

    # Main Card
    card_x0, card_y0 = 70, 510
    card_x1, card_y1 = WIDTH - 70, 1420
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=28, fill=(18, 22, 42, 245), outline=(6, 182, 212, 100), width=2)

    draw.text((WIDTH // 2, card_y0 + 60), "LIVE BENCHMARK IN CPYTHON", font=FONT_HEADING, fill=COLOR_PURPLE, anchor="mm")
    draw.text((WIDTH // 2, card_y0 + 115), "Creating 10,000,000 Elements on Windows", font=FONT_SUB, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Side-by-side comparison boxes
    box_w = (card_x1 - card_x0 - 70) // 2
    
    # List Box
    b1_x0 = card_x0 + 30
    b1_x1 = b1_x0 + box_w
    draw.rounded_rectangle([b1_x0, card_y0 + 170, b1_x1, card_y0 + 470], radius=20, fill=(26, 18, 30, 240), outline=(244, 63, 94, 160), width=2)
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 215), "PYTHON LIST", font=FONT_HEADING, fill=COLOR_RED, anchor="mm")
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 300), "1.088s", font=FONT_HERO, fill=COLOR_RED, anchor="mm")
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 380), "Dynamic Over-allocation", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="mm")
    draw.text(((b1_x0 + b1_x1) // 2, card_y0 + 420), "Extra RAM Waste", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Tuple Box
    b2_x0 = b1_x1 + 20
    b2_x1 = b2_x0 + box_w
    draw.rounded_rectangle([b2_x0, card_y0 + 170, b2_x1, card_y0 + 470], radius=20, fill=(15, 30, 26, 240), outline=COLOR_GREEN, width=2)
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 215), "PYTHON TUPLE", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 300), "0.590s", font=FONT_HERO, fill=COLOR_GREEN, anchor="mm")
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 380), "Exact Memory Allocation", font=FONT_BADGE, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text(((b2_x0 + b2_x1) // 2, card_y0 + 420), "Zero Wasted Bytes", font=FONT_BADGE, fill=COLOR_GREEN, anchor="mm")

    # Hero Banner: 1.84x FASTER
    h_y0 = card_y0 + 510
    h_y1 = h_y0 + 120
    draw.rounded_rectangle([card_x0 + 30, h_y0, card_x1 - 30, h_y1], radius=22, fill=(34, 197, 94, 45), outline=COLOR_GREEN, width=3)
    draw.text((WIDTH // 2, h_y0 + 42), "⚡ 1.84x FASTER EXECUTION", font=FONT_TITLE, fill=COLOR_GREEN, anchor="mm")
    draw.text((WIDTH // 2, h_y0 + 88), "Optimized by CPython Constant Folding & Free-Lists", font=FONT_BADGE, fill=COLOR_TEXT_MAIN, anchor="mm")

    # Key Architecture Points
    bullets = [
        ("• Fixed Memory Size: ", COLOR_CYAN, "Tuples don't carry dynamic buffer overhead"),
        ("• Hashability Rule : ", COLOR_PURPLE, "Tuples can be Dictionary Keys, Lists CANNOT"),
        ("• Write Protection  : ", COLOR_YELLOW, "Prevents accidental data modification in APIs")
    ]
    cur_y = card_y0 + 670
    for head, h_col, body in bullets:
        draw.text((card_x0 + 45, cur_y), head, font=FONT_BODY, fill=h_col)
        draw.text((card_x0 + 330, cur_y), body, font=FONT_BODY, fill=COLOR_TEXT_MAIN)
        cur_y += 62

    return img


def create_scene_3():
    """Scene 3 (13-21s): Key Concepts Mastered"""
    img, draw = draw_canvas(0.75, "TOPICS CONQUERED")

    draw.text((WIDTH // 2, 330), "Core Concepts", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 415), "Mastered on Day 08", font=FONT_TITLE, fill=COLOR_PURPLE, anchor="mm")

    cards = [
        ("01", "The Single-Element Comma Trap", "(42,) is a tuple, but (42) evaluates as an int", COLOR_CYAN),
        ("02", "Star (*) Extended Unpacking", "first, *middle, last = numbers", COLOR_PURPLE),
        ("03", "Tuples as Dictionary Keys", "Valid keys because tuples are hashable", COLOR_GREEN),
        ("04", "Mutable Object in Tuple Trap", "t = (1, [2, 3]) reference vs internal list state", COLOR_PINK),
        ("05", "AI Tensor Dimensions", "PyTorch & NumPy use immutable shape tuples", COLOR_YELLOW)
    ]

    cy = 500
    for num, title, desc, accent_color in cards:
        draw.rounded_rectangle([70, cy, WIDTH - 70, cy + 135], radius=20, fill=(18, 22, 42, 240), outline=(50, 60, 95, 180), width=2)
        # Left Accent pill
        draw.rounded_rectangle([70, cy, 82, cy + 135], radius=6, fill=accent_color)

        # Number Badge
        draw.rounded_rectangle([105, cy + 28, 180, cy + 105], radius=16, fill=(11, 14, 27, 240), outline=accent_color, width=2)
        draw.text((142, cy + 66), num, font=FONT_HEADING, fill=accent_color, anchor="mm")

        # Texts
        draw.text((210, cy + 45), title, font=FONT_HEADING, fill=COLOR_TEXT_MAIN, anchor="lm")
        draw.text((210, cy + 95), desc, font=FONT_BODY, fill=COLOR_TEXT_MUTED, anchor="lm")
        cy += 160

    return img


def create_scene_4():
    """Scene 4 (21-28s): GitHub Update & Outro CTA"""
    img, draw = draw_canvas(1.0, "DAY 08 COMPLETE")

    draw.text((WIDTH // 2, 330), "Code & Workbook", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 415), "Officially Live on GitHub! 🚀", font=FONT_TITLE, fill=COLOR_GREEN, anchor="mm")

    # GitHub Repository Card
    card_x0, card_y0 = 70, 510
    card_x1, card_y1 = WIDTH - 70, 1310
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=28, fill=(18, 22, 42, 245), outline=(34, 197, 94, 140), width=2)

    # Header in GitHub box
    draw.text((WIDTH // 2, card_y0 + 65), "github.com/Sapnayadav1608", font=FONT_TITLE, fill=COLOR_CYAN, anchor="mm")
    draw.text((WIDTH // 2, card_y0 + 125), "fullstack-python-ai / day8", font=FONT_SUB, fill=COLOR_TEXT_MUTED, anchor="mm")

    # File checklist
    files = [
        ("01_tuple_fundamentals_and_creation.py", COLOR_TEXT_MAIN),
        ("02_tuples_vs_lists_memory_and_speed.py", COLOR_CYAN),
        ("03_tuple_operations_and_unpacking.py", COLOR_TEXT_MAIN),
        ("04_tuple_interview_questions.py", COLOR_PURPLE),
        ("my_practice.py (6 Hands-On Student Tasks)", COLOR_YELLOW),
        ("README.md (Notes & Cheat-Sheet)", COLOR_TEXT_MUTED)
    ]

    fy = card_y0 + 205
    for f, col in files:
        draw.rounded_rectangle([card_x0 + 35, fy - 15, card_x1 - 35, fy + 45], radius=12, fill=(11, 14, 27, 200))
        draw.text((card_x0 + 55, fy + 15), "✓", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")
        draw.text((card_x0 + 95, fy + 15), f, font=FONT_CODE, fill=col, anchor="lm")
        fy += 75

    # Outro Call to Action Card
    draw.rounded_rectangle([80, 1380, WIDTH - 80, 1530], radius=28, fill=(20, 24, 52, 240), outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, 1425), "Follow along for Day 09! ✨", font=FONT_TITLE, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 1480), "Drop your questions & answers in the comments below 👇", font=FONT_BADGE, fill=COLOR_CYAN, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day8/day8_reel_video.mp4"
    temp_dir = "D:/learn-python/day8/temp_frames_v2"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating High-Aesthetic Scene Frames...")
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

    print("Concatenating Video Clips (28 Seconds @ 24fps)...")
    clip1 = ImageClip(p1, duration=6)
    clip2 = ImageClip(p2, duration=7)
    clip3 = ImageClip(p3, duration=8)
    clip4 = ImageClip(p4, duration=7)

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

    # Clean temporary frame files
    for p in [p1, p2, p3, p4]:
        if os.path.exists(p):
            os.remove(p)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

    print(f"\n[SUCCESS] Day 8 Ultra-Aesthetic Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()

