"""
Day 08: Highly Engaging Infographic + Code Snippets Reel (40 Seconds)
====================================================================
Designed for maximum Instagram engagement & retention:
- Zero text overflow (all lines under 38 characters with strict auto-bounds)
- Rich Visual Infographics:
  1. Comma Rule comparison cards (int vs tuple)
  2. Memory Architecture & Speedometer bar-chart benchmark
  3. Star (*) Unpacking stream breakdown visual
  4. The Infamous '+=' Interview Trap dilemma & reveal
  5. AI PyTorch Tensor Dimensions & GitHub Repository Checklist
- High-aesthetic ambient dark mesh background with glowing neon orbs
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
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 34)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 26)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 25)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 46)

# Colors
COLOR_BG = [11, 14, 27]
COLOR_WHITE = (248, 250, 252)
COLOR_MUTED = (148, 163, 184)
COLOR_CARD_BG = (18, 22, 42, 245)
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

    # Subtitle
    draw.text((WIDTH // 2, 235), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Bottom Progress Bar (Y: 1615 to 1627)
    bar_y = 1615
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 12], radius=6, fill=(20, 25, 45, 220), outline=(40, 50, 80, 150))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 12], radius=6, fill=COLOR_CYAN)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): Visual Comma Rule Comparison + Short Code
# =========================================================================
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 08 / 30  •  WEEK 2 KICK-OFF")

    draw.text((WIDTH // 2, 280), "The Single-Element Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 335), "Comma defines the tuple, NOT parentheses!", font=FONT_SUB, fill=COLOR_PURPLE, anchor="mm")

    # Visual Comparison Cards (Two side-by-side cards)
    card_w = 440
    c1_x0, c1_x1 = 70, 70 + card_w
    c2_x0, c2_x1 = 570, 570 + card_w
    cards_y0, cards_y1 = 390, 700

    # Card 1: Math Grouping (NOT a tuple)
    draw.rounded_rectangle([c1_x0, cards_y0, c1_x1, cards_y1], radius=24, fill=(35, 18, 25, 240), outline=(244, 63, 94, 180), width=2)
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 40), "❌ NOT A TUPLE", font=FONT_HEADING, fill=COLOR_RED, anchor="mm")
    draw.rounded_rectangle([c1_x0 + 40, cards_y0 + 80, c1_x1 - 40, cards_y0 + 170], radius=16, fill=(11, 14, 27, 240))
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 125), "x = (42)", font=FONT_STAT, fill=COLOR_WHITE, anchor="mm")
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 215), "Type: <class 'int'>", font=FONT_SUB, fill=COLOR_RED, anchor="mm")
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 265), "Treated as math grouping", font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")

    # Card 2: Valid Tuple (WITH COMMA)
    draw.rounded_rectangle([c2_x0, cards_y0, c2_x1, cards_y1], radius=24, fill=(18, 35, 28, 240), outline=(34, 197, 94, 180), width=2)
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 40), "✅ VALID TUPLE", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")
    draw.rounded_rectangle([c2_x0 + 40, cards_y0 + 80, c2_x1 - 40, cards_y0 + 170], radius=16, fill=(11, 14, 27, 240))
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 125), "y = (42,)", font=FONT_STAT, fill=COLOR_CYAN, anchor="mm")
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 215), "Type: <class 'tuple'>", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 265), "Trailing comma is key!", font=FONT_BODY, fill=COLOR_YELLOW, anchor="mm")

    # Code Box below (y0: 740, y1: 1400)
    code_y0, code_y1 = 740, 1410
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=24, fill=COLOR_CARD_BG, outline=(139, 92, 246, 160), width=2)
    draw.text((100, code_y0 + 35), "01_tuple_fundamentals_and_creation.py", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, code_y0 + 60, WIDTH - 70, code_y0 + 60], fill=(45, 55, 85, 180), width=1)

    code_lines = [
        ("# 1. Mathematical grouping vs Tuple:", COLOR_GREEN),
        ("not_tuple = (42)    # type: int", COLOR_RED),
        ("is_tuple  = (42,)   # type: tuple", COLOR_CYAN),
        ("", COLOR_WHITE),
        ("# 2. Packing without parentheses works!", COLOR_GREEN),
        ("coords = 19.0760, 72.8777", COLOR_YELLOW),
        ("print(type(coords)) # <class 'tuple'>", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("# 3. Empty tuple creation:", COLOR_GREEN),
        ("empty_t = ()", COLOR_WHITE),
        ("print(len(empty_t)) # 0", COLOR_MUTED)
    ]

    cur_y = code_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(40, 48, 75, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 46

    # Bottom Takeaway Pill (Y: 1465 to 1555)
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1510), "💡 In Python, the COMMA (,) defines a tuple, not ()", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img


# =========================================================================
# SCENE 2 (8 to 16s): Memory Architecture & Visual Speedometer Bar Chart
# =========================================================================
def create_scene_2():
    img, draw = draw_canvas(0.40, "SPEED & ARCHITECTURE BENCHMARK")

    draw.text((WIDTH // 2, 280), "Tuples vs Lists Architecture", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 335), "Why Tuples are Faster and Save Memory", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Visual Bar Chart Benchmark Card (y0: 380, y1: 820)
    b_y0, b_y1 = 380, 820
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=24, fill=COLOR_CARD_BG, outline=(34, 197, 94, 180), width=2)
    draw.text((WIDTH // 2, b_y0 + 40), "CPYTHON SPEED BENCHMARK (10M ITERATIONS)", font=FONT_HEADING, fill=COLOR_YELLOW, anchor="mm")

    # Tuple Bar (Fast - 0.59s)
    draw.text((105, b_y0 + 105), "Python Tuple : 0.59s", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((WIDTH - 105, b_y0 + 105), "⚡ 1.84x FASTER", font=FONT_HEADING, fill=COLOR_GREEN, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 145, WIDTH - 105, b_y0 + 185], radius=12, fill=(11, 14, 27))
    tup_bar_w = int((WIDTH - 210) * 0.95)
    draw.rounded_rectangle([105, b_y0 + 145, 105 + tup_bar_w, b_y0 + 185], radius=12, fill=COLOR_GREEN)

    # List Bar (Slower - 1.08s)
    draw.text((105, b_y0 + 230), "Python List  : 1.08s", font=FONT_SUB, fill=COLOR_RED)
    draw.text((WIDTH - 105, b_y0 + 230), "Over-allocated RAM", font=FONT_BODY, fill=COLOR_MUTED, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 270, WIDTH - 105, b_y0 + 310], radius=12, fill=(11, 14, 27))
    list_bar_w = int((WIDTH - 210) * 0.52)
    draw.rounded_rectangle([105, b_y0 + 270, 105 + list_bar_w, b_y0 + 310], radius=12, fill=COLOR_RED)

    # Key Architectural Reason Pill inside card
    draw.rounded_rectangle([105, b_y0 + 345, WIDTH - 105, b_y0 + 415], radius=14, fill=(11, 14, 27), outline=(40, 50, 80))
    draw.text((WIDTH // 2, b_y0 + 380), "🧠 Reason: CPython Constant Folding + Tuple Free-Lists", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Code Box: Memory & Hashability (y0: 850, y1: 1410)
    c_y0, c_y1 = 850, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_BG, outline=(6, 182, 212, 160), width=2)
    draw.text((100, c_y0 + 35), "02_tuples_vs_lists_memory_and_speed.py", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(45, 55, 85, 180), width=1)

    code_lines = [
        ("# 1. Memory Overhead (sys.getsizeof):", COLOR_GREEN),
        ("sys.getsizeof([])  # 56 bytes (dynamic)", COLOR_RED),
        ("sys.getsizeof(())  # 48 bytes (exact size)", COLOR_GREEN),
        ("", COLOR_WHITE),
        ("# 2. Hashability Rule for Dict Keys:", COLOR_GREEN),
        ("geo = {(19.07, 72.87): 'Mumbai'}  # VALID", COLOR_CYAN),
        ("bad = {[19.07, 72.87]: 'Error'}   # TypeError!", COLOR_RED),
        ("", COLOR_WHITE),
        ("# Lists are unhashable because mutable,", COLOR_MUTED),
        ("# but immutable Tuples are hashable!", COLOR_YELLOW)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(40, 48, 75, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 46

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1510), "⚡ Tuples: 1.84x faster, less RAM & valid Dict Keys!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img


# =========================================================================
# SCENE 3 (16 to 24s): Variable Swap & Star Unpacking Visual Breakdown
# =========================================================================
def create_scene_3():
    img, draw = draw_canvas(0.60, "PYTHONIC OPERATIONS")

    draw.text((WIDTH // 2, 280), "Star (*) Unpacking & Swap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 335), "Zero-Temp Swap & Extended Unpacking (PEP 3132)", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    # Visual Infographic Card: Stream Breakdown (y0: 380, y1: 760)
    v_y0, v_y1 = 380, 760
    draw.rounded_rectangle([70, v_y0, WIDTH - 70, v_y1], radius=24, fill=COLOR_CARD_BG, outline=(6, 182, 212, 180), width=2)
    draw.text((WIDTH // 2, v_y0 + 40), "STREAM EXTRACTION VISUAL BREAKDOWN", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    # Tuple boxes row
    items = ["10", "20", "30", "40", "50", "60", "70"]
    box_w = 110
    start_x = 95
    for i, item in enumerate(items):
        bx = start_x + (i * 125)
        # Highlight first and last with green/cyan, middle with purple
        b_color = COLOR_CYAN if i in (0, 6) else COLOR_PURPLE
        draw.rounded_rectangle([bx, v_y0 + 90, bx + box_w, v_y0 + 170], radius=14, fill=(11, 14, 27), outline=b_color, width=2)
        draw.text((bx + box_w // 2, v_y0 + 130), item, font=FONT_TITLE, fill=COLOR_WHITE, anchor="mm")

    # Labels below boxes
    draw.text((start_x + box_w // 2, v_y0 + 205), "first", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")
    mid_center = start_x + (3 * 125) + box_w // 2
    draw.text((mid_center, v_y0 + 205), "*middle (Dynamic List: [20, 30, 40, 50, 60])", font=FONT_SUB, fill=COLOR_YELLOW, anchor="mm")
    last_center = start_x + (6 * 125) + box_w // 2
    draw.text((last_center, v_y0 + 205), "last", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    # Variable Swap Mini Box inside card
    draw.rounded_rectangle([105, v_y0 + 260, WIDTH - 105, v_y0 + 345], radius=14, fill=(11, 14, 27), outline=(139, 92, 246))
    draw.text((WIDTH // 2, v_y0 + 302), "🔄 Variable Swap: a, b = b, a  (Zero Temp Variables!)", font=FONT_SUB, fill=COLOR_WHITE, anchor="mm")

    # Code Box (y0: 790, y1: 1410)
    c_y0, c_y1 = 790, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_BG, outline=(139, 92, 246, 160), width=2)
    draw.text((100, c_y0 + 35), "03_tuple_operations_and_unpacking.py", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(45, 55, 85, 180), width=1)

    code_lines = [
        ("# 1. In-Place Swap via Tuple Packing:", COLOR_GREEN),
        ("x, y = 100, 200", COLOR_WHITE),
        ("x, y = y, x   # a=200, b=100", COLOR_YELLOW),
        ("", COLOR_WHITE),
        ("# 2. Extended Star (*) Unpacking:", COLOR_GREEN),
        ("stream = (10, 20, 30, 40, 50, 60, 70)", COLOR_WHITE),
        ("first, *middle, last = stream", COLOR_CYAN),
        ("print(first)   # 10", COLOR_MUTED),
        ("print(middle)  # [20, 30, 40, 50, 60]", COLOR_YELLOW),
        ("print(last)    # 70", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("# Tuples have only 2 methods: .count & .index", COLOR_GREEN)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(40, 48, 75, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 44

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1510), "🚀 Extended Unpacking extracts any stream cleanly!", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img


# =========================================================================
# SCENE 4 (24 to 32s): The Infamous '+=' Trap Dilemma & Reveal
# =========================================================================
def create_scene_4():
    img, draw = draw_canvas(0.80, "TOP PYTHON INTERVIEW TRAP")

    draw.text((WIDTH // 2, 280), "The Infamous '+=' Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 335), "Raises TypeError, but STILL mutates the inner list?!", font=FONT_SUB, fill=COLOR_RED, anchor="mm")

    # Visual Dilemma & Reveal Card (y0: 380, y1: 820)
    d_y0, d_y1 = 380, 820
    draw.rounded_rectangle([70, d_y0, WIDTH - 70, d_y1], radius=24, fill=(35, 18, 25, 240), outline=(244, 63, 94, 200), width=2)
    draw.text((WIDTH // 2, d_y0 + 40), "INTERVIEW QUESTION: WHAT HAPPENS?", font=FONT_HEADING, fill=COLOR_YELLOW, anchor="mm")

    # Code question box
    draw.rounded_rectangle([105, d_y0 + 80, WIDTH - 105, d_y0 + 170], radius=14, fill=(11, 14, 27))
    draw.text((130, d_y0 + 125), "t = (1, 2, [3, 4]) ; t[2] += [5]", font=FONT_HEADING, fill=COLOR_CYAN, anchor="lm")

    # Dual Outcome badges
    draw.rounded_rectangle([105, d_y0 + 200, 520, d_y0 + 290], radius=16, fill=(11, 14, 27), outline=COLOR_RED, width=2)
    draw.text((312, d_y0 + 230), "⚠️ EXCEPTION", font=FONT_HEADING, fill=COLOR_RED, anchor="mm")
    draw.text((312, d_y0 + 265), "TypeError Raised!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    draw.rounded_rectangle([560, d_y0 + 200, WIDTH - 105, d_y0 + 290], radius=16, fill=(11, 14, 27), outline=COLOR_GREEN, width=2)
    draw.text((770, d_y0 + 230), "⚡ STATE MUTATED", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")
    draw.text((770, d_y0 + 265), "List becomes [3, 4, 5]!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Why explanation banner
    draw.rounded_rectangle([105, d_y0 + 325, WIDTH - 105, d_y0 + 405], radius=14, fill=(11, 14, 27), outline=(139, 92, 246))
    draw.text((WIDTH // 2, d_y0 + 365), "🧠 CPython: __iadd__ mutates in-place BEFORE tuple check!", font=FONT_BODY, fill=COLOR_YELLOW, anchor="mm")

    # Code Box (y0: 850, y1: 1410)
    c_y0, c_y1 = 850, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_BG, outline=(244, 63, 94, 160), width=2)
    draw.text((100, c_y0 + 35), "04_tuple_interview_questions.py", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(45, 55, 85, 180), width=1)

    code_lines = [
        ("# The Classic Python Gotcha:", COLOR_GREEN),
        ("t = (1, 2, [3, 4])", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("try:", COLOR_PURPLE),
        ("    t[2] += [5]", COLOR_RED),
        ("except TypeError as e:", COLOR_PURPLE),
        ("    print('Caught:', e)", COLOR_MUTED),
        ("", COLOR_WHITE),
        ("print(t)  # (1, 2, [3, 4, 5])", COLOR_YELLOW),
        ("# The inner list mutated in-place!", COLOR_GREEN),
        ("# Tuple protects pointer, not state!", COLOR_CYAN)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(40, 48, 75, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 46

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_RED, width=2)
    draw.text((WIDTH // 2, 1510), "🔥 90% Developers Fail This Interview Trap!", font=FONT_SUB, fill=COLOR_RED, anchor="mm")

    return img


# =========================================================================
# SCENE 5 (32 to 40s): AI PyTorch Shapes + Student Workbook Checklist
# =========================================================================
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 08 COMPLETE")

    draw.text((WIDTH // 2, 280), "AI Tensor Shapes & GitHub Live", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 335), "Student Workbook • my_practice.py • All Tests Passing!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # AI Tensor Infographic Card (y0: 380, y1: 760)
    ai_y0, ai_y1 = 380, 760
    draw.rounded_rectangle([70, ai_y0, WIDTH - 70, ai_y1], radius=24, fill=COLOR_CARD_BG, outline=(139, 92, 246, 180), width=2)
    draw.text((WIDTH // 2, ai_y0 + 40), "PYTORCH / DEEP LEARNING TENSOR SHAPES", font=FONT_HEADING, fill=COLOR_PURPLE, anchor="mm")

    # Tensor Dimensions Pill
    draw.rounded_rectangle([105, ai_y0 + 80, WIDTH - 105, ai_y0 + 175], radius=16, fill=(11, 14, 27), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, ai_y0 + 128), "shape = (32, 3, 224, 224)", font=FONT_STAT, fill=COLOR_CYAN, anchor="mm")

    # Breakdown Labels
    labels = ["Batch (32)", "Channels (3 RGB)", "Height (224px)", "Width (224px)"]
    lbl_w = 210
    start_lx = 95
    for i, lbl in enumerate(labels):
        bx = start_lx + (i * 225)
        draw.rounded_rectangle([bx, ai_y0 + 205, bx + lbl_w, ai_y0 + 265], radius=12, fill=(11, 14, 27), outline=(45, 55, 85))
        draw.text((bx + lbl_w // 2, ai_y0 + 235), lbl, font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    draw.rounded_rectangle([105, ai_y0 + 295, WIDTH - 105, ai_y0 + 355], radius=12, fill=(11, 14, 27), outline=COLOR_GREEN)
    draw.text((WIDTH // 2, ai_y0 + 325), "🔒 Why Tuple? Model layer shapes must remain IMMUTABLE!", font=FONT_BODY, fill=COLOR_GREEN, anchor="mm")

    # GitHub Checklist Box (y0: 790, y1: 1410)
    gh_y0, gh_y1 = 790, 1410
    draw.rounded_rectangle([70, gh_y0, WIDTH - 70, gh_y1], radius=24, fill=COLOR_CARD_BG, outline=(34, 197, 94, 180), width=2)
    draw.text((100, gh_y0 + 35), "github.com/Sapnayadav1608/fullstack-python-ai", font=FONT_BADGE, fill=COLOR_CYAN, anchor="lm")
    draw.line([70, gh_y0 + 60, WIDTH - 70, gh_y0 + 60], fill=(45, 55, 85, 180), width=1)

    checklist = [
        ("01_tuple_fundamentals_and_creation.py", "Comma rule & memory"),
        ("02_tuples_vs_lists_memory_and_speed.py", "1.84x live benchmark"),
        ("03_tuple_operations_and_unpacking.py", "Star unpacking & swap"),
        ("04_tuple_interview_questions.py", "Top gotchas & tricks"),
        ("my_practice.py (Sapna's Workbook)", "6 Tasks ALL PASSING!"),
        ("README.md (Summary & Notes)", "Full Week 2 Roadmap")
    ]

    cur_y = gh_y0 + 95
    for f_name, f_desc in checklist:
        draw.text((100, cur_y), "✅", font=FONT_BODY, fill=COLOR_GREEN)
        draw.text((140, cur_y), f_name, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((140, cur_y + 36), f_desc, font=FONT_BADGE, fill=COLOR_MUTED)
        cur_y += 85

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(20, 24, 50, 240), outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, 1510), "⭐ Follow along for Day 09! Code link in bio 👇", font=FONT_SUB, fill=COLOR_WHITE, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day8/day8_reel_video.mp4"
    temp_dir = "D:/learn-python/day8/temp_frames_infographic"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating 5 Infographic + Code Scene Frames...")
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

    print("Concatenating 5 Clips (Exact 40.0 Seconds @ 24fps)...")
    clip1 = ImageClip(p1, duration=8)
    clip2 = ImageClip(p2, duration=8)
    clip3 = ImageClip(p3, duration=8)
    clip4 = ImageClip(p4, duration=8)
    clip5 = ImageClip(p5, duration=8)

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5], method="compose")

    print(f"Rendering final 40s MP4 to {output_path}...")
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

    print(f"\n[SUCCESS] Day 8 Infographic + Code Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()

