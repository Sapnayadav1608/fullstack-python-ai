"""
Day 15: Minimalist Luxury Editorial Tech Reel Generator (Times New Roman)
=========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: The 2:00 AM Production Outage Story
       Advanced Object-Oriented Architecture in Python

Design Philosophy (Minimalist, Calm, Luxury Tech):
- ZERO Information Overload: 1 big idea per scene, 70% negative breathing room
- Prestigious Typography: Times New Roman Bold & Italic (52-60px bold headlines)
- High Contrast & Legibility: Pure White (#FFFFFF) & Radiant Gold (#FFD700) on Deep Matte Obsidian (#09090C)
- Clean Minimalist Visual Centerpieces:
  * Scene 1: Bold Outage Statement + 1 Minimalist Incident Card
  * Scene 2: 5-line Clean Typewriter Code Block showing dynamic super()
  * Scene 3: Minimalist Geometric Diamond Graph + Clean MRO Ribbon
  * Scene 4: Pluggable Vector DB Interface + 1-Line Switcher
  * Scene 5: 3 Clean Gold Milestones + 100% Architect Ready
- Strict Instagram Safe Zone: Content ends at Y <= 1260, Progress bar at Y = 1300
- 620px completely empty bottom zone for captions & Instagram UI
- Pure silent video (audio=False) for real voiceover recording
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

# Minimalist Bold Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 56)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 21)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 26)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 22)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 52)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 19)

# Clean Editorial Palette
COLOR_BG_DARK = np.array([9, 9, 12], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (18, 16, 24, 252)                          # Sleek Glass Card
COLOR_INNER_BG = (11, 10, 15, 255)                         # Pitch Black Inner

COLOR_WHITE = (255, 255, 255)          # 100% Pure White
COLOR_LIGHT = (226, 232, 240)          # Light Platinum
COLOR_GOLD = (255, 215, 0)             # Radiant Gold
COLOR_RED = (248, 113, 113)            # Warning Coral
COLOR_GREEN = (52, 211, 153)           # Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Sky Cyan
COLOR_BORDER = (65, 60, 80)            # Crisp Subtle Border


def ease_out(t):
    """Smooth cubic ease-out."""
    t = np.clip(t, 0.0, 1.0)
    return 1.0 - (1.0 - t) ** 3.0


def render_minimal_canvas(t, progress_ratio, badge_text):
    """
    Renders an ultra-clean, minimalist matte dark canvas with huge breathing room.
    """
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    # Subtle vignette
    d = np.sqrt((x - WIDTH // 2)**2 + (y - 650)**2)
    w = (np.clip(1.0 - d / 900.0, 0, 1) ** 2.2)[:, :, None]
    base += w * np.array([28, 24, 34], dtype=np.float32)

    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 140 to 192) - Generous top breathing room
    badge_w, badge_h = 560, 52
    bx0, by0 = (WIDTH - badge_w) // 2, 140
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=26, fill=(24, 20, 30, 250), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # Clean Gold Progress Bar (Y: 1290 to 1298) - High above Instagram safe zone!
    bar_y = 1290
    bar_w = WIDTH - 200
    draw.rounded_rectangle([100, bar_y, 100 + bar_w, bar_y + 8], radius=4, fill=(22, 18, 26), outline=(45, 40, 55))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([100, bar_y, 100 + fill_len, bar_y + 8], radius=4, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): THE HOOK (Minimalist & Dramatic)
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_minimal_canvas(t, prog, "DAY 15 / 30  •  AI ARCHITECTURE")

    # Big Bold Editorial Statement (Huge breathing room)
    draw.text((WIDTH // 2, 290), "Why 90% of AI Apps", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Crash at 2:00 AM.", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "A single OOP inheritance bug cost $10,000 in duplicate API calls.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Just 1 Sleek Minimalist Incident Card (Y: 490 to 920)
    card_y0, card_y1 = 490, 920
    draw.rounded_rectangle([90, card_y0, WIDTH - 90, card_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_RED, width=2)

    # Red Warning Pill
    draw.rounded_rectangle([125, card_y0 + 35, 450, card_y0 + 78], radius=8, fill=(45, 15, 20), outline=COLOR_RED, width=1)
    draw.text((287, card_y0 + 56), "PRODUCTION INCIDENT: 02:14 AM", font=FONT_MINI, fill=COLOR_RED, anchor="mm")

    draw.text((125, card_y0 + 115), "Fatal: Inconsistent MRO Resolution", font=FONT_TITLE, fill=COLOR_WHITE)

    # 2 Clear, Punchy Points (No wall of text!)
    draw.rounded_rectangle([125, card_y0 + 165, WIDTH - 125, card_y0 + 370], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
    
    draw.text((150, card_y0 + 200), "❌ The Flaw:", font=FONT_HEADING, fill=COLOR_RED)
    draw.text((150, card_y0 + 240), "Multiple inheritance executed the base LLM client TWICE,", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((150, card_y0 + 270), "triggering 5,000 duplicate API calls and memory corruption.", font=FONT_BODY, fill=COLOR_LIGHT)

    draw.text((150, card_y0 + 315), "✅ The Senior Fix:", font=FONT_HEADING, fill=COLOR_GREEN)
    draw.text((150, card_y0 + 350), "Python C3 Linearization & Dynamic super() Chaining.", font=FONT_BODY, fill=COLOR_GOLD)

    # Single Minimalist Bottom Callout Pill (Y: 970 to 1050)
    draw.rounded_rectangle([90, 970, WIDTH - 90, 1050], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1010), "Watch the Senior Architect Blueprint ->", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): THE RULE (Never Hardcode Parent Names)
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_minimal_canvas(t, prog, "RULE 01  •  INHERITANCE & super()")

    draw.text((WIDTH // 2, 290), "Never Hardcode", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Parent Class Names.", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "super() is not the parent. It is a dynamic runtime proxy.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: 1 Clean Minimalist Code Box (Y: 480 to 1040)
    c_y0, c_y1 = 480, 1040
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Cooperative State Chaining Pattern", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Terminal inner
    draw.rounded_rectangle([120, c_y0 + 75, WIDTH - 120, c_y1 - 35], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)

    code_lines = [
        ("class FineTunedClient(AIModelClient):", COLOR_GOLD),
        ("    def __init__(self, model_id, lora):", COLOR_WHITE),
        ("        # 1. Cooperative MRO initialization:", COLOR_LIGHT),
        ("        super().__init__(model_id=model_id)", COLOR_GREEN),
        ("        self.lora = lora", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("    def generate(self, prompt: str):", COLOR_GOLD),
        ("        # 2. Dynamic runtime method extension:", COLOR_LIGHT),
        ("        raw = super().generate(prompt)", COLOR_CYAN),
        ("        return self.lora.apply(raw)", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# CPython resolves next class dynamically along MRO!", COLOR_LIGHT),
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
    draw.rounded_rectangle([90, 1070, WIDTH - 90, 1150], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1110), "super() resolves the NEXT class in MRO at runtime", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): THE CLIMAX (The Diamond Problem & C3 MRO)
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_minimal_canvas(t, prog, "RULE 02  •  THE DIAMOND PROBLEM")

    draw.text((WIDTH // 2, 290), "The Infamous", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Diamond Trap.", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "How Python C3 Linearization guarantees single execution.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Minimalist Geometric Diamond Diagram (Y: 480 to 980)
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

    # Clean Big Resolution Ribbon
    ry0 = c_y0 + 390
    draw.rounded_rectangle([120, ry0, WIDTH - 120, ry0 + 64], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, ry0 + 32), "Resolution Path:  D  ->  B  ->  C  ->  A  ->  object", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Bottom Pill
    draw.rounded_rectangle([90, 1020, WIDTH - 90, 1100], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1060), "Zero duplicates. Guaranteed single execution path.", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): SENIOR ARCHITECTURE (Pluggable Vector DBs)
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_minimal_canvas(t, prog, "RULE 03  •  PLUGGABLE ADAPTERS")

    draw.text((WIDTH // 2, 290), "Zero Vendor Lock-in.", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Pluggable Vector DBs.", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "Enforcing interface contracts with abc.ABC & @abstractmethod.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Minimalist Pluggable Architecture Box (Y: 480 to 1020)
    c_y0, c_y1 = 480, 1020
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Enterprise Vector DB Interface Engine", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Abstract Base Class Box
    draw.rounded_rectangle([120, c_y0 + 75, WIDTH - 120, c_y0 + 185], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
    draw.text((145, c_y0 + 102), "class BaseVectorDatabase(abc.ABC):", font=FONT_HEADING, fill=COLOR_GOLD)
    draw.text((145, c_y0 + 138), "@abstractmethod def upsert(self, id: str, vector: list): ...", font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((145, c_y0 + 164), "@abstractmethod def query(self, vec: list, top_k: int): ...", font=FONT_CODE_SM, fill=COLOR_LIGHT)

    # Dividing line
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
    draw.text((145, c_y0 + 408), "1-Line Swappable RAG Pipeline Architecture:", font=FONT_BODY, fill=COLOR_GOLD)
    active_code = "pipeline = RAGPipeline(db=PineconeAdapter())  # Cloud Active" if is_pinecone else "pipeline = RAGPipeline(db=ChromaDBAdapter())  # Local Active"
    draw.text((145, c_y0 + 444), active_code, font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((145, c_y0 + 472), "Decoupled architecture guarantees zero vendor lock-in!", font=FONT_BODY, fill=COLOR_LIGHT)

    # Bottom Pill
    draw.rounded_rectangle([90, 1050, WIDTH - 90, 1130], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1090), "Guaranteed interfaces prevent runtime bugs before production", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): THE VICTORY (You Just Leveled Up!)
# =========================================================================
MILESTONES = [
    ("Dynamic super() Proxy", "Chains cooperative state along MRO dynamically"),
    ("The Diamond Problem Solved", "C3 Linearization guarantees monotonic execution"),
    ("Pluggable Vector DB Adapters", "1-line swappable architecture with abc.ABC")
]

def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.0)
    img, draw = render_minimal_canvas(t, prog, "DAY 15 / 30  •  MASTERY UNLOCKED")

    draw.text((WIDTH // 2, 290), "You Just", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 355), "Leveled Up.", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 420), "From junior spaghetti code to Senior AI System Architect.", font=FONT_SUB, fill=COLOR_LIGHT, anchor="mm")

    # Centerpiece: Just 3 Clean Milestone Cards (Y: 480 to 880)
    c_y0, c_y1 = 480, 880
    draw.rounded_rectangle([90, c_y0, WIDTH - 90, c_y1], radius=20, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c_y0 + 40), "Architect Mastery Milestones", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    py = c_y0 + 80
    for idx, (title, desc) in enumerate(MILESTONES):
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

    # Single Clean Metric Card (Y: 910 to 1020)
    pct = int(min(100, (t / 5.5) * 100))
    draw.rounded_rectangle([90, 910, WIDTH - 90, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 945), f"MASTERY: {pct}% COMPLETE", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 985), "4 In-Depth Modules  •  6 Lab Tasks in Workbook  •  Production Ready", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill
    draw.rounded_rectangle([90, 1050, WIDTH - 90, 1130], radius=20, fill=(24, 20, 30), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 1090), "⭐ Full code & workbook on GitHub. Link in bio!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# VIDEO COMPOSITOR & EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day15"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Minimalist Luxury Tech Reel (Times New Roman)...")
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
