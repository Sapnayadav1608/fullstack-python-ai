"""
Day 13: Ultra-Aesthetic Infographic + Dynamic Typewriter Code Reel Generator
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
- Output paths: D:/learn-python/day13
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


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 13 / 30"):
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
    img, draw = draw_canvas(0.20, "DAY 13 / 30  •  ROADMAP & INTRO")
    draw.text((WIDTH // 2, 246), "Python Iterators & Generators", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Streaming Big Data & Lazy Evaluation in O(1) RAM", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: 4 Sequential Modules
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DAY 13 COMPLETE 4-MODULE ROADMAP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("MOD 01", "The Iteration Protocol: __iter__, __next__ & for-loop Engine", COLOR_GREEN),
        ("MOD 02", "Generators, yield & Live 10M Memory Benchmark", COLOR_ORANGE),
        ("MOD 03", "Composable Pipelines, yield from & AI Token Streaming", COLOR_CYAN),
        ("MOD 04", "Context Managers, with & Atomic DB Auto-Rollback", COLOR_CORAL)
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
    draw.text((100, c_y0 + 30), "The Generator Pattern: Lazy Evaluation in O(1) RAM", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Day 13 is live! Master Streaming & Iteration! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_1 = build_base_scene_1()
CODE_SCENE_1 = [
    ("def token_stream(prompt):", COLOR_GOLD),
    ("    # Yields tokens lazily without loading full reply", COLOR_MUTED),
    ("    for chunk in query_llm_model(prompt):", COLOR_WHITE),
    ("        yield chunk  # Freezes frame, O(1) RAM!", COLOR_GREEN),
    ("", COLOR_WHITE),
    ("# Consuming live stream (ChatGPT / Gemini style)", COLOR_MUTED),
    ("stream = token_stream('Explain AI Engineering')", COLOR_CYAN),
    ("for token in stream:", COLOR_WHITE),
    ("    print(token, end='', flush=True) # Real-time!", COLOR_AMBER),
    ("", COLOR_WHITE),
    ("# Zero memory lag! Scales to 100M+ tokens!", COLOR_GREEN)
]

def make_frame_scene_1(t):
    img = BASE_SCENE_1.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_1, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 (Iteration Protocol & Under the Hood for-loop)
# =========================================================================
def build_base_scene_2():
    img, draw = draw_canvas(0.40, "DAY 13 / 30  •  MODULE 01")
    draw.text((WIDTH // 2, 246), "The Iteration Protocol", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "How Python's for-Loop Works Under The Hood", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Protocol Mechanics
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE TWO CONTRACTS OF ITERATION", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Item 1: Iterable
    draw.rounded_rectangle([100, card_y0 + 64, WIDTH - 100, card_y0 + 144], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((120, card_y0 + 84), "1. ITERABLE (list, str, dict):", font=FONT_SUB, fill=COLOR_AMBER)
    draw.text((120, card_y0 + 116), "   Implements __iter__() -> Produces a fresh iterator instance.", font=FONT_BODY, fill=COLOR_CREAM)

    # Item 2: Iterator
    draw.rounded_rectangle([100, card_y0 + 158, WIDTH - 100, card_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
    draw.text((120, card_y0 + 178), "2. ITERATOR (stateful data stream):", font=FONT_SUB, fill=COLOR_CYAN)
    draw.text((120, card_y0 + 210), "   Implements BOTH __iter__() (returns self) AND __next__().", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 242), "   Raises StopIteration when exhausted. Cannot be rewound!", font=FONT_BODY, fill=COLOR_RED)
    draw.text((120, card_y0 + 274), "   AI Mini-Batcher: Streams batches directly to GPU VRAM.", font=FONT_BODY, fill=COLOR_GREEN)

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, c_y0 + 30), "CPython Under-The-Hood: for-Loop Emulation", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, 1290), "⚡ The for-loop is just syntactic sugar over iter() & next()! 🎯", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    return img

BASE_SCENE_2 = build_base_scene_2()
CODE_SCENE_2 = [
    ("# When you write: for item in dataset: ...", COLOR_MUTED),
    ("# CPython executes this exact while loop:", COLOR_MUTED),
    ("iterator = iter(dataset)  # Calls __iter__()", COLOR_GOLD),
    ("while True:", COLOR_WHITE),
    ("    try:", COLOR_WHITE),
    ("        item = next(iterator)  # Calls __next__()", COLOR_CYAN),
    ("        process_ai_batch(item)", COLOR_AMBER),
    ("    except StopIteration:", COLOR_GREEN),
    ("        break  # Stream terminated safely!", COLOR_GREEN),
    ("", COLOR_WHITE),
    ("# Trap: list(iterator) exhausts it permanently!", COLOR_RED)
]

def make_frame_scene_2(t):
    img = BASE_SCENE_2.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_2, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): MODULE 02 (Generators & Live 45,000x Memory Benchmark)
# =========================================================================
def build_base_scene_3():
    img, draw = draw_canvas(0.60, "DAY 13 / 30  •  MODULE 02")
    draw.text((WIDTH // 2, 246), "Generators & yield", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Frame Freezing & 45,000x Memory Optimization", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Benchmark Comparison
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "1,000,000 INTEGERS MEMORY BENCHMARK", font=FONT_HEADING, fill=COLOR_ORANGE, anchor="mm")

    # Bench 1: List
    draw.rounded_rectangle([100, card_y0 + 64, WIDTH - 100, card_y0 + 144], radius=14, fill=COLOR_INNER_BG, outline=COLOR_RED, width=2)
    draw.text((120, card_y0 + 84), "LIST COMPREHENSION [x * 2 for x in data]:", font=FONT_SUB, fill=COLOR_RED)
    draw.text((120, card_y0 + 116), "  💥 Peak Heap RAM: 38.57 MB (Eager - Out of Memory risk)", font=FONT_BODY, fill=COLOR_CREAM)

    # Bench 2: Generator
    draw.rounded_rectangle([100, card_y0 + 158, WIDTH - 100, card_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((120, card_y0 + 178), "GENERATOR EXPRESSION (x * 2 for x in data):", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((120, card_y0 + 210), "  ⚡ Peak Heap RAM: 0.87 KB (Constant O(1) Memory!)", font=FONT_BODY, fill=COLOR_GOLD)
    draw.text((120, card_y0 + 242), "  🚀 Result: Uses ~45,000x LESS RAM than List!", font=FONT_BODY, fill=COLOR_GREEN)
    draw.text((120, card_y0 + 274), "  🔄 States: GEN_CREATED -> GEN_SUSPENDED -> GEN_CLOSED", font=FONT_BODY, fill=COLOR_CYAN)

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((100, c_y0 + 30), "Infinite Stream Generator: State Preserved at yield", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Stream 50GB Big Data on an 8GB laptop with zero OOM! 🚀", font=FONT_SUB, fill=COLOR_ORANGE, anchor="mm")

    return img

BASE_SCENE_3 = build_base_scene_3()
CODE_SCENE_3 = [
    ("def infinite_fibonacci():", COLOR_GOLD),
    ("    a, b = 0, 1", COLOR_WHITE),
    ("    while True:", COLOR_WHITE),
    ("        yield a  # Pauses instruction & freezes frame", COLOR_GREEN),
    ("        a, b = b, a + b  # Resumes on next()", COLOR_WHITE),
    ("", COLOR_WHITE),
    ("# Inspecting CPython frame state:", COLOR_MUTED),
    ("fib = infinite_fibonacci()", COLOR_CYAN),
    ("print(inspect.getgeneratorstate(fib)) # GEN_CREATED", COLOR_AMBER),
    ("next(fib) # Starts execution", COLOR_WHITE),
    ("print(inspect.getgeneratorstate(fib)) # GEN_SUSPENDED", COLOR_GREEN)
]

def make_frame_scene_3(t):
    img = BASE_SCENE_3.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_3, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): MODULE 03 (Pipelines, yield from & AI Streaming)
# =========================================================================
def build_base_scene_4():
    img, draw = draw_canvas(0.80, "DAY 13 / 30  •  MODULE 03")
    draw.text((WIDTH // 2, 246), "Pipelines & AI Streaming", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Unix Pipes, yield from & Bidirectional Coroutines", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Pipeline Architecture
    card_y0, card_y1 = 330, 660
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE 3 PRODUCTION GENERATOR POWERS", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    features = [
        ("UNIX PIPELINES", "Chain stages: raw_stream | parse_json | filter_anomalies", COLOR_GOLD),
        ("`yield from`", "Delegates directly to sub-generators & recursive flattening", COLOR_GREEN),
        ("COROUTINES", "Bidirectional flow: .send(data), .throw(err), .close()", COLOR_CORAL)
    ]

    p_y = card_y0 + 64
    for feat_title, feat_desc, col in features:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 70], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
        draw.text((120, p_y + 16), feat_title, font=FONT_SUB, fill=col)
        draw.text((120, p_y + 44), feat_desc, font=FONT_BODY, fill=COLOR_CREAM)
        p_y += 82

    # Bottom Code Card (Y: 680 to 1230)
    c_y0, c_y1 = 680, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
    draw.text((100, c_y0 + 30), "Recursive Flattening & LLM Token Streaming", font=FONT_BADGE, fill=COLOR_MUTED, anchor="lm")
    draw.line([70, c_y0 + 52, WIDTH - 70, c_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Takeaway Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, 1290), "🤖 Clean composable streaming for modern AI architectures! ⚡", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")

    return img

BASE_SCENE_4 = build_base_scene_4()
CODE_SCENE_4 = [
    ("def deep_flatten(nested_data):", COLOR_GOLD),
    ("    # Elegant recursive flattening with yield from", COLOR_MUTED),
    ("    if isinstance(nested_data, (list, tuple)):", COLOR_WHITE),
    ("        for item in nested_data:", COLOR_WHITE),
    ("            yield from deep_flatten(item) # Delegates!", COLOR_GREEN),
    ("    else:", COLOR_WHITE),
    ("        yield nested_data", COLOR_CYAN),
    ("", COLOR_WHITE),
    ("# Bidirectional Coroutine Consumer", COLOR_MUTED),
    ("def averager():", COLOR_GOLD),
    ("    val = yield avg  # Receives input via .send()", COLOR_AMBER)
]

def make_frame_scene_4(t):
    img = BASE_SCENE_4.copy()
    draw = ImageDraw.Draw(img)
    draw_typewriter_code(draw, CODE_SCENE_4, start_y=756, t=t)
    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): MODULE 04 + ANIMATED CHECKLIST RECAP
# =========================================================================
def build_base_scene_5():
    img, draw = draw_canvas(1.0, "DAY 13 / 30  •  RECAP & WRAP-UP")
    draw.text((WIDTH // 2, 246), "Context Managers & Recap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Resource Safety, @contextmanager & Day 13 Checklist", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Context Manager Protocol
    s_y0, s_y1 = 330, 660
    draw.rounded_rectangle([70, s_y0, WIDTH - 70, s_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 30), "RESOURCE SAFETY: THE `with` PROTOCOL", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Banner 1: with statement
    draw.rounded_rectangle([105, s_y0 + 64, WIDTH - 105, s_y0 + 165], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, s_y0 + 98), "__enter__() sets up | __exit__() guarantees teardown", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 134), "⚡ Atomic DB Transactions: Automatic Rollback on Exceptions!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Banner 2: @contextlib.contextmanager
    draw.rounded_rectangle([105, s_y0 + 180, WIDTH - 105, s_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN)
    draw.text((WIDTH // 2, s_y0 + 218), "@contextlib.contextmanager: The Generator Bridge", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text((WIDTH // 2, s_y0 + 265), "Code before yield = __enter__ | Code in finally = __exit__", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Combined Card: Checklist Frame
    b_y0, b_y1 = 680, 1230
    draw.rounded_rectangle([70, b_y0, WIDTH - 70, b_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((100, b_y0 + 30), "Day 13 Modules & Student Workbook Checklist", font=FONT_BADGE, fill=COLOR_GOLD, anchor="lm")
    draw.line([70, b_y0 + 52, WIDTH - 70, b_y0 + 52], fill=(55, 38, 48, 180), width=1)

    # Bottom Pill
    draw.rounded_rectangle([80, 1250, WIDTH - 80, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "📂 Code & Practice Workbook live on GitHub! Follow for Day 14! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_5 = build_base_scene_5()

CHECKLIST_ITEMS = [
    ("MOD 01: The Iteration Protocol (__iter__, __next__, CPython for-loop)", COLOR_GREEN),
    ("MOD 02: Generators, yield & Live 45,000x Memory Benchmark", COLOR_ORANGE),
    ("MOD 03: Composable Pipelines, yield from & LLM Streaming", COLOR_CYAN),
    ("MOD 04: Context Managers, with & Atomic DB Auto-Rollback", COLOR_CORAL),
    ("WORKBOOK: 6 Hands-on Practice Challenges (my_practice.py)", COLOR_GOLD),
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
    print("\n--- Generating Day 13 Ultra-Aesthetic Typewriter Reel ---")
    os.makedirs("day13/reel_preview_frames", exist_ok=True)

    # Save Previews at peak typewriter typing (t=6.0s)
    print("Saving Preview Frames at peak typing (t=6.0s)...")
    Image.fromarray(make_frame_scene_1(6.0)).save("day13/reel_preview_frames/scene1_roadmap_intro.png")
    Image.fromarray(make_frame_scene_2(6.0)).save("day13/reel_preview_frames/scene2_module01_iteration_protocol.png")
    Image.fromarray(make_frame_scene_3(6.0)).save("day13/reel_preview_frames/scene3_module02_generator_benchmark.png")
    Image.fromarray(make_frame_scene_4(6.0)).save("day13/reel_preview_frames/scene4_module03_pipelines_streaming.png")
    Image.fromarray(make_frame_scene_5(6.0)).save("day13/reel_preview_frames/scene5_module04_context_managers_recap.png")
    print("Saved 5 Preview Frames to 'day13/reel_preview_frames/' [OK]")

    clip1 = VideoClip(make_frame_scene_1, duration=SCENE_DURATION)
    clip2 = VideoClip(make_frame_scene_2, duration=SCENE_DURATION)
    clip3 = VideoClip(make_frame_scene_3, duration=SCENE_DURATION)
    clip4 = VideoClip(make_frame_scene_4, duration=SCENE_DURATION)
    clip5 = VideoClip(make_frame_scene_5, duration=SCENE_DURATION)

    print("\nConcatenating 5 Scenes (Exact 40.0s @ 24fps)...")
    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5], method="compose")

    out_path = "day13/day13_reel_video.mp4"
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
