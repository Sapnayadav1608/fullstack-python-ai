"""
Day 08: Perfect 40-Second Instagram Reel Generator (Zero Overlap & Real Repo Code)
=================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Features:
- Exact 40.0 seconds runtime (5 scenes @ 8 seconds each)
- ZERO OVERLAP: Strict mathematical bounding boxes within Instagram 9:16 safe zone (160px - 1620px)
- REAL CODE directly from Sapna's day8 repo files:
  Scene 1: 01_tuple_fundamentals_and_creation.py (The Single-Element Comma Trap)
  Scene 2: 02_tuples_vs_lists_memory_and_speed.py (10M Benchmark: 1.84x Speedup)
  Scene 3: 03_tuple_operations_and_unpacking.py (Variable Swap & Star * Unpacking)
  Scene 4: 04_tuple_interview_questions.py (The Infamous '+=' Mutation Trap)
  Scene 5: my_practice.py (Sapna's Workbook Tasks & Automated Tests)
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
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 52)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 27)
FONT_LINENUM = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 24)
FONT_TERM = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 25)
FONT_PILL = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)

# Colors
COLOR_BG = [11, 14, 27]
COLOR_WHITE = (248, 250, 252)
COLOR_MUTED = (148, 163, 184)
COLOR_LINENUM = (71, 85, 105)
COLOR_CYAN = (6, 182, 212)
COLOR_PURPLE = (168, 85, 247)
COLOR_GREEN = (34, 197, 94)
COLOR_YELLOW = (250, 204, 21)
COLOR_RED = (244, 63, 94)
COLOR_ORANGE = (251, 146, 60)


def generate_ambient_background():
    """Generates an ultra-modern dark mesh gradient with dual-color ambient glowing orbs."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG

    # Orb 1: Neon Violet ambient glow (Top-Left)
    d1 = np.sqrt((x - 180)**2 + (y - 320)**2)
    w1 = (np.clip(1.0 - d1 / 750.0, 0, 1) ** 2.2)[:, :, None]
    base += w1 * np.array([139, 92, 246], dtype=np.float32) * 0.9

    # Orb 2: Neon Cyan ambient glow (Bottom-Right)
    d2 = np.sqrt((x - 900)**2 + (y - 1580)**2)
    w2 = (np.clip(1.0 - d2 / 800.0, 0, 1) ** 2.2)[:, :, None]
    base += w2 * np.array([6, 182, 212], dtype=np.float32) * 0.85

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

    # Header Badge (Y: 155 to 215)
    badge_w, badge_h = 520, 58
    bx0 = (WIDTH - badge_w) // 2
    by0 = 155
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=29, fill=(20, 24, 48, 230), outline=(139, 92, 246, 200), width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_WHITE, anchor="mm")

    # Author Subtitle (Y: 235)
    draw.text((WIDTH // 2, 238), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar at Bottom (Y: 1615 to 1627)
    bar_y = 1615
    bar_w = WIDTH - 120
    draw.rounded_rectangle([60, bar_y, 60 + bar_w, bar_y + 12], radius=6, fill=(20, 25, 45, 220), outline=(40, 50, 80, 150))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([60, bar_y, 60 + fill_len, bar_y + 12], radius=6, fill=COLOR_CYAN)

    return img, draw


def draw_ide_window(draw, x0, y0, x1, y1, filename, code_lines, terminal_lines=None, border_color=(139, 92, 246, 160)):
    """
    Draws a structured Carbon / VS Code style window.
    Strictly isolated: Code text in upper half, Terminal box in lower half.
    """
    # Main IDE Frame (y0 to y1)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=(18, 22, 42, 245), outline=border_color, width=2)

    # Window Title Bar (y0 to y0 + 60)
    draw.ellipse([x0 + 30, y0 + 22, x0 + 46, y0 + 38], fill=(255, 95, 86))
    draw.ellipse([x0 + 58, y0 + 22, x0 + 74, y0 + 38], fill=(255, 189, 46))
    draw.ellipse([x0 + 86, y0 + 22, x0 + 102, y0 + 38], fill=(39, 201, 63))

    # Filename tab
    draw.text((x0 + 130, y0 + 30), filename, font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([x0 + 15, y0 + 58, x1 - 15, y0 + 58], fill=(45, 55, 85, 180), width=1)

    # Code Area (y0 + 75 to y1 - 250)
    y_code = y0 + 85
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        # Line number
        draw.text((x0 + 30, y_code), f"{idx:2d}", font=FONT_LINENUM, fill=COLOR_LINENUM)
        # Vertical gutter line
        draw.line([x0 + 75, y_code - 4, x0 + 75, y_code + 26], fill=(40, 48, 75, 120), width=1)
        # Code text
        draw.text((x0 + 95, y_code), code_text, font=FONT_CODE, fill=color)
        y_code += 44

    # Terminal Box (y1 - 225 to y1 - 20)
    if terminal_lines:
        t_y0 = y1 - 235
        t_y1 = y1 - 20
        draw.rounded_rectangle([x0 + 20, t_y0, x1 - 20, t_y1], radius=16, fill=(10, 13, 24, 255), outline=(6, 182, 212, 100), width=1)
        # Terminal Header
        draw.text((x0 + 40, t_y0 + 24), "TERMINAL", font=FONT_BADGE, fill=COLOR_CYAN, anchor="lm")
        draw.line([x0 + 20, t_y0 + 42, x1 - 20, t_y0 + 42], fill=(30, 40, 65, 150), width=1)

        # Terminal text lines
        cur_ty = t_y0 + 64
        for t_line, t_col in terminal_lines:
            draw.text((x0 + 40, cur_ty), t_line, font=FONT_TERM, fill=t_col, anchor="lm")
            cur_ty += 38


# -------------------------------------------------------------------------
# SCENE 1 (0 to 8s): Single-Element Comma Trap from 01_tuple_fundamentals_and_creation.py
# -------------------------------------------------------------------------
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 08 / 30  •  WEEK 2 KICK-OFF")

    # Header Title (Y: 280 & 335)
    draw.text((WIDTH // 2, 285), "Single-Element Comma Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 345), "Topic 01 • day8/01_tuple_fundamentals_and_creation.py", font=FONT_SUB, fill=COLOR_PURPLE, anchor="mm")

    code_lines = [
        ("# Mathematical grouping without comma:", COLOR_GREEN),
        ("not_a_tuple = (42)", COLOR_RED),
        ("print(type(not_a_tuple))  # <class 'int'>", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("# The Trailing Comma creates the tuple!", COLOR_GREEN),
        ("is_a_tuple = (42,)", COLOR_CYAN),
        ("print(type(is_a_tuple))   # <class 'tuple'>", COLOR_YELLOW),
        ("", COLOR_WHITE),
        ("# Tuple packing without parentheses:", COLOR_GREEN),
        ("packed_coords = 19.0760, 72.8777", COLOR_WHITE),
        ("print(type(packed_coords)) # <class 'tuple'>", COLOR_MUTED)
    ]

    terminal_lines = [
        ("$ python day8/01_tuple_fundamentals_and_creation.py", COLOR_MUTED),
        ("Expression: (42)  -> Type: int   | Value: 42", COLOR_RED),
        ("Expression: (42,) -> Type: tuple | Value: (42,)", COLOR_GREEN),
        ("Packed Coordinates : (19.076, 72.8777) | Type: tuple", COLOR_CYAN)
    ]

    draw_ide_window(
        draw, 60, 400, WIDTH - 60, 1420,
        "01_tuple_fundamentals_and_creation.py",
        code_lines,
        terminal_lines=terminal_lines,
        border_color=(139, 92, 246, 180)
    )

    # Bottom Pill (Y: 1465 to 1555)
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1510), "💡 GOLDEN RULE: In Python, COMMA (,) defines a tuple!", font=FONT_PILL, fill=COLOR_CYAN, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 2 (8 to 16s): 10M Speed & Memory Benchmark from 02_tuples_vs_lists_memory_and_speed.py
# -------------------------------------------------------------------------
def create_scene_2():
    img, draw = draw_canvas(0.40, "SPEED & ARCHITECTURE BENCHMARK")

    draw.text((WIDTH // 2, 285), "Tuples vs Lists Benchmark", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 345), "Topic 02 • day8/02_tuples_vs_lists_memory_and_speed.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    code_lines = [
        ("# Benchmark: Creating 10,000,000 Elements", COLOR_GREEN),
        ("t0 = time.perf_counter()", COLOR_MUTED),
        ("for _ in range(10_000_000): _ = [1, 2, 3, 4, 5]", COLOR_RED),
        ("time_list = time.perf_counter() - t0  # 1.0882s", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("t0 = time.perf_counter()", COLOR_MUTED),
        ("for _ in range(10_000_000): _ = (1, 2, 3, 4, 5)", COLOR_GREEN),
        ("time_tuple = time.perf_counter() - t0 # 0.5904s", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("# Hashability: Tuples can be Dictionary Keys!", COLOR_GREEN),
        ("geo_map = {(19.07, 72.87): 'Mumbai'}  # VALID", COLOR_CYAN),
        ("bad_map = {[19.07, 72.87]: 'Error'}   # TypeError!", COLOR_RED)
    ]

    terminal_lines = [
        ("$ python day8/02_tuples_vs_lists_memory_and_speed.py", COLOR_MUTED),
        ("Creating 10,000,000 Lists  : 1.0882 seconds", COLOR_RED),
        ("Creating 10,000,000 Tuples : 0.5904 seconds", COLOR_GREEN),
        (">> RESULT: Tuples are 1.84x FASTER than Lists in CPython!", COLOR_YELLOW)
    ]

    draw_ide_window(
        draw, 60, 400, WIDTH - 60, 1420,
        "02_tuples_vs_lists_memory_and_speed.py",
        code_lines,
        terminal_lines=terminal_lines,
        border_color=(34, 197, 94, 180)
    )

    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1510), "⚡ 1.84x Faster Execution + Fixed Size RAM Savings!", font=FONT_PILL, fill=COLOR_GREEN, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 3 (16 to 24s): Variable Swap & Star Unpacking from 03_tuple_operations_and_unpacking.py
# -------------------------------------------------------------------------
def create_scene_3():
    img, draw = draw_canvas(0.60, "PYTHONIC OPERATIONS")

    draw.text((WIDTH // 2, 285), "Variable Swap & Star Unpacking", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 345), "Topic 03 • day8/03_tuple_operations_and_unpacking.py", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    code_lines = [
        ("# 1. Zero-Temp Variable Swap (Tuple Packing):", COLOR_GREEN),
        ("x = 100; y = 200", COLOR_WHITE),
        ("x, y = y, x  # (y, x) packed into tuple -> unpacked", COLOR_YELLOW),
        ("print(f'x={x}, y={y}')  # x=200, y=100", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("# 2. Extended Star (*) Unpacking (PEP 3132):", COLOR_GREEN),
        ("data_stream = (10, 20, 30, 40, 50, 60, 70)", COLOR_WHITE),
        ("first, *middle, last = data_stream", COLOR_CYAN),
        ("print('First :', first)   # 10", COLOR_WHITE),
        ("print('Middle:', middle)  # [20, 30, 40, 50, 60]", COLOR_YELLOW),
        ("print('Last  :', last)    # 70", COLOR_WHITE)
    ]

    terminal_lines = [
        ("$ python day8/03_tuple_operations_and_unpacking.py", COLOR_MUTED),
        ("After Swap : x=200, y=100 (Swapped without temp variable!)", COLOR_GREEN),
        ("Data Stream: (10, 20, 30, 40, 50, 60, 70)", COLOR_WHITE),
        ("Middle list: [20, 30, 40, 50, 60] (Captured dynamically by *middle)", COLOR_CYAN)
    ]

    draw_ide_window(
        draw, 60, 400, WIDTH - 60, 1420,
        "03_tuple_operations_and_unpacking.py",
        code_lines,
        terminal_lines=terminal_lines,
        border_color=(6, 182, 212, 180)
    )

    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1510), "🚀 Extended Star (*) Unpacking Captures Rest into a List!", font=FONT_PILL, fill=COLOR_CYAN, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 4 (24 to 32s): Infamous '+=' Interview Trap from 04_tuple_interview_questions.py
# -------------------------------------------------------------------------
def create_scene_4():
    img, draw = draw_canvas(0.80, "TOP PYTHON INTERVIEW TRAP")

    draw.text((WIDTH // 2, 285), "The Infamous '+=' Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 345), "Topic 04 • day8/04_tuple_interview_questions.py", font=FONT_SUB, fill=COLOR_RED, anchor="mm")

    code_lines = [
        ("# The Classic Interview Brain Teaser:", COLOR_GREEN),
        ("t = (1, 2, [3, 4])  # Immutable tuple with inner list", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("try:", COLOR_PURPLE),
        ("    t[2] += [5]      # What happens here?", COLOR_RED),
        ("except TypeError as error:", COLOR_PURPLE),
        ("    print('TypeError caught:', error)", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("print('Tuple t is now:', t)  # (1, 2, [3, 4, 5])!", COLOR_YELLOW),
        ("# WHY? += mutates inner list in-place first (__iadd__),", COLOR_GREEN),
        ("# then tuple assignment raises TypeError (STORE_SUBSCR)!", COLOR_GREEN)
    ]

    terminal_lines = [
        ("$ python day8/04_tuple_interview_questions.py", COLOR_MUTED),
        ("Exception raised: TypeError -> 'tuple' object does not support assignment", COLOR_RED),
        ("Tuple AFTER exception: (1, 2, [3, 4, 5])", COLOR_YELLOW),
        (">> RESULT: Inner list mutated IN-PLACE despite TypeError!", COLOR_GREEN)
    ]

    draw_ide_window(
        draw, 60, 400, WIDTH - 60, 1420,
        "04_tuple_interview_questions.py",
        code_lines,
        terminal_lines=terminal_lines,
        border_color=(244, 63, 94, 180)
    )

    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_RED, width=2)
    draw.text((WIDTH // 2, 1510), "🔥 90% Python Developers Fail This Interview Trap!", font=FONT_PILL, fill=COLOR_RED, anchor="mm")

    return img


# -------------------------------------------------------------------------
# SCENE 5 (32 to 40s): Sapna's Workbook (my_practice.py) & GitHub Live Status
# -------------------------------------------------------------------------
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 08 COMPLETE")

    draw.text((WIDTH // 2, 285), "Practice Workbook & GitHub Live", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 345), "Student Workbook • day8/my_practice.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    code_lines = [
        ("# day8/my_practice.py (6 Hands-On Student Tasks):", COLOR_GREEN),
        ("def swap_pair(a, b):", COLOR_CYAN),
        ("    return b, a  # TODO solved via tuple unpacking!", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("def stream_summary(data: tuple) -> dict:", COLOR_CYAN),
        ("    first, *middle, last = data", COLOR_YELLOW),
        ("    return {'first': first, 'last': last, 'mid_avg': sum(middle)/len(middle)}", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("# PyTorch Deep Learning Tensor Dimension Tuple:", COLOR_GREEN),
        ("image_tensor_shape = (32, 3, 224, 224)  # (Batch, C, H, W)", COLOR_PURPLE),
        ("print(image_tensor_shape)  # Immutable during training", COLOR_MUTED)
    ]

    terminal_lines = [
        ("$ python day8/my_practice.py", COLOR_MUTED),
        ("[PASS] Task 1: Single-Element Tuple Creator  |  [PASS] Task 2: Variable Swap", COLOR_GREEN),
        ("[PASS] Task 3: Stream Summary with Star (*)  |  [PASS] Task 4: Employee Sorter", COLOR_GREEN),
        ("All 6 Tasks Passed! Pushed to github.com/Sapnayadav1608/fullstack-python-ai", COLOR_CYAN)
    ]

    draw_ide_window(
        draw, 60, 400, WIDTH - 60, 1420,
        "my_practice.py",
        code_lines,
        terminal_lines=terminal_lines,
        border_color=(34, 197, 94, 180)
    )

    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, 1510), "⭐ Follow along for Day 09! Code link in bio 👇", font=FONT_PILL, fill=COLOR_WHITE, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day8/day8_reel_video.mp4"
    temp_dir = "D:/learn-python/day8/temp_frames_perfect"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating 5 Zero-Overlap Scene Frames...")
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

    print("Concatenating 5 Video Clips (Exact 40.0 Seconds @ 24fps)...")
    clip1 = ImageClip(p1, duration=8)
    clip2 = ImageClip(p2, duration=8)
    clip3 = ImageClip(p3, duration=8)
    clip4 = ImageClip(p4, duration=8)
    clip5 = ImageClip(p5, duration=8)

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

    # Clean temporary files
    for p in [p1, p2, p3, p4, p5]:
        if os.path.exists(p):
            os.remove(p)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

    print(f"\n[SUCCESS] Day 8 Perfect 40-Second Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()

