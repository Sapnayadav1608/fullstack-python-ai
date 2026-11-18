"""
Day 14: Ultra-Aesthetic Infographic + Dynamic Typewriter Code Reel Generator
=============================================================================
30-Day Full Stack Python + AI Engineering Challenge

Features:
- 1080x1920 Vertical Aspect Ratio (Instagram Reel / Shorts)
- Exact 40.0 Seconds Duration (5 Scenes x 8s @ 24fps)
- Dynamic Typewriter Effect: Code types out with a blinking developer cursor '▌'
- Scene 5 Progressive Checklist Animation
- Deep Dark Obsidian Base (#0C090C) with Subtle Warm Amber/Ember Glow
- High Readability Bold Typography (Segoe UI Bold + Consolas Bold)
- Strict Safe Zone: Content ends at Y = 1330, Progress bar at Y = 1350-1360
- 560px bottom clear zone (Y: 1360 to 1920) for Instagram captions and UI!
- Zero Personal Name (Generic Track Branding)
- Audio: Pure clean video (no audio track) for real voiceover recording
- Output paths: D:/learn-python/day14
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
COLOR_CYAN = (56, 189, 248)             # Neon Cyan / Sky


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


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 14 / 30"):
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


def draw_typewriter_code(draw, code_lines, start_y, t, typing_start=0.4, typing_end=5.6):
    """
    Renders lines of code with character-by-character typewriter progression and blinking cursor.
    """
    line_lengths = [max(1, len(txt)) for txt, _ in code_lines]
    total_chars = sum(line_lengths)

    if t < typing_start:
        chars_to_show = 0
    elif t >= typing_end:
        chars_to_show = total_chars
    else:
        alpha = (t - typing_start) / (typing_end - typing_start)
        chars_to_show = int(alpha * total_chars)

    # Blinking cursor (toggled every 0.25s)
    cursor_visible = (int(t * 4) % 2 == 0)

    cur_y = start_y
    accumulated_chars = 0
    cursor_drawn = False

    for idx, (code_text, color) in enumerate(code_lines, start=1):
        line_len = max(1, len(code_text))

        # Always draw line number and vertical gutter separator
        draw.text((100, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 38, 48, 120), width=1)

        if accumulated_chars + line_len <= chars_to_show:
            # Entire line is typed
            draw.text((165, cur_y), code_text, font=FONT_CODE, fill=color)
            if accumulated_chars + line_len == chars_to_show and not cursor_drawn and cursor_visible:
                bbox = draw.textbbox((165, cur_y), code_text, font=FONT_CODE)
                draw.text((bbox[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        elif accumulated_chars < chars_to_show:
            # Partial line typed
            chars_in_line = chars_to_show - accumulated_chars
            partial_text = code_text[:chars_in_line]
            draw.text((165, cur_y), partial_text, font=FONT_CODE, fill=color)
            if not cursor_drawn and cursor_visible:
                bbox = draw.textbbox((165, cur_y), partial_text, font=FONT_CODE)
                draw.text((bbox[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            # Line not yet reached
            if not cursor_drawn and cursor_visible:
                draw.text((165, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True

        accumulated_chars += line_len
        cur_y += 39


# =========================================================================
# SCENE 1 (0 to 8s): ROADMAP & INTRO HOOK (Typewriter Code)
# =========================================================================
def build_base_scene_1():
    img, draw = draw_canvas(0.20, "DAY 14 / 30  •  ROADMAP & INTRO")
    draw.text((WIDTH // 2, 246), "Object-Oriented Python (OOP)", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Classes, Objects, The self Parameter & Encapsulation", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: 4 Sequential Modules
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DAY 14 COMPLETE 4-MODULE ROADMAP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("MOD 01", "Classes, Objects, Lifecycle (__new__ vs __init__) & self", COLOR_GREEN),
        ("MOD 02", "Namespaces (__dict__), Class vs Instance & Mutable Trap", COLOR_ORANGE),
        ("MOD 03", "The 3 Methods: Instance, @classmethod & @staticmethod", COLOR_CYAN),
        ("MOD 04", "Encapsulation, Name Mangling (__var) & @property", COLOR_CORAL)
    ]

    p_y = card_y0 + 64
    for mod_tag, mod_desc, col in modules:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 54], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((125, p_y + 14), mod_tag, font=FONT_SUB, fill=col)
        draw.text((250, p_y + 16), mod_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 66

    # Bottom Code Box Frame (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((100, c_y0 + 30), "The Class Blueprint: Bundling State & Behavior", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Day 14 is live! Master Object-Oriented Python! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_1 = build_base_scene_1()
CODE_SCENE_1 = [
    ("class AIModel:", COLOR_GOLD),
    ("    def __init__(self, name, context_len):", COLOR_WHITE),
    ("        self.name = name  # Instance variable", COLOR_GREEN),
    ("        self.context_len = context_len", COLOR_WHITE),
    ("", COLOR_WHITE),
    ("    def prompt(self, text):", COLOR_GOLD),
    ("        # CPython desugars: AIModel.prompt(self, text)", COLOR_MUTED),
    ("        return f'[{self.name}]: Processing {text}'", COLOR_CYAN),
    ("", COLOR_WHITE),
    ("gpt = AIModel('GPT-4o', 128_000)", COLOR_AMBER),
    ("print(gpt.prompt('Explain OOP')) # Dispatches self!", COLOR_GREEN)
]

def make_frame_scene_1(t):
    img = BASE_SCENE_1.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_1, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 (The self Mechanism & __new__ vs __init__)
# =========================================================================
def build_base_scene_2():
    img, draw = draw_canvas(0.40, "DAY 14 / 30  •  MODULE 01")
    draw.text((WIDTH // 2, 246), "The self Parameter", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "How Python Dispatches Methods Under The Hood", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: The Architecture
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE TWO STAGES OF INSTANTIATION", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Item 1: __new__ vs __init__
    draw.rounded_rectangle([100, card_y0 + 64, WIDTH - 100, card_y0 + 154], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((120, card_y0 + 84), "1. __new__(cls) vs __init__(self):", font=FONT_SUB, fill=COLOR_AMBER)
    draw.text((120, card_y0 + 116), "   __new__ allocates raw memory | __init__ initializes attributes.", font=FONT_BODY, fill=COLOR_CREAM)

    # Item 2: self Desugaring
    draw.rounded_rectangle([100, card_y0 + 168, WIDTH - 100, card_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
    draw.text((120, card_y0 + 188), "2. The `self` Mechanism Demystified:", font=FONT_SUB, fill=COLOR_CYAN)
    draw.text((120, card_y0 + 220), "   `dev.introduce()` is pure syntactic sugar for:", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 252), "   `Developer.introduce(dev)` -> Instance passed as 1st arg!", font=FONT_BODY, fill=COLOR_GOLD)
    draw.text((120, card_y0 + 284), "   `__str__` (for users) vs `__repr__` (for debuggers & REPL).", font=FONT_BODY, fill=COLOR_GREEN)

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, c_y0 + 30), "CPython Under-The-Hood: self Dispatched Explicitly", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1290), "⚡ 'self' is not a keyword — it's an instance pointer passed by CPython! 🎯", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img

BASE_SCENE_2 = build_base_scene_2()
CODE_SCENE_2 = [
    ("dev = Developer('Sapna', role='AI Engineer')", COLOR_GOLD),
    ("", COLOR_WHITE),
    ("# Syntax A: Calling method on instance", COLOR_MUTED),
    ("msg_a = dev.introduce()", COLOR_WHITE),
    ("", COLOR_WHITE),
    ("# Syntax B: What CPython actually runs under the hood:", COLOR_MUTED),
    ("msg_b = Developer.introduce(dev)  # Explicit instance!", COLOR_CYAN),
    ("", COLOR_WHITE),
    ("print(msg_a == msg_b)  # True! Identical bytecode!", COLOR_GREEN),
    ("", COLOR_WHITE),
    ("# __str__: pretty text | __repr__: eval(repr(obj))==obj", COLOR_AMBER)
]

def make_frame_scene_2(t):
    img = BASE_SCENE_2.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_2, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): MODULE 02 & 03 (The 3 Method Types & Factory Patterns)
# =========================================================================
def build_base_scene_3():
    img, draw = draw_canvas(0.60, "DAY 14 / 30  •  MODULE 02 & 03")
    draw.text((WIDTH // 2, 246), "The 3 Method Flavors", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Instance Methods, @classmethod & @staticmethod", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Method Comparison
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "WHICH METHOD FLAVOR TO USE?", font=FONT_HEADING, fill=COLOR_ORANGE, anchor="mm")

    methods = [
        ("1. INSTANCE (self)", "Operates on specific object state (e.g. self.name).", COLOR_GREEN),
        ("2. @classmethod (cls)", "Alternative Factory Constructors (from_json, from_dict).", COLOR_GOLD),
        ("3. @staticmethod", "Isolated utility math/helpers (no self, no cls).", COLOR_CYAN)
    ]

    p_y = card_y0 + 64
    for m_title, m_desc, col in methods:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 70], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((120, p_y + 16), m_title, font=FONT_SUB, fill=col)
        draw.text((120, p_y + 44), m_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 82

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((100, c_y0 + 30), "Alternative Factory Constructor Pattern", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Clean factory constructors with @classmethod beat ugly __init__ flags! 🚀", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    return img

BASE_SCENE_3 = build_base_scene_3()
CODE_SCENE_3 = [
    ("class LLMClient:", COLOR_GOLD),
    ("    # 1. Alternative Factory Constructor", COLOR_MUTED),
    ("    @classmethod", COLOR_GOLD),
    ("    def from_json(cls, json_payload):", COLOR_WHITE),
    ("        data = json.loads(json_payload)", COLOR_WHITE),
    ("        return cls(model=data['model'], key=data['key'])", COLOR_GREEN),
    ("", COLOR_WHITE),
    ("    # 2. Pure Static Utility Math (No self, no cls)", COLOR_MUTED),
    ("    @staticmethod", COLOR_CYAN),
    ("    def cosine_similarity(v1, v2):", COLOR_WHITE),
    ("        return sum(a*b for a,b in zip(v1, v2))", COLOR_AMBER)
]

def make_frame_scene_3(t):
    img = BASE_SCENE_3.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_3, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): MODULE 04 (Encapsulation, Name Mangling & @property)
# =========================================================================
def build_base_scene_4():
    img, draw = draw_canvas(0.80, "DAY 14 / 30  •  MODULE 04")
    draw.text((WIDTH // 2, 246), "Encapsulation & @property", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Pythonic Data Protection & Bounds Validation", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Encapsulation Levels
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE 3 VISIBILITY CONVENTIONS IN PYTHON", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    levels = [
        ("PUBLIC (name)", "Free for all callers to read & mutate directly.", COLOR_WHITE),
        ("PROTECTED (_name)", "Single underscore convention: 'internal detail, do not touch'.", COLOR_AMBER),
        ("PRIVATE (__name)", "Double underscore: CPython Name Mangling (_Class__name).", COLOR_RED)
    ]

    p_y = card_y0 + 64
    for l_title, l_desc, col in levels:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 70], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((120, p_y + 16), l_title, font=FONT_SUB, fill=col)
        draw.text((120, p_y + 44), l_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 82

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
    draw.text((100, c_y0 + 30), "Pythonic Getter & Setter with Strict Validation", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1290), "🛡️ Eliminates clumsy get_x() and set_x() Java anti-patterns! ⚡", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img

BASE_SCENE_4 = build_base_scene_4()
CODE_SCENE_4 = [
    ("class BankAccount:", COLOR_GOLD),
    ("    def __init__(self, deposit):", COLOR_WHITE),
    ("        self._balance = deposit # Protected", COLOR_MUTED),
    ("", COLOR_WHITE),
    ("    @property", COLOR_CYAN),
    ("    def balance(self): return self._balance # Getter", COLOR_GREEN),
    ("", COLOR_WHITE),
    ("    @balance.setter", COLOR_GOLD),
    ("    def balance(self, amt):", COLOR_WHITE),
    ("        if amt < 0: raise ValueError('Negative balance!')", COLOR_RED),
    ("        self._balance = amt # Validated Setter!", COLOR_GREEN)
]

def make_frame_scene_4(t):
    img = BASE_SCENE_4.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_4, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): RECAP & ANIMATED CHECKLIST
# =========================================================================
def build_base_scene_5():
    img, draw = draw_canvas(1.0, "DAY 14 / 30  •  RECAP & WRAP-UP")
    draw.text((WIDTH // 2, 246), "OOP Part 1 & Recap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Clean Object Design, @property & Day 14 Checklist", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Architecture Summary
    s_y0, s_y1 = 330, 660
    draw.rounded_rectangle([70, s_y0, WIDTH - 70, s_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 30), "ENTERPRISE OBJECT DESIGN CHECKLIST", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Banner 1: Architecture
    draw.rounded_rectangle([105, s_y0 + 64, WIDTH - 105, s_y0 + 165], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 98), "__dict__ Introspection & Attribute Lookup Chain", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 134), "⚡ Avoid mutable class variables! Use __slots__ for 6x less RAM!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Banner 2: Clean API
    draw.rounded_rectangle([105, s_y0 + 180, WIDTH - 105, s_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN)
    draw.text((WIDTH // 2, s_y0 + 218), "Clean Encapsulation & Alternative Constructors", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 265), "@property getters/setters guard state without breaking API!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Combined Card: Checklist Frame
    b_y0, b_y1 = 680, 1230
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, b_y0 + 30), "Day 14 Modules & Student Workbook Checklist", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, b_y0 + 52, WIDTH - 70, b_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "📂 Code & Practice Workbook live on GitHub! Follow for Day 15! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_5 = build_base_scene_5()

CHECKLIST_ITEMS = [
    ("MOD 01: Classes, Objects, Lifecycle & self Desugaring", COLOR_GREEN),
    ("MOD 02: __dict__ Namespaces, Lookup Chain & __slots__", COLOR_ORANGE),
    ("MOD 03: The 3 Methods: Instance, @classmethod & @staticmethod", COLOR_CYAN),
    ("MOD 04: Encapsulation, Name Mangling & @property Validation", COLOR_CORAL),
    ("WORKBOOK: 6 Hands-on OOP Practice Tasks (my_practice.py)", COLOR_GOLD),
    ("TEST SUITE: Automated Test Harness (run_tests)", COLOR_GREEN)
]

def draw_animated_checklist(draw, t, start_y=750):
    item_delay = 0.7
    for idx, (text, col) in enumerate(CHECKLIST_ITEMS):
        reveal_t = 0.5 + idx * item_delay
        y = start_y + idx * 72

        if t >= reveal_t:
            draw.rounded_rectangle([100, y, WIDTH - 100, y + 58], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
            draw.text((120, y + 14), "✅", font=FONT_SUB, fill=COLOR_GREEN)
            draw.text((170, y + 16), text, font=FONT_BODY, fill=COLOR_WHITE)
        else:
            draw.rounded_rectangle([100, y, WIDTH - 100, y + 58], radius=14, fill=(15, 11, 15, 180), outline=(45, 32, 40, 140), width=1)
            draw.text((120, y + 14), "⏳", font=FONT_SUB, fill=COLOR_MUTED)
            draw.text((170, y + 16), text, font=FONT_BODY, fill=COLOR_MUTED)

def make_frame_scene_5(t):
    img = BASE_SCENE_5.copy()
    draw = ImageDraw.Draw(img)
    draw_animated_checklist(draw, t)
    return np.array(img)


# =========================================================================
# MAIN VIDEO COMPOSER & EXPORTER
# =========================================================================
def generate_all_scenes():
    print("\n--- Generating Day 14 Ultra-Aesthetic Typewriter Reel ---")
    os.makedirs("day14/reel_preview_frames", exist_ok=True)

    # Save Previews at peak typewriter typing (t=6.0s)
    print("Saving Preview Frames at peak typing (t=6.0s)...")
    Image.fromarray(make_frame_scene_1(6.0)).save("day14/reel_preview_frames/scene1_roadmap_intro.png")
    Image.fromarray(make_frame_scene_2(6.0)).save("day14/reel_preview_frames/scene2_module01_self_mechanism.png")
    Image.fromarray(make_frame_scene_3(6.0)).save("day14/reel_preview_frames/scene3_module02_method_flavors.png")
    Image.fromarray(make_frame_scene_4(6.0)).save("day14/reel_preview_frames/scene4_module03_encapsulation_property.png")
    Image.fromarray(make_frame_scene_5(6.0)).save("day14/reel_preview_frames/scene5_module04_recap_checklist.png")
    print("Saved 5 Preview Frames to 'day14/reel_preview_frames/' [OK]")

    clip1 = VideoClip(make_frame_scene_1, duration=SCENE_DURATION)
    clip2 = VideoClip(make_frame_scene_2, duration=SCENE_DURATION)
    clip3 = VideoClip(make_frame_scene_3, duration=SCENE_DURATION)
    clip4 = VideoClip(make_frame_scene_4, duration=SCENE_DURATION)
    clip5 = VideoClip(make_frame_scene_5, duration=SCENE_DURATION)

    print("\nConcatenating 5 Scenes (Exact 40.0s @ 24fps)...")
    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5], method="compose")

    out_path = "day14/day14_reel_video.mp4"
    print(f"Exporting video to: {out_path}")

    final_video.write_videofile(
        out_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )
    print(f"\n[SUCCESS] Final Video Saved: {out_path} ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    generate_all_scenes()
