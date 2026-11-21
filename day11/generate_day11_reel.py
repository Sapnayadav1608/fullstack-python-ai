"""
Day 11: Ultra-Aesthetic Infographic + Code Reel Generator (Deep Dark + Warm Shade)
===================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Specifications:
- 1080x1920 Vertical Aspect Ratio (Instagram Reel / Shorts)
- Exact 40.0 Seconds Duration (5 Scenes x 8s @ 24fps)
- Deep Dark Obsidian Base (#0C090C) with Subtle Warm Amber/Ember Glow
- High Readability Bold Typography (Segoe UI Bold + Consolas Bold)
- Strict Safe Zone: Content ends at Y = 1330, Progress bar at Y = 1350-1360.
- 560px bottom clear zone (Y: 1360 to 1920) for Instagram captions and UI!
- Zero Personal Name (Generic Track Branding)
- Output paths: D:/learn-python/day11 & D:/fullstack-python-ai/day11
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
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 27)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 23)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 23)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 42)

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


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 11 / 30"):
    """Paints top header, track branding (NO PERSONAL NAME), and glowing progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 125 to 181)
    badge_w, badge_h = 560, 56
    bx0 = (WIDTH - badge_w) // 2
    by0 = 125
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=28, fill=(24, 16, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_CREAM, anchor="mm")

    # Subtitle Branding (NO PERSONAL NAME)
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar (Y: 1350 to 1360) - Safe above caption zone!
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(20, 14, 18, 240), outline=(55, 38, 48, 180))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): ROADMAP & INTRO HOOK (Functions & Execution)
# =========================================================================
def create_scene_1():
    img, draw = draw_canvas(0.20, "DAY 11 / 30  •  ROADMAP & INTRO")

    draw.text((WIDTH // 2, 246), "Python Functions & Execution", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Building Blocks of Scalable Python & AI Code", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: 4 Sequential Modules of Day 11 (Y: 330 to 660)
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DAY 11 COMPLETE 4-MODULE ROADMAP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("MOD 01", "Parameters, *args, **kwargs & Mutable Default Trap", COLOR_GREEN),
        ("MOD 02", "LEGB Scope Resolution & UnboundLocalError Trap", COLOR_ORANGE),
        ("MOD 03", "Closures, Lexical Scope & Function Factories", COLOR_GOLD),
        ("MOD 04", "Lambdas, Multi-Key Sort & Recursive Flattener", COLOR_CORAL)
    ]

    p_y = card_y0 + 64
    for mod_tag, mod_desc, col in modules:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 54], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((125, p_y + 14), mod_tag, font=FONT_SUB, fill=col)
        draw.text((250, p_y + 16), mod_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 66

    # Bottom Code Box: The #1 Python Interview Trap (Y: 680 to 1230)
    code_y0, code_y1 = 680, 1230
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, code_y0 + 30), "The #1 Python Interview Trap: Mutable Default List", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, code_y0 + 52, WIDTH - 70, code_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("# 1. Dangerous mutable default (Shared across calls!):", COLOR_CORAL),
        ("def add_user(uid, users=[]):", COLOR_WHITE),
        ("    users.append(uid)", COLOR_WHITE),
        ("    return users", COLOR_WHITE),
        ("print(add_user(101))  # [101]", COLOR_GOLD),
        ("print(add_user(202))  # [101, 202] 😱 Leaking state!", COLOR_RED),
        ("", COLOR_WHITE),
        ("# 2. The Pythonic Sentinel Fix:", COLOR_GREEN),
        ("def add_user_safe(uid, users=None):", COLOR_GREEN),
        ("    if users is None: users = []  # Fresh local list", COLOR_GREEN),
        ("    users.append(uid); return users  # Safe ✅", COLOR_GOLD)
    ]

    cur_y = code_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 40

    # Bottom Pill (Y: 1250 to 1330) - Safe Zone Above Captions!
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Day 11 is live! Master Functions & Scopes! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 (Modern Parameters: *args, /, *)
# =========================================================================
def create_scene_2():
    img, draw = draw_canvas(0.40, "DAY 11 / 30  •  MODULE 01")

    draw.text((WIDTH // 2, 246), "Modern Parameters: *args, / & *", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 01 • day11/01_function_parameters_and_signatures.py", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Python 3.8+ Syntax Spec (Y: 330 to 660)
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 30), "PYTHON 3.8+ PARAMETER SYNTAX SPECIFICATION", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Visual Syntax Box
    draw.rounded_rectangle([105, card_y0 + 64, WIDTH - 105, card_y0 + 135], radius=12, fill=COLOR_INNER_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, card_y0 + 100), "def api(path, method, /, timeout=30, *, auth=True):", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Parameter Breakdown Grid
    draw.rounded_rectangle([105, card_y0 + 150, WIDTH - 105, card_y0 + 315], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((130, card_y0 + 175), "1. Before '/' ➔ Positional-Only (No keywords allowed!)", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 215), "2. Middle     ➔ Standard (Positional OR Keyword)", font=FONT_SUB, fill=COLOR_ORANGE)
    draw.text((130, card_y0 + 255), "3. After '*'  ➔ Keyword-Only (MUST pass as keyword!)", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((130, card_y0 + 288), "✨ Prevents breaking API changes across production versions!", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Code Box: Dynamic Argument Unpacking (Y: 680 to 1230)
    code_y0, code_y1 = 680, 1230
    draw.rounded_rectangle([70, code_y0, WIDTH - 70, code_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, code_y0 + 30), "Dynamic Argument Unpacking (*args & **kwargs)", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, code_y0 + 52, WIDTH - 70, code_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("def build_prompt(role: str, *docs: str, **params):", COLOR_GOLD),
        ("    print(f'System Role: {role}')", COLOR_WHITE),
        ("    for doc in docs:  # *args gathers into a TUPLE", COLOR_GREEN),
        ("        print(f'  - Context: {doc}')", COLOR_WHITE),
        ("    temp = params.get('temp', 0.7) # **kwargs DICT", COLOR_ORANGE),
        ("    return f'Configured LLM (temp={temp})' ✨", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# Call with arbitrary documents & hyper-parameters:", COLOR_MUTED),
        ("build_prompt('AI Tutor', *my_docs, **config)", COLOR_WHITE),
        ("# Injects parameters dynamically without hardcoding! ✅", COLOR_GREEN)
    ]

    cur_y = code_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 42

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "💡 Use '/' and '*' to strictly enforce safe API boundaries!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img


# =========================================================================
# SCENE 3 (16 to 24s): MODULE 02 (LEGB Hierarchy & UnboundLocalError)
# =========================================================================
def create_scene_3():
    img, draw = draw_canvas(0.60, "DAY 11 / 30  •  MODULE 02")

    draw.text((WIDTH // 2, 246), "LEGB Rule & Scope Traps", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 02 • day11/02_scopes_and_legb_rule.py", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    # Top Card: 4-Level LEGB Hierarchy (Y: 330 to 660)
    v_y0, v_y1 = 330, 660
    draw.rounded_rectangle([70, v_y0, WIDTH - 70, v_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, v_y0 + 30), "THE LEGB VARIABLE LOOKUP HIERARCHY", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    levels = [
        ("[L] LOCAL", "Inside currently executing function", COLOR_GREEN),
        ("[E] ENCLOSING", "Outer function scopes in closures", COLOR_GOLD),
        ("[G] GLOBAL", "Module-level variables / top-level", COLOR_ORANGE),
        ("[B] BUILT-IN", "Python native names (len, sum, range)", COLOR_ROSE)
    ]

    for i, (tag, desc, col) in enumerate(levels):
        ox = 105 if i % 2 == 0 else 555
        oy = v_y0 + 68 if i < 2 else v_y0 + 192
        draw.rounded_rectangle([ox, oy, ox + 420, oy + 105], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((ox + 25, oy + 25), tag, font=FONT_SUB, fill=col)
        draw.text((ox + 25, oy + 64), desc, font=FONT_BADGE, fill=COLOR_CREAM)

    # Bottom Code Box: The UnboundLocalError Trap (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, c_y0 + 30), "The Infamous UnboundLocalError Mystery", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("counter = 10  # Global variable", COLOR_WHITE),
        ("def bad_function():", COLOR_WHITE),
        ("    print(counter)  # UnboundLocalError! ❌", COLOR_RED),
        ("    counter += 1    # Assignment makes 'counter' local!", COLOR_CORAL),
        ("", COLOR_WHITE),
        ("# The Nonlocal Solution for Nested Closures:", COLOR_GREEN),
        ("def create_rate_limiter(max_calls=3):", COLOR_GOLD),
        ("    calls = 0  # Enclosing scope variable [E]", COLOR_WHITE),
        ("    def request():", COLOR_WHITE),
        ("        nonlocal calls  # Binds to enclosing scope! ✅", COLOR_GREEN),
        ("        calls += 1; return calls", COLOR_CREAM)
    ]

    cur_y = c_y0 + 76
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 39

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, 1290), "🚀 CPython flags local variables at compile-time!", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    return img


# =========================================================================
# SCENE 4 (24 to 32s): MODULE 03 (Closures & Lexical Scope)
# =========================================================================
def create_scene_4():
    img, draw = draw_canvas(0.80, "DAY 11 / 30  •  MODULE 03")

    draw.text((WIDTH // 2, 246), "Closures & Lexical Scope", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 03 • day11/03_first_class_functions_and_closures.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Top Card: How Closures Retain Enclosed Memory (Y: 330 to 660)
    b_y0, b_y1 = 330, 660
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, b_y0 + 30), "HOW CLOSURES RETAIN ENCLOSED SCOPE IN MEMORY", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Visual Closure Mechanism
    draw.rounded_rectangle([105, b_y0 + 64, WIDTH - 105, b_y0 + 155], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((130, b_y0 + 86), "Outer Function returns Inner Function ➔ Outer Frame Popped!", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, b_y0 + 120), "Inner Function holds a hidden __closure__ cell pointing to data!", font=FONT_BODY, fill=COLOR_CREAM)

    draw.rounded_rectangle([105, b_y0 + 170, WIDTH - 105, b_y0 + 315], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((130, b_y0 + 195), "double = make_multiplier(2)", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((130, b_y0 + 232), "double.__closure__[0].cell_contents  ==  2  (Alive in RAM! ✨)", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((130, b_y0 + 275), "⚡ Enables stateful logic WITHOUT polluting global variables!", font=FONT_BODY, fill=COLOR_GREEN)

    # Bottom Code Box: Streaming Moving Average Tracker (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, c_y0 + 30), "Production Pattern: Streaming Moving Average (O(1) Space)", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    code_lines = [
        ("def create_moving_average_tracker():", COLOR_GOLD),
        ("    total_sum, count = 0.0, 0", COLOR_WHITE),
        ("    def add_reading(val: float) -> float:", COLOR_GREEN),
        ("        nonlocal total_sum, count", COLOR_WHITE),
        ("        total_sum += val", COLOR_WHITE),
        ("        count += 1", COLOR_WHITE),
        ("        return total_sum / count  # O(1) Memory! ✨", COLOR_GREEN),
        ("    return add_reading", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("tracker = create_moving_average_tracker()", COLOR_WHITE),
        ("print(tracker(24.0)) # 24.0°C (No list stored in RAM!)", COLOR_CREAM)
    ]

    cur_y = c_y0 + 72
    for idx, (code_text, color) in enumerate(code_lines, start=1):
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)
        draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
        cur_y += 38

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1290), "⚡ Closures form the foundation of Python Decorators!", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img


# =========================================================================
# SCENE 5 (32 to 40s): MODULE 04 & RECAP (Multi-Key Lambda & Checklist)
# =========================================================================
def create_scene_5():
    img, draw = draw_canvas(1.0, "DAY 11 / 30  •  MODULE 04 & RECAP")

    draw.text((WIDTH // 2, 246), "Multi-Key Lambda & Day 11 Recap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Topic 04 • day11/04_lambdas_functional_patterns_and_recursion.py", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # Top Card: Multi-Key Lambda Sorting (Y: 330 to 660)
    s_y0, s_y1 = 330, 660
    draw.rounded_rectangle([70, s_y0, WIDTH - 70, s_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 30), "MULTI-KEY TUPLE SORTING WITH LAMBDAS", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Code Banner inside card
    draw.rounded_rectangle([105, s_y0 + 64, WIDTH - 105, s_y0 + 165], radius=14, fill=COLOR_INNER_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, s_y0 + 98), "sorted(devs, key=lambda d: (-d['salary'], -d['exp']))", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 134), "⚡ Sorts by Salary DESC, then Experience DESC in 1 line!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Recursion Badge inside card
    draw.rounded_rectangle([105, s_y0 + 180, WIDTH - 105, s_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD)
    draw.text((WIDTH // 2, s_y0 + 218), "Recursion: Base Case + Stack Frame Unwinding", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 265), "Solved FAANG Recursive Nested JSON Flattener in O(N)!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Combined Card: Day 11 Checklist (Y: 680 to 1230)
    b_y0, b_y1 = 680, 1230
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, b_y0 + 30), "Day 11 Modules & Student Workbook Checklist", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, b_y0 + 52, WIDTH - 70, b_y0 + 52], fill=(55, 38, 48, 180), width=1)

    checklist = [
        ("01_function_parameters_and_signatures.py", "Parameters, *args/**kwargs, mutable default"),
        ("02_scopes_and_legb_rule.py", "LEGB hierarchy, shadowing, UnboundLocalError"),
        ("03_first_class_functions_and_closures.py", "Closures, __closure__ cells & factories"),
        ("04_lambdas_functional_patterns_and_recursion.py", "Multi-key lambdas & recursive flattener"),
        ("my_practice.py (Student Workbook)", "All 6 Practice Tasks Ready! ✅")
    ]

    cur_y = b_y0 + 80
    for f_name, f_desc in checklist:
        draw.text((100, cur_y), "✅", font=FONT_BODY, fill=COLOR_GREEN)
        draw.text((140, cur_y), f_name, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((140, cur_y + 30), f_desc, font=FONT_BADGE, fill=COLOR_MUTED)
        cur_y += 66

    # Bottom Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "⭐ Day 11 Complete! Ready for Day 12 Decorators 👇", font=FONT_SUB, fill=COLOR_CREAM, anchor="mm")

    return img


def generate_video():
    output_path = "D:/learn-python/day11/day11_reel_video.mp4"
    dest_path = "D:/fullstack-python-ai/day11/day11_reel_video.mp4"
    temp_dir = "D:/learn-python/day11/temp_frames_warm"
    preview_dir = "D:/fullstack-python-ai/day11/reel_preview_frames"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(preview_dir, exist_ok=True)

    print("Generating 5 Strictly Aligned Day 11 Frames...")
    img1 = create_scene_1()
    img2 = create_scene_2()
    img3 = create_scene_3()
    img4 = create_scene_4()
    img5 = create_scene_5()

    # Save preview frames for instant inspection
    img1.save(os.path.join(preview_dir, "scene1_roadmap_intro.png"))
    img2.save(os.path.join(preview_dir, "scene2_module01_parameters_args.png"))
    img3.save(os.path.join(preview_dir, "scene3_module02_legb_scope.png"))
    img4.save(os.path.join(preview_dir, "scene4_module03_closures_factories.png"))
    img5.save(os.path.join(preview_dir, "scene5_module04_lambda_recap.png"))
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

    print(f"Rendering Day 11 Dark Warm 40s MP4 to {output_path}...")
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
            try:
                os.rmdir(temp_dir)
            except Exception:
                pass

    print(f"\n[SUCCESS] Day 11 Reel Video Generated: {output_path} & {dest_path}")


if __name__ == "__main__":
    generate_video()

