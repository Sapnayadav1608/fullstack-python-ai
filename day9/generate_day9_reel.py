"""
Day 09: Ultra-Aesthetic Infographic + Code Reel Generator (Warm Sunset / Mocha Palette)
======================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Color Palette:
- Deep Warm Espresso / Dark Mocha base [20, 16, 20]
- Top-Left Sunset Amber / Gold glow [245, 158, 11]
- Bottom-Right Sunset Coral / Rose glow [244, 63, 94]
- Warm Cream & Amber typography with soft glowing borders
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

# Warm Theme Color Palette
COLOR_BG_WARM = [22, 16, 20]            # Deep Dark Espresso/Mocha
COLOR_CARD_WARM = (30, 22, 28, 245)     # Translucent Warm Glass Card
COLOR_TEXT_MAIN = (255, 250, 242)       # Warm Crisp White
COLOR_TEXT_CREAM = (254, 243, 199)      # Warm Cream/Ivory
COLOR_TEXT_MUTED = (168, 150, 160)      # Muted Warm Grey
COLOR_AMBER = (245, 158, 11)            # Sunset Amber / Gold
COLOR_GOLD = (251, 191, 36)             # Warm Bright Gold
COLOR_ORANGE = (251, 146, 60)           # Warm Tangerine / Terracotta
COLOR_CORAL = (244, 63, 94)             # Warm Coral Sunset
COLOR_ROSE = (251, 113, 133)            # Soft Warm Rose
COLOR_GREEN = (52, 211, 153)            # Warm Mint / Emerald
COLOR_RED = (248, 113, 113)             # Warm Terracotta Red


def generate_warm_ambient_background():
    """Generates a warm, cozy dark-mode mesh gradient with amber and coral sunset orbs."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_WARM

    # Orb 1: Warm Amber / Sunset Gold glow (Top-Left)
    d1 = np.sqrt((x - 180)**2 + (y - 320)**2)
    w1 = (np.clip(1.0 - d1 / 750.0, 0, 1) ** 2.2)[:, :, None]
    base += w1 * np.array([245, 158, 11], dtype=np.float32) * 0.85

    # Orb 2: Sunset Coral / Rose ambient glow (Bottom-Right)
    d2 = np.sqrt((x - 900)**2 + (y - 1580)**2)
    w2 = (np.clip(1.0 - d2 / 800.0, 0, 1) ** 2.2)[:, :, None]
    base += w2 * np.array([244, 63, 94], dtype=np.float32) * 0.80

    # Orb 3: Soft Peach / Tangerine accent (Mid-Right)
    d3 = np.sqrt((x - 980)**2 + (y - 750)**2)
    w3 = (np.clip(1.0 - d3 / 550.0, 0, 1) ** 2.5)[:, :, None]
    base += w3 * np.array([251, 146, 60], dtype=np.float32) * 0.60

    # Warm Tech Grid Dots
    dot_mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    dot_mask[::50, ::50] = True
    base[dot_mask] = np.clip(base[dot_mask] + 40, 0, 255)

    base = np.clip(base, 0, 255).astype(np.uint8)
    return Image.fromarray(base)


