"""
Day 10: Ultra-Aesthetic Infographic + Code Reel Generator (Deep Dark + Warm Shade)
===================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Specifications:
- 1080x1920 Vertical Aspect Ratio (Instagram Reel / Shorts)
- Exact 40.0 Seconds Duration (5 Scenes x 8s @ 24fps)
- Deep Dark Obsidian Base (#0C090C) with Subtle Warm Amber/Ember Glow
- High Readability Bold Typography (Segoe UI Bold + Consolas Bold)
- 100% Pixel-Locked Layout & Guaranteed Zero Text Overflow
- No personal name (Generic Track Branding)
- Output paths: D:/learn-python/day10 & D:/fullstack-python-ai/day10
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

# High-Contrast Bold Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 54)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 42)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 34)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 25)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 44)

# Deep Dark Base with Warm Shade Palette
COLOR_BG_DARK = np.array([12, 9, 12], dtype=np.float32)   # Deep Obsidian Dark
COLOR_CARD_BG = (18, 14, 18, 252)                         # Deep Dark Glass Card
COLOR_INNER_BG = (10, 7, 10, 255)                         # Pitch Black Inner Container

# Vibrant Warm Highlight Colors
COLOR_WHITE = (255, 253, 248)           # Crisp Warm White
COLOR_CREAM = (254, 243, 199)           # Warm Ivory
COLOR_MUTED = (165, 150, 160)           # High-visibility Warm Slate Grey
COLOR_AMBER = (245, 158, 11)            # Sunset Amber
COLOR_GOLD = (251, 191, 36)             # Radiant Gold
COLOR_ORANGE = (251, 146, 60)           # Tangerine / Warm Terracotta
COLOR_CORAL = (244, 63, 94)             # Warm Coral Sunset
COLOR_ROSE = (251, 113, 133)            # Soft Warm Rose
COLOR_GREEN = (52, 211, 153)            # Neon Emerald
COLOR_RED = (248, 113, 113)             # Vivid Warning Coral/Red


def generate_dark_warm_background():
    """Generates a rich, deep dark obsidian canvas with subtle warm amber atmospheric glow."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    # Subtle Warm Amber Glow (Top-Left Halo)
    d1 = np.sqrt((x - 150)**2 + (y - 200)**2)
    w1 = (np.clip(1.0 - d1 / 650.0, 0, 1) ** 3.0)[:, :, None]
    base += w1 * np.array([217, 119, 6], dtype=np.float32) * 0.40

    # Subtle Warm Ember Accent (Bottom-Right)
    d2 = np.sqrt((x - 930)**2 + (y - 1700)**2)
    w2 = (np.clip(1.0 - d2 / 700.0, 0, 1) ** 3.0)[:, :, None]
    base += w2 * np.array([194, 65, 12], dtype=np.float32) * 0.35

    # Subtle Warm Mid Accent
    d3 = np.sqrt((x - 950)**2 + (y - 750)**2)
    w3 = (np.clip(1.0 - d3 / 500.0, 0, 1) ** 3.2)[:, :, None]
    base += w3 * np.array([180, 83, 9], dtype=np.float32) * 0.25

    # Refined Micro Dark Grid
    dot_mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    dot_mask[::50, ::50] = True
    base[dot_mask] = np.clip(base[dot_mask] + 16, 0, 255)

    base = np.clip(base, 0, 255).astype(np.uint8)
    return Image.fromarray(base)


