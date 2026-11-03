"""
Day 08: 40-Second Ultra-Aesthetic Reel with Real Code Snippets & IDE Window
===========================================================================
Creates a 40-second, 1080x1920 (9:16) vertical MP4 Reel featuring:
- Ambient mesh gradient background with glowing neon orbs & grid dots
- Carbon / VS Code style code editor window with line numbers & syntax highlighting
- 5 comprehensive scenes covering all core concepts & interview traps:
  1. The Single-Element Comma Trap (0-8s)
  2. Star (*) Unpacking & In-Place Swap (8-16s)
  3. Tuples vs Lists 1.84x Speed Benchmark & Hashability (16-25s)
  4. The Infamous '+=' on Tuple with List Trap (25-33s)
  5. AI PyTorch Tensor Shapes & GitHub Update (33-40s)
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
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 62)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 48)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 40)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 30)
FONT_LINENUM = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 26)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)

# Vibrant Syntax & Theme Colors
COLOR_BG_BASE = [11, 14, 27]
COLOR_TEXT_MAIN = (248, 250, 252)     # Crisp White
COLOR_TEXT_MUTED = (148, 163, 184)   # Slate Grey
COLOR_LINE_NUM = (71, 85, 105)       # Line number grey
COLOR_CYAN = (6, 182, 212)           # Neon Cyan
COLOR_PURPLE = (168, 85, 247)        # Neon Violet
COLOR_PINK = (244, 63, 94)           # Rose/Pink
COLOR_GREEN = (34, 197, 94)          # Emerald Neon
COLOR_YELLOW = (250, 204, 21)        # Gold/Yellow
COLOR_BLUE = (96, 165, 250)          # Soft Sky Blue


def generate_ambient_background():
    """Generates an ultra-modern dark mesh gradient with dual-color ambient glowing orbs."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_BASE

    # Orb 1: Neon Violet ambient glow (Top-Left)
    d1 = np.sqrt((x - 180)**2 + (y - 320)**2)
    w1 = (np.clip(1.0 - d1 / 750.0, 0, 1) ** 2.2)[:, :, None]
    base += w1 * np.array([139, 92, 246], dtype=np.float32) * 0.9

    # Orb 2: Neon Cyan ambient glow (Bottom-Right)
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


