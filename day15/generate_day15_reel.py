"""
Day 15: Personal Journey Daily Vlog Reel Generator (Times New Roman Edition)
============================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 15/30: What I Learned & Built Today!" (Personal Learning Journey)
       Mastering Advanced Object-Oriented Programming (OOP) Part 2

Story Structure (Daily Progress Vlog):
- Scene 1: Journey Hook -> "Day 15/30 of my Python + AI Journey! Today I tackled Advanced OOP!"
- Scene 2: Step 1 -> "First, I mastered Inheritance & Dynamic super() state chaining"
- Scene 3: Step 2 -> "Next, I solved the famous Diamond Problem with C3 Linearization MRO"
- Scene 4: Step 3 -> "Then, I built pluggable Vector DB adapters with abc.ABC & Protocols"
- Scene 5: Day 15 Complete -> "Halfway mark (50%)! Solved 6 practice workbook challenges. Follow my journey!"

Visual & Design Highlights:
- Clean Editorial Journey Log (Times New Roman Bold & Italic)
- Ultra-Clean Minimalist Cards with 70% breathing room (Zero "content hi content" clutter!)
- High Visibility: Pure White (#FFFFFF), Radiant Gold (#FFD700) on Deep Matte Obsidian (#09090C)
- Strict Safe Zone: Content ends at Y <= 1240, Progress bar at Y = 1280
- Bottom 640px completely clear for Instagram captions & UI
- Pure silent video (audio=False) for Sapna to record her real voiceover
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

# Times New Roman Bold & Bold Italic (Clean, Prestigious Editorial)
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 54)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 52)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 20)

# Clean High-Contrast Palette
COLOR_BG_DARK = np.array([9, 9, 12], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (20, 18, 26, 252)                          # Sleek Glass Card
COLOR_INNER_BG = (12, 10, 16, 255)                         # Pitch Black Inner

COLOR_WHITE = (255, 255, 255)          # 100% Pure White
COLOR_LIGHT = (226, 232, 240)          # Light Platinum
COLOR_GOLD = (255, 215, 0)             # Radiant Gold
COLOR_GREEN = (52, 211, 153)           # Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Sky Cyan
COLOR_BORDER = (65, 60, 80)            # Crisp Subtle Border


def ease_out(t):
    """Smooth cubic ease-out."""
    t = np.clip(t, 0.0, 1.0)
    return 1.0 - (1.0 - t) ** 3.0


def render_journey_canvas(t, progress_ratio, badge_text):
    """
    Renders an ultra-clean, minimalist matte dark canvas with generous breathing room.
    """
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    # Soft subtle center aura
    d = np.sqrt((x - WIDTH // 2)**2 + (y - 650)**2)
    w = (np.clip(1.0 - d / 900.0, 0, 1) ** 2.2)[:, :, None]
    base += w * np.array([28, 24, 34], dtype=np.float32)

    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 140 to 192)
    badge_w, badge_h = 560, 52
    bx0, by0 = (WIDTH - badge_w) // 2, 140
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=26, fill=(24, 20, 30, 250), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # Clean Gold Progress Bar (Y: 1270 to 1278) - Safe above caption zone
    bar_y = 1270
    bar_w = WIDTH - 200
    draw.rounded_rectangle([100, bar_y, 100 + bar_w, bar_y + 8], radius=4, fill=(22, 18, 26), outline=(45, 40, 55))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([100, bar_y, 100 + fill_len, bar_y + 8], radius=4, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK - "Day 15: What I Learned Today!"
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 15 / 30  •  MY PYTHON + AI JOURNEY")

    # Headline
    draw.text((WIDTH // 2, 285), "Day 15 of 30 Days", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Python + AI Engineering!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "Here is everything I learned and built today.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Daily Roadmap Card (Clean, Spacious)
    card_y0, card_y1 = 480, 940
    draw.rounded_rectangle([90, card_y0, WIDTH - 90, card_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 40), "Today's Learning Focus: Advanced OOP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "Inheritance & Dynamic super()", "Chaining parent state without hardcoding names"),
        ("02", "The Diamond Problem & C3 MRO", "Mastering method resolution order in Python"),
        ("03", "Pluggable Vector DB Architecture", "Building swappable adapters with abc.ABC"),
        ("04", "Practice Workbook Tasks", "Solving 6 hands-on OOP challenges with tests")
    ]

    py = card_y0 + 80
    for num, title, desc in modules:
        draw.rounded_rectangle([120, py, WIDTH - 120, py + 86], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        # Gold Number Tag
        draw.rounded_rectangle([135, py + 15, 185, py + 71], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
        draw.text((160, py + 43), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((205, py + 22), title, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((205, py + 52), desc, font=FONT_MINI, fill=COLOR_LIGHT)
        py += 100

    # Bottom Pill
    draw.rounded_rectangle([90, 980, WIDTH - 90, 1060], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1020), "Come along with me on Day 15 ->", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - "First, I Mastered super() and Inheritance"
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  WHAT I LEARNED FIRST")

    draw.text((WIDTH // 2, 285), "Step 1: Inheritance &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "The Dynamic super() Proxy", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "I learned why you should never hardcode parent class names.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Clean Code Box showing what she wrote
    c_y0, c_y1 = 480, 1030
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "My Code: FineTunedGeminiClient", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    draw.rounded_rectangle([120, c_y0 + 75, WIDTH - 120, c_y1 - 35], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)

    code_lines = [
        ("class FineTunedClient(AIModelClient):", COLOR_GOLD),
        ("    def __init__(self, model_id, lora):", COLOR_WHITE),
        ("        # 1. Calling super() delegates dynamically:", COLOR_LIGHT),
        ("        super().__init__(model_id=model_id)", COLOR_GREEN),
        ("        self.lora = lora", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("    def generate(self, prompt: str):", COLOR_GOLD),
        ("        # 2. Extending base method cleanly:", COLOR_LIGHT),
        ("        raw = super().generate(prompt)", COLOR_CYAN),
        ("        return self.lora.apply(raw)", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# super() queries the MRO chain at runtime!", COLOR_LIGHT),
        ("print(FineTunedClient.mro())", COLOR_WHITE)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = c_y0 + 105
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((145, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_LIGHT)
        draw.line([185, cur_y - 2, 185, cur_y + 24], fill=COLOR_BORDER, width=1)

        if acc + line_len <= shown_chars:
            draw.text((205, cur_y), text, font=FONT_CODE_SM, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((205, cur_y), text, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((205, cur_y), part, font=FONT_CODE_SM, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((205, cur_y), part, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((205, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 34

    # Bottom Pill
    draw.rounded_rectangle([90, 1060, WIDTH - 90, 1140], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1100), "Key Takeaway: super() is a dynamic runtime proxy!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - "Next, I Solved The Diamond Problem"
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I SOLVED NEXT")

    draw.text((WIDTH // 2, 285), "Step 2: Solving The", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Famous Diamond Problem", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "I learned how C3 Linearization prevents duplicate method calls.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Clean Geometric Diamond Graph (Y: 480 to 980)
    c_y0, c_y1 = 480, 980
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "C3 Method Resolution Order (MRO)", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    step = 0
    if t >= 6.0:
        step = 4
    elif t >= 4.5:
        step = 3
    elif t >= 3.0:
        step = 2
    elif t >= 1.5:
        step = 1

    nw, nh = 280, 68
    ax0, ay0 = WIDTH // 2 - nw // 2, c_y0 + 80
    bx0, by0 = 120, c_y0 + 185
    cx0, cy0 = WIDTH - 120 - nw, c_y0 + 185
    dx0, dy0 = WIDTH // 2 - nw // 2, c_y0 + 290

    # Clean Connecting Lines
    draw.line([dx0 + nw // 4, dy0, bx0 + nw // 2, by0 + nh], fill=COLOR_BORDER, width=2)
    draw.line([dx0 + 3 * nw // 4, dy0, cx0 + nw // 2, cy0 + nh], fill=COLOR_BORDER, width=2)
    draw.line([bx0 + nw // 2, by0, ax0 + nw // 4, ay0 + nh], fill=COLOR_BORDER, width=2)
    draw.line([cx0 + nw // 2, cy0, ax0 + 3 * nw // 4, ay0 + nh], fill=COLOR_BORDER, width=2)

    if step >= 2:
        draw.line([dx0 + nw // 4, dy0, bx0 + nw // 2, by0 + nh], fill=COLOR_GOLD, width=3)
    if step >= 3:
        draw.line([dx0 + 3 * nw // 4, dy0, cx0 + nw // 2, cy0 + nh], fill=COLOR_GOLD, width=3)
    if step >= 4:
        draw.line([bx0 + nw // 2, by0, ax0 + nw // 4, ay0 + nh], fill=COLOR_GOLD, width=3)
        draw.line([cx0 + nw // 2, cy0, ax0 + 3 * nw // 4, ay0 + nh], fill=COLOR_GOLD, width=3)

    def draw_node(x0, y0, title, code, is_active, badge=None):
        fill_col = (35, 28, 42) if is_active else COLOR_INNER_BG
        border_col = COLOR_GOLD if is_active else COLOR_BORDER
        draw.rounded_rectangle([x0, y0, x0 + nw, y0 + nh], radius=10, fill=fill_col, outline=border_col, width=2 if is_active else 1)
        draw.text((x0 + nw // 2, y0 + 22), title, font=FONT_BODY, fill=COLOR_WHITE if is_active else COLOR_LIGHT, anchor="mm")
        draw.text((x0 + nw // 2, y0 + 48), code, font=FONT_CODE_SM, fill=COLOR_GOLD if is_active else COLOR_LIGHT, anchor="mm")
        if badge and is_active:
            draw.rounded_rectangle([x0 + nw - 26, y0 - 12, x0 + nw + 26, y0 + 12], radius=6, fill=COLOR_GOLD)
            draw.text((x0 + nw, y0), badge, font=FONT_BADGE, fill=(10, 8, 14), anchor="mm")

    draw_node(ax0, ay0, "Class A (Base Root)", "def ping(): 'Root'", step == 4, "4th")
    draw_node(bx0, by0, "Class B (Left)", "super().ping()", step == 2, "2nd")
    draw_node(cx0, cy0, "Class C (Right)", "super().ping()", step == 3, "3rd")
    draw_node(dx0, dy0, "Class D(B, C)", "d = D(); d.ping()", step >= 1, "1st")

    # Resolution Ribbon
    ry0 = c_y0 + 390
    draw.rounded_rectangle([120, ry0, WIDTH - 120, ry0 + 64], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, ry0 + 32), "Resolution Path:  D  ->  B  ->  C  ->  A  ->  object", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Bottom Pill
    draw.rounded_rectangle([90, 1020, WIDTH - 90, 1100], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1060), "Zero duplicate executions. Single deterministic path!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - "Then, I Built Pluggable Vector DB Adapters"
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 285), "Step 3: Pluggable AI", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Vector Database Architecture", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "I built adapters for Pinecone and ChromaDB with abc.ABC.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Pluggable Architecture Box (Y: 480 to 1020)
    c_y0, c_y1 = 480, 1020
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Enterprise Vector DB Interface Engine", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Abstract Base Class Box
    draw.rounded_rectangle([120, c_y0 + 75, WIDTH - 120, c_y0 + 185], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
    draw.text((145, c_y0 + 102), "class BaseVectorDatabase(abc.ABC):", font=FONT_HEADING, fill=COLOR_GOLD)
    draw.text((145, c_y0 + 138), "@abstractmethod def upsert(self, id: str, vector: list): ...", font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((145, c_y0 + 164), "@abstractmethod def query(self, vec: list, top_k: int): ...", font=FONT_CODE_SM, fill=COLOR_LIGHT)

    # Dividing connector line
    draw.line([WIDTH // 2, c_y0 + 185, WIDTH // 2, c_y0 + 225], fill=COLOR_GOLD, width=2)
    draw.line([WIDTH // 4 + 20, c_y0 + 225, 3 * WIDTH // 4 - 20, c_y0 + 225], fill=COLOR_GOLD, width=2)
    draw.line([WIDTH // 4 + 20, c_y0 + 225, WIDTH // 4 + 20, c_y0 + 245], fill=COLOR_GOLD, width=2)
    draw.line([3 * WIDTH // 4 - 20, c_y0 + 225, 3 * WIDTH // 4 - 20, c_y0 + 245], fill=COLOR_GOLD, width=2)

    # Dual Provider Cards
    ad_w = (WIDTH - 240 - 24) // 2
    is_pinecone = (int(t * 1.5) % 2 == 0)

    # Pinecone
    p_fill = (35, 28, 42) if is_pinecone else COLOR_INNER_BG
    draw.rounded_rectangle([120, c_y0 + 245, 120 + ad_w, c_y0 + 360], radius=10, fill=p_fill, outline=COLOR_CYAN if is_pinecone else COLOR_BORDER, width=2 if is_pinecone else 1)
    draw.text((120 + ad_w // 2, c_y0 + 278), "PineconeAdapter", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")
    draw.text((120 + ad_w // 2, c_y0 + 312), "Cloud Serverless Vector DB", font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
    draw.text((120 + ad_w // 2, c_y0 + 338), "✓ 100% Contract Satisfied", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")

    # ChromaDB
    ch_x = 120 + ad_w + 24
    c_fill = (35, 28, 42) if not is_pinecone else COLOR_INNER_BG
    draw.rounded_rectangle([ch_x, c_y0 + 245, ch_x + ad_w, c_y0 + 360], radius=10, fill=c_fill, outline=COLOR_GOLD if not is_pinecone else COLOR_BORDER, width=2 if not is_pinecone else 1)
    draw.text((ch_x + ad_w // 2, c_y0 + 278), "ChromaDBAdapter", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 312), "Local In-Memory Vector DB", font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 338), "✓ 100% Contract Satisfied", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")

    # 1-Line Swappable Showcase Box
    draw.rounded_rectangle([120, c_y0 + 380, WIDTH - 120, c_y0 + 495], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
    draw.text((145, c_y0 + 408), "1-Line Swappable RAG Pipeline:", font=FONT_BODY, fill=COLOR_GOLD)
    active_code = "pipeline = RAGPipeline(db=PineconeAdapter())  # Cloud Active" if is_pinecone else "pipeline = RAGPipeline(db=ChromaDBAdapter())  # Local Active"
    draw.text((145, c_y0 + 444), active_code, font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((145, c_y0 + 472), "Now I can swap databases anytime with zero vendor lock-in!", font=FONT_BODY, fill=COLOR_LIGHT)

    # Bottom Pill
    draw.rounded_rectangle([90, 1050, WIDTH - 90, 1130], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1090), "Interface contracts guarantee zero runtime crashes!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): WRAP-UP - "Day 15 Complete! Halfway Mark (50%)!"
# =========================================================================
TASKS_DONE = [
    ("4 In-Depth Modules Mastered", "Inheritance, super(), C3 MRO, Mixins & Vector DB ABCs"),
    ("6 Practice Tasks Solved", "All 6 unit tests passing in my practice workbook"),
    ("Halfway Mark Reached (50%)", "15 days completed out of 30 days challenge!")
]

def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.0)
    img, draw = render_journey_canvas(t, prog, "DAY 15 / 30  •  DAILY PROGRESS COMPLETE")

    draw.text((WIDTH // 2, 285), "Day 15 Completed!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 350), "Officially 50% Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 415), "15 days down, 15 more exciting days to go.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Daily Achievements Box (Y: 480 to 880)
    c_y0, c_y1 = 480, 880
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Today's Daily Progress Log", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    py = c_y0 + 80
    for idx, (title, desc) in enumerate(TASKS_DONE):
        reveal_time = idx * 1.5
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([120, py, WIDTH - 120, py + 95], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
            # Gold Checkmark
            draw.rounded_rectangle([140, py + 18, 200, py + 78], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
            draw.text((170, py + 48), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((220, py + 26), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((220, py + 60), desc, font=FONT_BODY, fill=COLOR_LIGHT)
        else:
            draw.rounded_rectangle([120, py, WIDTH - 120, py + 95], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
            draw.rounded_rectangle([140, py + 18, 200, py + 78], radius=8, fill=(20, 18, 24), outline=COLOR_BORDER, width=1)
            draw.text((170, py + 48), "○", font=FONT_HEADING, fill=COLOR_LIGHT, anchor="mm")
            draw.text((220, py + 26), title, font=FONT_HEADING, fill=(120, 120, 140))
            draw.text((220, py + 60), desc, font=FONT_BODY, fill=(90, 90, 100))
        py += 115

    # Halfway Milestone Card (Y: 910 to 1020)
    pct = int(min(50, 25 + (t / 5.5) * 25))
    draw.rounded_rectangle([90, 910, WIDTH - 90, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 945), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 985), "Follow along my 30-Day Python + AI Journey! Day 16 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill
    draw.rounded_rectangle([90, 1050, WIDTH - 90, 1130], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1090), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# VIDEO COMPOSITOR & EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day15"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Day 15 Personal Journey Daily Vlog Reel...")
    print("=" * 65)

    # 1. Export High-Resolution Preview Frames
    print("📸 Exporting 5 Preview Frames for Quality Verification...")
    previews = [
        ("scene_1.png", make_frame_scene_1(4.5)),
        ("scene_2.png", make_frame_scene_2(4.5)),
        ("scene_3.png", make_frame_scene_3(5.5)),
        ("scene_4.png", make_frame_scene_4(4.5)),
        ("scene_5.png", make_frame_scene_5(5.5)),
    ]
    for filename, frame_arr in previews:
        preview_path = os.path.join(preview_dir, filename)
        Image.fromarray(frame_arr).save(preview_path)
        print(f"  ✓ Saved: {preview_path}")

    # 2. Build Video Clips for Each Scene
    clip1 = VideoClip(make_frame_scene_1, duration=SCENE_DURATION)
    clip2 = VideoClip(make_frame_scene_2, duration=SCENE_DURATION)
    clip3 = VideoClip(make_frame_scene_3, duration=SCENE_DURATION)
    clip4 = VideoClip(make_frame_scene_4, duration=SCENE_DURATION)
    clip5 = VideoClip(make_frame_scene_5, duration=SCENE_DURATION)

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])

    video_output_path = os.path.join(out_dir, "day15_reel_video.mp4")
    print(f"\n🎥 Encoding MP4 Video: {video_output_path}")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        logger="bar"
    )

    print("\n" + "=" * 65)
    print(f"✅ Video Generated Successfully: {video_output_path}")
    print(f"✅ Total Duration: {final_video.duration:.1f}s | FPS: {FPS}")
    print(f"✅ Previews saved in: {preview_dir}")
    print("=" * 65)


if __name__ == "__main__":
    main()