CACHED_BG = generate_dark_warm_background()


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 10 / 30"):
    """Paints top header, track branding (NO PERSONAL NAME), and glowing progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 125 to 181) - Shifted up for Instagram safe zones
    badge_w, badge_h = 560, 56
    bx0 = (WIDTH - badge_w) // 2
    by0 = 125
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=28, fill=(24, 16, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_CREAM, anchor="mm")

    # Subtitle Branding (NO PERSONAL NAME)
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar (Y: 1350 to 1360) - Positioned safely above caption zone
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(20, 14, 18, 240), outline=(55, 38, 48, 180))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): ROADMAP & INTRO HOOK (Double Digits Milestone)
# =========================================================================
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 10 / 30  •  ROADMAP & INTRO")

    draw.text((WIDTH // 2, 246), "Python Dictionaries & Hash Maps", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Hitting Double Digits • Core Data Structure Track", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: 4 Sequential Modules of Day 10 (Y: 330 to 660)
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DAY 10 COMPLETE 4-MODULE ROADMAP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("MOD 01", "CPython Compact Hash Table & Key Rules", COLOR_GREEN),
        ("MOD 02", "Safe .get(), .setdefault() & Pipe Union |", COLOR_ORANGE),
        ("MOD 03", "5,000x Speedup Benchmark & TTL Cache", COLOR_GOLD),
        ("MOD 04", "Two Sum LeetCode #1 & FAANG Hash Maps", COLOR_CORAL)
    ]

    p_y = card_y0 + 64
    for mod_tag, mod_desc, col in modules:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 54], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((125, p_y + 14), mod_tag, font=FONT_SUB, fill=col)
        draw.text((250, p_y + 16), mod_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 66

    # Bottom Code Box: The fromkeys Reference Trap (Y: 680 to 1230)
    code_y0, code_y1 = 680, 1230
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, code_y0 + 30), "The Famous 'fromkeys' Reference Bug", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, code_y0 + 52, WIDTH - 70, code_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("# 1. Normal dictionary creation:", COLOR_GREEN),
        ("user = {'name': 'Alex', 'role': 'AI'}", COLOR_WHITE),
        ("print(type(user))  # <class 'dict'> ✨", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# 2. The dangerous fromkeys reference bug:", COLOR_CORAL),
        ("teams = dict.fromkeys(['A', 'B'], [])", COLOR_WHITE),
        ("teams['A'].append('Alice')", COLOR_WHITE),
        ("print(teams['B']) # ['Alice'] 🤯 (Shared!)", COLOR_RED),
        ("", COLOR_WHITE),
        ("# 3. The Pythonic Comprehension Fix:", COLOR_GREEN),
        ("clean = {k: [] for k in ['A', 'B']}  # Safe ✅", COLOR_GREEN)
    ]

    cur_y = code_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 42

    # Bottom Pill (Y: 1250 to 1330) - 100% Above Instagram Caption Zone!
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Welcome to Day 10! Let's master Hash Maps! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 (Compact Hash Table & Hashability)
# =========================================================================
def create_scene_2():
    img, draw = draw_canvas(0.40, "DAY 10 / 30  •  MODULE 01")

    draw.text((WIDTH // 2, 246), "Compact Hash Table Architecture", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 01 • day10/01_dict_fundamentals_and_memory.py", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: CPython Compact Table Diagram (Y: 330 to 660)
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 30), "CPYTHON 3.6+ COMPACT DICTIONARY DESIGN", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # 1. Sparse Indices Table
    draw.rounded_rectangle([105, card_y0 + 64, WIDTH - 105, card_y0 + 150], radius=12, fill=COLOR_INNER_BG, outline=COLOR_ORANGE, width=2)
    draw.text((130, card_y0 + 86), "1. Sparse Indices Array  : [ -1,  0, -1,  1, -1,  2 ]", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((130, card_y0 + 118), "   Tiny 1-byte indices save 25% RAM compared to Python 3.5!", font=FONT_BODY, fill=COLOR_CREAM)

    # 2. Dense Entries Array
    draw.rounded_rectangle([105, card_y0 + 165, WIDTH - 105, card_y0 + 315], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((130, card_y0 + 185), "2. Dense Entries Array   : 0 ➔ ('name', 'Alex')", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 218), "                           1 ➔ ('role', 'AI Engineer')", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 251), "                           2 ➔ ('tier', 'PRO')", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 282), "   ✨ Guarantees Insertion Order as official Language Spec!", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Code Box: The Key Hashability Rule (Y: 680 to 1230)
    code_y0, code_y1 = 680, 1230
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, code_y0 + 30), "The Key Hashability Rule: What can be a key?", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, code_y0 + 52, WIDTH - 70, code_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("# 1. Immutable types are HASHABLE (Allowed):", COLOR_GREEN),
        ("valid_dict = {", COLOR_WHITE),
        ("    101: 'Integer Key',", COLOR_WHITE),
        ("    'role': 'String Key',", COLOR_WHITE),
        ("    (10, 20): 'Tuple Key OK! ✅',", COLOR_GOLD),
        ("    frozenset(['r', 'w']): 'Frozenset OK! ✅'", COLOR_GOLD),
        ("}", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("# 2. Mutable types CANNOT be keys:", COLOR_CORAL),
        ("# bad = {[1, 2]: 'List Key'}  # TypeError! ❌", COLOR_RED),
        ("print('Lists mutate -> No fixed hash() value!')", COLOR_MUTED)
    ]

    cur_y = code_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 40

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "💡 Only immutable hashable objects can be dict keys!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 3 (16 to 24s): MODULE 02 (CRUD, .setdefault() & Union |)
# =========================================================================
def create_scene_3():
    img, draw = draw_canvas(0.60, "DAY 10 / 30  •  MODULE 02")

    draw.text((WIDTH // 2, 246), "CRUD, .setdefault() & Union (|)", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 02 • day10/02_dict_methods_and_crud.py", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    # Top Card: 4 Method Feature Grid (Y: 330 to 660)
    v_y0, v_y1 = 330, 660
    draw.rounded_rectangle([70, v_y0, WIDTH - 70, v_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, v_y0 + 32), "ADVANCED DICTIONARY METHODS & OPERATORS", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    features = [
        ("SAFE .get()", "Avoids KeyError with fallback", COLOR_GOLD),
        ("SETDEFAULT", "One-step read or initialize", COLOR_GREEN),
        ("UNION PIPE (|)", "Python 3.9+ clean merge", COLOR_ORANGE),
        ("DICT VIEWS (&)", "Direct set operations on keys", COLOR_ROSE)
    ]

    for i, (title, desc, col) in enumerate(features):
        ox = 105 if i % 2 == 0 else 555
        oy = v_y0 + 68 if i < 2 else v_y0 + 192
        draw.rounded_rectangle([ox, oy, ox + 420, oy + 105], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((ox + 25, oy + 25), title, font=FONT_SUB, fill=col)
        draw.text((ox + 25, oy + 64), desc, font=FONT_BADGE, fill=COLOR_CREAM)

    # Bottom Code Box: Python 3.9+ Union & setdefault (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, c_y0 + 30), "Python 3.9+ Union Operator (|) & Safe Retrieval", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("# 1. Safe access vs KeyError:", COLOR_GREEN),
        ("user = {'id': 101, 'role': 'PRO'}", COLOR_WHITE),
        ("email = user.get('email', 'N/A') # Safe fallback", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# 2. Python 3.9+ Pipe Union Operator '|':", COLOR_GREEN),
        ("base_cfg = {'port': 8000, 'timeout': 30}", COLOR_WHITE),
        ("prod_cfg = {'port': 443, 'debug': False}", COLOR_WHITE),
        ("merged   = base_cfg | prod_cfg # Non-destructive", COLOR_ORANGE),
        ("print(merged['port']) # 443 (Overridden!)", COLOR_GREEN),
        ("", COLOR_WHITE),
        ("# 3. Atomic .setdefault() Grouping:", COLOR_GREEN),
        ("clusters.setdefault('eu-west', []).append('node-1')", COLOR_CREAM)
    ]

    cur_y = c_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 39

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, 1290), "🚀 Python 3.9+ '|' merges dicts cleanly without mutating!", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    return img


# =========================================================================
# SCENE 4 (24 to 32s): MODULE 03 (5,000x Speedup & TTL Cache)
# =========================================================================
def create_scene_4():
    img, draw = draw_canvas(0.80, "DAY 10 / 30  •  MODULE 03")

    draw.text((WIDTH // 2, 246), "5,000x Faster Search & TTL Cache", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 03 • day10/03_dict_internals_and_performance.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Top Card: 1,000,000 Items Benchmark Bar Chart (Y: 330 to 660)
    b_y0, b_y1 = 330, 660
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, b_y0 + 30), "MEMBERSHIP LOOKUP IN 1,000,000 KEY-VALUE ITEMS", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Dict Bar (0.0090 ms)
    draw.text((105, b_y0 + 72), "Python Dict (O(1)) : 0.009 ms", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((WIDTH - 105, b_y0 + 72), "⚡ 4,986x FASTER", font=FONT_HEADING, fill=COLOR_GOLD, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 110, WIDTH - 105, b_y0 + 145], radius=10, fill=COLOR_INNER_BG)
    dict_bar_w = int((WIDTH - 210) * 0.95)
    draw.rounded_rectangle([105, b_y0 + 110, 105 + dict_bar_w, b_y0 + 145], radius=10, fill=COLOR_GREEN)

    # List Bar (44.87 ms)
    draw.text((105, b_y0 + 168), "Python List (O(N)) : 44.87 ms", font=FONT_SUB, fill=COLOR_RED)
    draw.text((WIDTH - 105, b_y0 + 168), "Scans 1M tuples", font=FONT_BODY, fill=COLOR_MUTED, anchor="ra")
    draw.rounded_rectangle([105, b_y0 + 206, WIDTH - 105, b_y0 + 241], radius=10, fill=COLOR_INNER_BG)
    list_bar_w = int((WIDTH - 210) * 0.12)
    draw.rounded_rectangle([105, b_y0 + 206, 105 + list_bar_w, b_y0 + 241], radius=10, fill=COLOR_RED)

    # Explanation banner inside
    draw.rounded_rectangle([105, b_y0 + 260, WIDTH - 105, b_y0 + 315], radius=10, fill=COLOR_INNER_BG, outline=(55, 38, 48))
    draw.text((WIDTH // 2, b_y0 + 288), "🧠 Hash Table bucket calculated directly in O(1) time!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Code Box: In-Memory TTL Cache (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, c_y0 + 30), "Real-World Backend: In-Memory TTL Cache System", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("class SimpleTTLCache:", COLOR_GOLD),
        ("    def set(self, key, value, ttl_secs):", COLOR_GREEN),
        ("        expiry = time.time() + ttl_secs", COLOR_WHITE),
        ("        self._store[key] = (value, expiry)", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("    def get(self, key, default=None):", COLOR_GREEN),
        ("        if key not in self._store:", COLOR_WHITE),
        ("            return default", COLOR_MUTED),
        ("        val, expiry = self._store[key]", COLOR_WHITE),
        ("        if time.time() > expiry:  # Expired!", COLOR_CORAL),
        ("            del self._store[key]  # Auto purge", COLOR_RED),
        ("            return default", COLOR_MUTED),
        ("        return val  # Fresh O(1) cache hit! ✨", COLOR_GREEN)
    ]

    cur_y = c_y0 + 72
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 35

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1290), "⚡ Dictionaries power high-speed in-memory caches!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img


# =========================================================================
# SCENE 5 (32 to 40s): MODULE 04 & RECAP (Two Sum & Day 10 Checklist)
# =========================================================================
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 10 / 30  •  MODULE 04 & RECAP")

    draw.text((WIDTH // 2, 246), "Two Sum (LeetCode #1) in O(N)", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 04 • day10/04_dict_interview_questions.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Top Card: Two Sum Matching Visualizer (Y: 330 to 660)
    s_y0, s_y1 = 330, 660
    draw.rounded_rectangle([70, s_y0, WIDTH - 70, s_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 32), "LEETCODE #1: TWO SUM IN LINEAR O(N) TIME", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Array boxes: [ 2 ] + [ 7 ] = 9
    draw.rounded_rectangle([105, s_y0 + 70, WIDTH - 105, s_y0 + 165], radius=14, fill=COLOR_INNER_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, s_y0 + 102), "INPUT: [2, 7, 11, 15]  |  TARGET: 9", font=FONT_SUB, fill=COLOR_CREAM, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 138), "Target (9) - Num (7) = Complement (2) Found at index 0!", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")

    # Complexity Badge inside card
    draw.rounded_rectangle([105, s_y0 + 180, WIDTH - 105, s_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD)
    draw.text((WIDTH // 2, s_y0 + 218), "⚡ Hash Map turns O(N^2) brute force into O(N) linear time!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 265), "Single-pass lookup solves Two Sum in 1 single traversal!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Combined Card: Day 10 Modules & Practice Checklist (Y: 680 to 1230)
    b_y0, b_y1 = 680, 1230
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, b_y0 + 30), "Day 10 Modules & Student Workbook Checklist", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, b_y0 + 52, WIDTH - 70, b_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Key equation banner
    draw.rounded_rectangle([100, b_y0 + 70, WIDTH - 100, b_y0 + 155], radius=14, fill=COLOR_INNER_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, b_y0 + 98), "complement = target - num  # O(1) Lookup", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, b_y0 + 130), "⚡ FAANG's #1 Most Asked Interview Algorithm Pattern", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    checklist = [
        ("01_dict_fundamentals_and_memory.py", "Compact table & key constraints"),
        ("02_dict_methods_and_crud.py", ".get(), .setdefault() & pipe union |"),
        ("03_dict_internals_and_performance.py", "5,000x faster benchmark & TTL cache"),
        ("04_dict_interview_questions.py", "Two Sum, Anagrams, Subarray Sum"),
        ("my_practice.py (Student Workbook)", "All 6 Practice Tasks Ready! ✅")
    ]

    cur_y = b_y0 + 175
    for f_name, f_desc in checklist:
        draw.text((100, cur_y), "✅", font=FONT_BODY, fill=COLOR_GREEN)
        draw.text((140, cur_y), f_name, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((140, cur_y + 30), f_desc, font=FONT_BADGE, fill=COLOR_MUTED)
        cur_y += 66

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "⭐ Day 10 Complete! Follow along for Day 11 👇", font=FONT_SUB, fill=COLOR_CREAM, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day10/day10_reel_video.mp4"
    dest_path = "D:/fullstack-python-ai/day10/day10_reel_video.mp4"
    temp_dir = "D:/learn-python/day10/temp_frames_warm"
    preview_dir = "D:/fullstack-python-ai/day10/reel_preview_frames"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    print("Generating 5 Strictly Aligned Day 10 Frames...")
    img1 = create_scene_1()
    img2 = create_scene_2()
    img3 = create_scene_3()
    img4 = create_scene_4()
    img5 = create_scene_5()

    # Save preview frames for instant inspection
    img1.save(os.path.join(preview_dir, "scene1_roadmap_intro.png"))
    img2.save(os.path.join(preview_dir, "scene2_module01_compact_table.png"))
    img3.save(os.path.join(preview_dir, "scene3_module02_methods_union.png"))
    img4.save(os.path.join(preview_dir, "scene4_module03_speed_benchmark.png"))
    img5.save(os.path.join(preview_dir, "scene5_module04_two_sum_recap.png"))
    print("Preview frames saved to:", preview_dir)

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

    print(f"Rendering Day 10 Dark Warm 40s MP4 to {output_path}...")
    final_video.write_videofile(
        output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    # Copy to fullstack-python-ai
    import shutil
    shutil.copy2(output_path, dest_path)
    print(f"Copied final video to: {dest_path}")

    # Clean temporary files
    for p in [p1, p2, p3, p4, p5]:
        if os.path.exists(p):
            os.remove(p)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

    print(f"\n[SUCCESS] Day 10 Reel Video Generated: {output_path} & {dest_path}")


if __name__ == "__main__":
    generate_video()