CACHED_BG = generate_ambient_background()


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 08 / 30"):
    """Paints top header, author branding, and bottom progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Glass pill with purple border)
    badge_w, badge_h = 500, 62
    bx0 = (WIDTH - badge_w) // 2
    by0 = 100
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=31, fill=(20, 24, 48, 230), outline=(139, 92, 246, 200), width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_TEXT_MAIN, anchor="mm")

    # Subtitle Pill
    draw.text((WIDTH // 2, 195), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Glowing Progress Bar at Bottom
    bar_y = HEIGHT - 75
    bar_w = WIDTH - 160
    draw.rounded_rectangle([80, bar_y, 80 + bar_w, bar_y + 14], radius=7, fill=(20, 25, 45, 220), outline=(40, 50, 80, 150))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([80, bar_y, 80 + fill_len, bar_y + 14], radius=7, fill=COLOR_CYAN)

    return img, draw


def draw_ide_window(draw, x0, y0, x1, y1, filename, code_lines, terminal_output=None, border_color=(139, 92, 246, 140)):
    """Draws a professional Carbon / VS Code style window with line numbers and syntax highlighting."""
    # Window Box
    draw.rounded_rectangle([x0, y0, x1, y1], radius=26, fill=(18, 22, 42, 245), outline=border_color, width=2)

    # Mac Style Window Dots
    draw.ellipse([x0 + 32, y0 + 30, x0 + 50, y0 + 48], fill=(255, 95, 86))
    draw.ellipse([x0 + 64, y0 + 30, x0 + 82, y0 + 48], fill=(255, 189, 46))
    draw.ellipse([x0 + 96, y0 + 30, x0 + 114, y0 + 48], fill=(39, 201, 63))

    # Tab filename
    draw.text((x0 + 145, y0 + 39), filename, font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="lm")
    draw.line([x0 + 20, y0 + 68, x1 - 20, y0 + 68], fill=(45, 55, 85, 180), width=1)

    # Code Area with Line Numbers
    y_code = y0 + 98
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        # Line number
        draw.text((x0 + 35, y_code), f"{idx:2d}", font=FONT_LINENUM, fill=COLOR_LINE_NUM)
        # Vertical divider
        draw.line([x0 + 85, y_code - 5, x0 + 85, y_code + 32], fill=(40, 48, 75, 120), width=1)
        # Code text
        draw.text((x0 + 105, y_code), code_text, font=FONT_CODE, fill=color)
        y_code += 48

    # Optional Terminal Output Box at bottom of IDE
    if terminal_output:
        t_y0 = y1 - 130
        draw.rounded_rectangle([x0 + 25, t_y0, x1 - 25, y1 - 25], radius=16, fill=(11, 14, 27, 250), outline=(6, 182, 212, 120), width=1)
        draw.text((x0 + 45, t_y0 + 30), "Terminal Output:", font=FONT_BADGE, fill=COLOR_CYAN, anchor="lm")
        draw.text((x0 + 45, t_y0 + 75), terminal_output, font=FONT_CODE, fill=COLOR_TEXT_MAIN, anchor="lm")


# -------------------------------------------------------------------------
# SCENE 1 (0 to 8s): The Single-Element Comma Trap Code Snippet
# -------------------------------------------------------------------------
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 08 / 30  •  WEEK 2 KICK-OFF")

    draw.text((WIDTH // 2, 310), "The Single-Element Trap", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 385), "Comma defines the tuple, NOT parentheses!", font=FONT_SUB, fill=COLOR_PURPLE, anchor="mm")

    code_lines = [
        ("# Parentheses alone mean math grouping:", COLOR_GREEN),
        ("not_a_tuple = (42)", COLOR_PINK),
        ("print(type(not_a_tuple))  # <class 'int'>", COLOR_TEXT_MUTED),
        ("", COLOR_TEXT_MAIN),
        ("# The Trailing Comma creates the tuple!", COLOR_GREEN),
        ("is_a_tuple = (42,)", COLOR_CYAN),
        ("print(type(is_a_tuple))   # <class 'tuple'>", COLOR_YELLOW),
        ("", COLOR_TEXT_MAIN),
        ("# Packing without parentheses works too:", COLOR_GREEN),
        ("coords = 19.0760, 72.8777", COLOR_TEXT_MAIN),
        ("print(type(coords))       # <class 'tuple'>", COLOR_TEXT_MUTED)
    ]

    draw_ide_window(
        draw, 70, 470, WIDTH - 70, 1330,
        "01_comma_trap.py",
        code_lines,
        terminal_output=">>> (42) -> int  |  (42,) -> tuple (Length: 1)",
        border_color=(139, 92, 246, 160)
    )

    # Bottom Pill
    pill_w, pill_h = 620, 72
    px = (WIDTH - pill_w) // 2
    py = 1420
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=36, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, py + pill_h // 2), "💡 Always use (item,) for single tuples!", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 2 (8 to 16s): Star (*) Unpacking & In-Place Swap Code Snippet
# -------------------------------------------------------------------------
def create_scene_2():
    img, draw = draw_canvas(0.40, "PYTHONIC TRICKS")

    draw.text((WIDTH // 2, 310), "Advanced Tuple Unpacking", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 385), "Star (*) Operator & Zero-Temp Variable Swap", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    code_lines = [
        ("# 1. In-Place Swap (No temp variable!):", COLOR_GREEN),
        ("a, b = 100, 200", COLOR_TEXT_MAIN),
        ("a, b = b, a  # Packed into (b, a) tuple", COLOR_YELLOW),
        ("print(f'a={a}, b={b}')  # a=200, b=100", COLOR_TEXT_MUTED),
        ("", COLOR_TEXT_MAIN),
        ("# 2. Extended Star (*) Unpacking (PEP 3132):", COLOR_GREEN),
        ("data = (10, 20, 30, 40, 50, 60)", COLOR_TEXT_MAIN),
        ("first, *middle, last = data", COLOR_CYAN),
        ("print(first)   # 10", COLOR_TEXT_MAIN),
        ("print(middle)  # [20, 30, 40, 50]", COLOR_YELLOW),
        ("print(last)    # 60", COLOR_TEXT_MAIN)
    ]

    draw_ide_window(
        draw, 70, 470, WIDTH - 70, 1330,
        "02_star_unpacking.py",
        code_lines,
        terminal_output="Swapped: a=200, b=100 | Middle elements: [20, 30, 40, 50]",
        border_color=(6, 182, 212, 160)
    )

    pill_w, pill_h = 620, 72
    px = (WIDTH - pill_w) // 2
    py = 1420
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=36, fill=(20, 24, 50, 240), outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, py + pill_h // 2), "⚡ Clean, Pythonic, and Highly Readable", font=FONT_SUB, fill=COLOR_PURPLE, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 3 (16 to 25s): Tuples vs Lists Speed & Memory Benchmark
# -------------------------------------------------------------------------
def create_scene_3():
    img, draw = draw_canvas(0.62, "SPEED & ARCHITECTURE BENCHMARK")

    draw.text((WIDTH // 2, 310), "Tuples vs Lists", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 385), "Live CPython Benchmark: 10 Million Iterations", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    code_lines = [
        ("# Live Benchmark: Creating 10,000,000 elements", COLOR_GREEN),
        ("list_time  = 1.0882  # Slower dynamic array", COLOR_PINK),
        ("tuple_time = 0.5904  # Faster fixed-size", COLOR_GREEN),
        ("", COLOR_TEXT_MAIN),
        ("# Memory Footprint (sys.getsizeof):", COLOR_GREEN),
        ("sys.getsizeof([])  # 56 bytes (over-allocated)", COLOR_PINK),
        ("sys.getsizeof(())  # 48 bytes (exact size)", COLOR_GREEN),
        ("", COLOR_TEXT_MAIN),
        ("# Hashability: Tuples can be Dict Keys!", COLOR_GREEN),
        ("valid_dict = {(19.07, 72.87): 'Mumbai'}  # OK", COLOR_CYAN),
        ("invalid_dict = {[19.07, 72.87]: 'Error'} # TypeError", COLOR_PINK)
    ]

    draw_ide_window(
        draw, 70, 470, WIDTH - 70, 1310,
        "03_speed_benchmark.py",
        code_lines,
        terminal_output="⚡ RESULT: Tuples are 1.84x FASTER than Lists in CPython!",
        border_color=(34, 197, 94, 180)
    )

    # Big Hero Stat Badge
    h_y0 = 1380
    draw.rounded_rectangle([100, h_y0, WIDTH - 100, h_y0 + 120], radius=24, fill=(34, 197, 94, 40), outline=COLOR_GREEN, width=3)
    draw.text((WIDTH // 2, h_y0 + 42), "⚡ 1.84x FASTER CREATION SPEED", font=FONT_TITLE, fill=COLOR_GREEN, anchor="mm")
    draw.text((WIDTH // 2, h_y0 + 88), "Zero over-allocation overhead + Constant Folding", font=FONT_BADGE, fill=COLOR_TEXT_MAIN, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 4 (25 to 33s): The Infamous '+=' on Tuple with List Trap
# -------------------------------------------------------------------------
def create_scene_4():
    img, draw = draw_canvas(0.82, "TOP INTERVIEW TRAP")

    draw.text((WIDTH // 2, 310), "The Infamous '+=' Trap", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 385), "Raises TypeError, but STILL mutates the list?!", font=FONT_SUB, fill=COLOR_PINK, anchor="mm")

    code_lines = [
        ("# The Classic Python Interview Brain Teaser:", COLOR_GREEN),
        ("t = (1, 2, [3, 4])  # Tuple with inner list", COLOR_TEXT_MAIN),
        ("", COLOR_TEXT_MAIN),
        ("try:", COLOR_PURPLE),
        ("    t[2] += [5]      # What happens here?", COLOR_PINK),
        ("except TypeError as e:", COLOR_PURPLE),
        ("    print(e)         # 'tuple' does not support assignment", COLOR_TEXT_MUTED),
        ("", COLOR_TEXT_MAIN),
        ("print(t)             # (1, 2, [3, 4, 5]) !!!", COLOR_YELLOW),
        ("# WHY? += mutates inner list in-place first,", COLOR_GREEN),
        ("# then tuple assignment raises TypeError!", COLOR_GREEN)
    ]

    draw_ide_window(
        draw, 70, 470, WIDTH - 70, 1330,
        "04_interview_trap.py",
        code_lines,
        terminal_output="Result: (1, 2, [3, 4, 5]) -> List mutated despite TypeError!",
        border_color=(244, 63, 94, 180)
    )

    pill_w, pill_h = 620, 72
    px = (WIDTH - pill_w) // 2
    py = 1420
    draw.rounded_rectangle([px, py, px + pill_w, py + pill_h], radius=36, fill=(20, 24, 50, 240), outline=COLOR_PINK, width=2)
    draw.text((WIDTH // 2, py + pill_h // 2), "🔥 Ask this in your next Python interview!", font=FONT_SUB, fill=COLOR_PINK, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 5 (33 to 40s): AI Tensor Dimensions & GitHub Update
# -------------------------------------------------------------------------
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 08 COMPLETE")

    draw.text((WIDTH // 2, 310), "AI Tensor Shapes & GitHub", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 385), "PyTorch Shapes & All Code Live on GitHub!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    code_lines = [
        ("# Why AI frameworks use immutable tuples:", COLOR_GREEN),
        ("import torch", COLOR_TEXT_MAIN),
        ("tensor_shape = (32, 3, 224, 224)", COLOR_CYAN),
        ("# (Batch Size, Channels, Height, Width)", COLOR_TEXT_MUTED),
        ("print(tensor_shape)  # Immutable during training", COLOR_YELLOW),
        ("", COLOR_TEXT_MAIN),
        ("# GitHub Repository Modules Live:", COLOR_GREEN),
        ("├── 01_tuple_fundamentals_and_creation.py", COLOR_TEXT_MAIN),
        ("├── 02_tuples_vs_lists_memory_and_speed.py", COLOR_CYAN),
        ("├── 03_tuple_operations_and_unpacking.py", COLOR_TEXT_MAIN),
        ("├── 04_tuple_interview_questions.py", COLOR_PURPLE),
        ("└── my_practice.py (6 Hands-on tasks)", COLOR_YELLOW)
    ]

    draw_ide_window(
        draw, 70, 470, WIDTH - 70, 1330,
        "pytorch_tensor_and_repo.py",
        code_lines,
        terminal_output="github.com/Sapnayadav1608/fullstack-python-ai -> Pushed!",
        border_color=(34, 197, 94, 180)
    )

    # Outro Call to Action Card
    draw.rounded_rectangle([80, 1400, WIDTH - 80, 1530], radius=28, fill=(20, 24, 52, 240), outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, 1442), "Follow along for Day 09! ✨", font=FONT_TITLE, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 1495), "Drop your questions in the comments below 👇", font=FONT_BADGE, fill=COLOR_CYAN, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day8/day8_reel_video.mp4"
    temp_dir = "D:/learn-python/day8/temp_frames_40s"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating 5 High-Aesthetic Code Scene Frames...")
    img1 = create_scene_1()
    img2 = create_scene_2()
    img3 = create_scene_3()
    img4 = create_scene_4()
    img5 = create_scene_5()

    p1 = os.path.join(temp_dir, "scene1.png")
    p2 = os.path.join(temp_dir, "scene2.png")
    p3 = os.path.join(temp_dir, "scene3.png")
    p4 = os.path.join(temp_dir, "scene4.png")
    p5 = os.path.join(temp_dir, "scene5.png")

    img1.save(p1)
    img2.save(p2)
    img3.save(p3)
    img4.save(p4)
    img5.save(p5)

    print("Concatenating Video Clips (Total = 40 Seconds @ 24fps)...")
    # Durations: 8s + 8s + 9s + 8s + 7s = 40 seconds
    clip1 = ImageClip(p1, duration=8)
    clip2 = ImageClip(p2, duration=8)
    clip3 = ImageClip(p3, duration=9)
    clip4 = ImageClip(p4, duration=8)
    clip5 = ImageClip(p5, duration=7)

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5], method="compose")

    print(f"Rendering 40s final MP4 to {output_path}...")
    final_video.write_videofile(
        output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    # Clean temporary frame files
    for p in [p1, p2, p3, p4, p5]:
        if os.path.exists(p):
            os.remove(p)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

    print(f"\n[SUCCESS] Day 8 40-Second Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()