CACHED_BG = generate_warm_ambient_background()


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 09 / 30"):
    """Paints top header, author branding, and warm glowing progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 155 to 215)
    badge_w, badge_h = 520, 58
    bx0 = (WIDTH - badge_w) // 2
    by0 = 155
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=29, fill=(35, 24, 30, 230), outline=(245, 158, 11, 200), width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_TEXT_CREAM, anchor="mm")

    # Subtitle
    draw.text((WIDTH // 2, 235), "SAPNA YADAV  |  FULL STACK PYTHON + AI", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Warm Glowing Progress Bar at Bottom (Y: 1615 to 1627)
    bar_y = 1615
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 12], radius=6, fill=(30, 22, 26, 220), outline=(60, 45, 55, 150))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 12], radius=6, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): The Empty Set Trap (Warm Comparison Cards)
# =========================================================================
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 09 / 30  •  SETS & HASH TABLES")

    draw.text((WIDTH // 2, 280), "The Empty Set Trap", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 335), "Topic 01 • day9/01_set_fundamentals_and_hashing.py", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Visual Comparison Cards
    card_w = 440
    c1_x0, c1_x1 = 70, 70 + card_w
    c2_x0, c2_x1 = 570, 570 + card_w
    cards_y0, cards_y1 = 390, 700

    # Card 1: {} is Dict (Warm Red/Terracotta)
    draw.rounded_rectangle([c1_x0, cards_y0, c1_x1, cards_y1], radius=24, fill=(38, 20, 24, 240), outline=(248, 113, 113, 180), width=2)
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 40), "❌ NOT A SET", font=FONT_HEADING, fill=COLOR_RED, anchor="mm")
    draw.rounded_rectangle([c1_x0 + 40, cards_y0 + 80, c1_x1 - 40, cards_y0 + 170], radius=16, fill=(18, 12, 16, 240))
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 125), "empty = {}", font=FONT_STAT, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 215), "Type: <class 'dict'>", font=FONT_SUB, fill=COLOR_RED, anchor="mm")
    draw.text(((c1_x0 + c1_x1) // 2, cards_y0 + 265), "Creates empty Dictionary!", font=FONT_BODY, fill=COLOR_TEXT_MUTED, anchor="mm")

    # Card 2: set() is Set (Warm Gold/Amber)
    draw.rounded_rectangle([c2_x0, cards_y0, c2_x1, cards_y1], radius=24, fill=(35, 26, 18, 240), outline=(245, 158, 11, 180), width=2)
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 40), "✅ REAL SET", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.rounded_rectangle([c2_x0 + 40, cards_y0 + 80, c2_x1 - 40, cards_y0 + 170], radius=16, fill=(18, 12, 16, 240))
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 125), "empty = set()", font=FONT_STAT, fill=COLOR_GOLD, anchor="mm")
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 215), "Type: <class 'set'>", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text(((c2_x0 + c2_x1) // 2, cards_y0 + 265), "True Empty Set Constructor", font=FONT_BODY, fill=COLOR_TEXT_CREAM, anchor="mm")

    # Code Box
    code_y0, code_y1 = 740, 1410
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=24, fill=COLOR_CARD_WARM, outline=(245, 158, 11, 140), width=2)
    draw.text((100, code_y0 + 35), "01_set_fundamentals_and_hashing.py", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="lm")
    draw.line([70, code_y0 + 60, WIDTH - 70, code_y0 + 60], fill=(55, 40, 48, 180), width=1)

    code_lines = [
        ("# 1. Automatic Deduplication:", COLOR_GREEN),
        ("skills = ['Py', 'JS', 'Py', 'Go']", COLOR_TEXT_MAIN),
        ("unique = set(skills)", COLOR_GOLD),
        ("print(unique)  # {'Py', 'JS', 'Go'}", COLOR_TEXT_CREAM),
        ("", COLOR_TEXT_MAIN),
        ("# 2. The Hashability Rule:", COLOR_GREEN),
        ("s = {10, 'AI', (1, 2)}  # Tuple OK!", COLOR_TEXT_MAIN),
        ("# s = {10, [1, 2]}     # TypeError!", COLOR_RED),
        ("", COLOR_TEXT_MAIN),
        ("# 3. Boolean Equality Collision:", COLOR_GREEN),
        ("bool_set = {1, True}   # {1}", COLOR_ORANGE),
        ("print(1 == True)       # True!", COLOR_TEXT_MUTED)
    ]

    cur_y = code_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_TEXT_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 40, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 44

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(35, 24, 30, 240), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1510), "💡 In Python, always use set() for empty sets, not {}", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 2 (8 to 16s): Live 4,400x Speedup Bar Chart (Warm Gold & Terracotta)
# =========================================================================
def create_scene_2():
    img, draw = draw_canvas(0.40, "SPEED & ARCHITECTURE BENCHMARK")

    draw.text((WIDTH // 2, 280), "4,400x Faster Search Speed", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 335), "Topic 03 • 1,000,000 Elements Live Benchmark", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Visual Bar Chart Benchmark Card
    b_y0, b_y1 = 380, 820
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=24, fill=COLOR_CARD_WARM, outline=(52, 211, 153, 180), width=2)
    draw.text((WIDTH // 2, b_y0 + 40), "MEMBERSHIP SEARCH IN 1,000,000 ELEMENTS", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Set Bar (0.0020 ms)
    draw.text((105, b_y0 + 105), "Python Set (O(1))  : 0.002 ms", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((WIDTH - 105, b_y0 + 105), "⚡ 4,466x FASTER", font=FONT_HEADING, fill=COLOR_GOLD, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 145, WIDTH - 105, b_y0 + 185], radius=12, fill=(18, 12, 16))
    set_bar_w = int((WIDTH - 210) * 0.95)
    draw.rounded_rectangle([105, b_y0 + 145, 105 + set_bar_w, b_y0 + 185], radius=12, fill=COLOR_GREEN)

    # List Bar (8.93 ms)
    draw.text((105, b_y0 + 230), "Python List (O(N)) : 8.931 ms", font=FONT_SUB, fill=COLOR_RED)
    draw.text((WIDTH - 105, b_y0 + 230), "Scans 1M items", font=FONT_BODY, fill=COLOR_TEXT_MUTED, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 270, WIDTH - 105, b_y0 + 310], radius=12, fill=(18, 12, 16))
    list_bar_w = int((WIDTH - 210) * 0.15)
    draw.rounded_rectangle([105, b_y0 + 270, 105 + list_bar_w, b_y0 + 310], radius=12, fill=COLOR_RED)

    # Explanation banner inside
    draw.rounded_rectangle([105, b_y0 + 345, WIDTH - 105, b_y0 + 415], radius=14, fill=(18, 12, 16), outline=(60, 45, 55))
    draw.text((WIDTH // 2, b_y0 + 380), "🧠 Hash Table calculates bucket directly in O(1) time!", font=FONT_BODY, fill=COLOR_TEXT_CREAM, anchor="mm")

    # Code Box
    c_y0, c_y1 = 850, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_WARM, outline=(245, 158, 11, 140), width=2)
    draw.text((100, c_y0 + 35), "03_set_performance_and_frozenset.py", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(55, 40, 48, 180), width=1)

    code_lines = [
        ("# 1. Benchmark Loop in CPython:", COLOR_GREEN),
        ("sample_list = list(range(1_000_000))", COLOR_TEXT_MAIN),
        ("sample_set  = set(sample_list)", COLOR_GOLD),
        ("target in sample_set  # 0.002ms (O(1))", COLOR_GREEN),
        ("target in sample_list # 8.931ms (O(N))", COLOR_RED),
        ("", COLOR_TEXT_MAIN),
        ("# 2. Set Comprehension Filtering:", COLOR_GREEN),
        ("tags = [' python ', 'AI', 'PYTHON']", COLOR_TEXT_MAIN),
        ("clean = {t.strip().lower() for t in tags}", COLOR_ORANGE),
        ("print(clean) # {'python', 'ai'}", COLOR_TEXT_CREAM)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_TEXT_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 40, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 44

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(35, 24, 30, 240), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1510), "⚡ Sets perform O(1) instantaneous lookups!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img


# =========================================================================
# SCENE 3 (16 to 24s): Mathematical Set Theory (Warm Sunset Matrix)
# =========================================================================
def create_scene_3():
    img, draw = draw_canvas(0.60, "MATHEMATICAL SET THEORY")

    draw.text((WIDTH // 2, 280), "Set Theory & RBAC Control", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 335), "Topic 02 • day9/02_mathematical_set_operations.py", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    # Visual 4-Operation Grid
    v_y0, v_y1 = 380, 760
    draw.rounded_rectangle([70, v_y0, WIDTH - 70, v_y1], radius=24, fill=COLOR_CARD_WARM, outline=(251, 146, 60, 180), width=2)
    draw.text((WIDTH // 2, v_y0 + 40), "THE 4 PILLARS OF MATHEMATICAL SET OPERATIONS", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # 4 Cards with Warm Accents
    ops = [
        ("UNION (A | B)", "Combines all unique elements", COLOR_GOLD),
        ("INTERSECTION (A & B)", "Finds shared common elements", COLOR_GREEN),
        ("DIFFERENCE (A - B)", "In set A, but NOT in set B", COLOR_RED),
        ("SYMMETRIC DIFF (A ^ B)", "In either, but NOT both", COLOR_ROSE)
    ]

    for i, (title, desc, col) in enumerate(ops):
        ox = 105 if i % 2 == 0 else 555
        oy = v_y0 + 80 if i < 2 else v_y0 + 215
        draw.rounded_rectangle([ox, oy, ox + 420, oy + 115], radius=16, fill=(18, 12, 16), outline=col, width=2)
        draw.text((ox + 25, oy + 35), title, font=FONT_SUB, fill=col)
        draw.text((ox + 25, oy + 75), desc, font=FONT_BADGE, fill=COLOR_TEXT_CREAM)

    # Real-world RBAC Code Box
    c_y0, c_y1 = 790, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_WARM, outline=(245, 158, 11, 140), width=2)
    draw.text((100, c_y0 + 35), "Real-World Backend: RBAC Permission Validator", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(55, 40, 48, 180), width=1)

    code_lines = [
        ("# Define endpoint required permissions:", COLOR_GREEN),
        ("required = {'read', 'write', 'delete'}", COLOR_TEXT_MAIN),
        ("", COLOR_TEXT_MAIN),
        ("# User permission check via issubset():", COLOR_GREEN),
        ("admin = {'read', 'write', 'delete', 'export'}", COLOR_GOLD),
        ("print(required.issubset(admin)) # True", COLOR_GREEN),
        ("", COLOR_TEXT_MAIN),
        ("guest = {'read'}", COLOR_TEXT_MAIN),
        ("print(required.issubset(guest)) # False", COLOR_RED),
        ("missing = required - guest  # {'write', 'delete'}", COLOR_ORANGE)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_TEXT_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 40, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 46

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(35, 24, 30, 240), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, 1510), "🚀 Elegant Set Math for Access Control & Security", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    return img


# =========================================================================
# SCENE 4 (24 to 32s): LeetCode #128 - Longest Consecutive Sequence
# =========================================================================
def create_scene_4():
    img, draw = draw_canvas(0.80, "TOP LEETCODE INTERVIEW QUESTION")

    draw.text((WIDTH // 2, 280), "Longest Consecutive Sequence", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 335), "LeetCode #128 • Solved in O(N) Time using Hash Set", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Sequence Visual Blocks
    s_y0, s_y1 = 380, 760
    draw.rounded_rectangle([70, s_y0, WIDTH - 70, s_y1], radius=24, fill=COLOR_CARD_WARM, outline=(251, 191, 36, 180), width=2)
    draw.text((WIDTH // 2, s_y0 + 40), "INPUT: [100, 4, 200, 1, 3, 2]  ->  LONGEST: 4", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Consecutive chain boxes: 1 -> 2 -> 3 -> 4
    chain = ["1", "➔", "2", "➔", "3", "➔", "4"]
    start_cx = 100
    for i, ch in enumerate(chain):
        bx = start_cx + (i * 125)
        if ch == "➔":
            draw.text((bx + 35, s_y0 + 130), ch, font=FONT_TITLE, fill=COLOR_ORANGE, anchor="mm")
        else:
            draw.rounded_rectangle([bx, s_y0 + 90, bx + 90, s_y0 + 175], radius=14, fill=(18, 12, 16), outline=COLOR_GREEN, width=2)
            draw.text((bx + 45, s_y0 + 132), ch, font=FONT_TITLE, fill=COLOR_TEXT_MAIN, anchor="mm")

    # Sequence Length Badge inside card
    draw.rounded_rectangle([105, s_y0 + 215, WIDTH - 105, s_y0 + 340], radius=16, fill=(18, 12, 16), outline=COLOR_GOLD)
    draw.text((WIDTH // 2, s_y0 + 255), "⚡ O(N) Trick: Only start chain if (num - 1) NOT in set!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 300), "Sorting takes O(N log N) - Set solves it in Linear O(N)!", font=FONT_BODY, fill=COLOR_TEXT_CREAM, anchor="mm")

    # Code Box
    c_y0, c_y1 = 790, 1410
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=24, fill=COLOR_CARD_WARM, outline=(251, 191, 36, 140), width=2)
    draw.text((100, c_y0 + 35), "04_set_interview_questions.py", font=FONT_BADGE, fill=COLOR_TEXT_MUTED, anchor="lm")
    draw.line([70, c_y0 + 60, WIDTH - 70, c_y0 + 60], fill=(55, 40, 48, 180), width=1)

    code_lines = [
        ("def longest_consecutive(nums):", COLOR_GOLD),
        ("    num_set = set(nums)", COLOR_TEXT_MAIN),
        ("    longest = 0", COLOR_TEXT_MAIN),
        ("", COLOR_TEXT_MAIN),
        ("    for num in num_set:", COLOR_ORANGE),
        ("        # Check if start of streak", COLOR_GREEN),
        ("        if (num - 1) not in num_set:", COLOR_GOLD),
        ("            curr, streak = num, 1", COLOR_TEXT_MAIN),
        ("            while (curr + 1) in num_set:", COLOR_TEXT_CREAM),
        ("                curr += 1; streak += 1", COLOR_TEXT_MAIN),
        ("            longest = max(longest, streak)", COLOR_GREEN),
        ("    return longest  # Output: 4", COLOR_GOLD)
    ]

    cur_y = c_y0 + 95
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_TEXT_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 40, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 44

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(35, 24, 30, 240), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1510), "🔥 LeetCode #128 Solved in Strictly O(N) Linear Time!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 5 (32 to 40s): AI Tokenizer Vocabulary & GitHub Checklist
# =========================================================================
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 09 COMPLETE")

    draw.text((WIDTH // 2, 280), "AI Vocabulary & GitHub Live", font=FONT_HERO, fill=COLOR_TEXT_MAIN, anchor="mm")
    draw.text((WIDTH // 2, 335), "Student Workbook • my_practice.py • All Tests Passing!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # AI NLP Card
    ai_y0, ai_y1 = 380, 760
    draw.rounded_rectangle([70, ai_y0, WIDTH - 70, ai_y1], radius=24, fill=COLOR_CARD_WARM, outline=(245, 158, 11, 180), width=2)
    draw.text((WIDTH // 2, ai_y0 + 40), "AI & NLP: FAST TOKEN VOCABULARY DEDUPLICATION", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Stopwords filter equation
    draw.rounded_rectangle([105, ai_y0 + 80, WIDTH - 105, ai_y0 + 175], radius=16, fill=(18, 12, 16), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, ai_y0 + 128), "vocab = set(tokens) - stopwords", font=FONT_STAT, fill=COLOR_GOLD, anchor="mm")

    # NLP details
    draw.rounded_rectangle([105, ai_y0 + 205, WIDTH - 105, ai_y0 + 345], radius=14, fill=(18, 12, 16), outline=(60, 45, 55))
    draw.text((WIDTH // 2, ai_y0 + 245), "⚡ Instantaneous O(1) stopword elimination", font=FONT_SUB, fill=COLOR_TEXT_CREAM, anchor="mm")
    draw.text((WIDTH // 2, ai_y0 + 300), "🔒 frozenset enables Sets as Dictionary Keys!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # GitHub Checklist Box
    gh_y0, gh_y1 = 790, 1410
    draw.rounded_rectangle([70, gh_y0, WIDTH - 70, gh_y1], radius=24, fill=COLOR_CARD_WARM, outline=(52, 211, 153, 180), width=2)
    draw.text((100, gh_y0 + 35), "github.com/Sapnayadav1608/fullstack-python-ai", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, gh_y0 + 60, WIDTH - 70, gh_y0 + 60], fill=(55, 40, 48, 180), width=1)

    checklist = [
        ("01_set_fundamentals_and_hashing.py", "Empty set trap & hashing"),
        ("02_mathematical_set_operations.py", "Union, Intersection, RBAC"),
        ("03_set_performance_and_frozenset.py", "4,400x speedup & frozenset"),
        ("04_set_interview_questions.py", "LeetCode #128 in O(N)"),
        ("my_practice.py (Sapna's Workbook)", "6 Tasks ALL PASSING!"),
        ("README.md (Summary & Notes)", "Full Day 9 Roadmap")
    ]

    cur_y = gh_y0 + 95
    for f_name, f_desc in checklist:
        draw.text((100, cur_y), "✅", font=FONT_BODY, fill=COLOR_GREEN)
        draw.text((140, cur_y), f_name, font=FONT_BODY, fill=COLOR_TEXT_MAIN)
        draw.text((140, cur_y + 36), f_desc, font=FONT_BADGE, fill=COLOR_TEXT_MUTED)
        cur_y += 85

    # Bottom Pill
    draw.rounded_rectangle([80, 1465, WIDTH - 80, 1555], radius=24, fill=(35, 24, 30, 240), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1510), "⭐ Follow along for Day 10! Code link in bio 👇", font=FONT_SUB, fill=COLOR_TEXT_CREAM, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day9/day9_reel_video.mp4"
    temp_dir = "D:/learn-python/day9/temp_frames_warm"
    os.makedirs(temp_dir, exist_ok=True)

    print("Generating 5 Warm Sunset / Mocha Scene Frames for Day 9...")
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

    print(f"Rendering warm final 40s MP4 to {output_path}...")
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

    print(f"\n[SUCCESS] Day 9 Warm Reel Video Generated: {output_path}")


if __name__ == "__main__":
    generate_video()
