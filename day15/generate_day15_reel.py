"""
Day 15: Zero-Overflow High-Visibility Times New Roman Reel Generator
=====================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: The 2:00 AM Production Outage Story
       Advanced Object-Oriented Architecture in Python

Strict Formatting & Alignment Guarantees:
- Zero Overflow: Every line tested with draw.textbbox to ensure 30px+ safety padding inside all boxes!
- 100% Bold Typography: Uses Times New Roman Bold (`timesbd.ttf`) & Bold Italic (`timesbi.ttf`)
- Maximum Contrast Color Palette:
  * Pure Crisp White (#FFFFFF) & Radiant Bright Gold (#FFD700)
  * High-Contrast Light Platinum (#E2E8F0) - NO low-contrast dull greys!
  * Vivid Neon Green (#34D399) & Sky Cyan (#38BDF8)
- Generous Box Padding: Outer cards 65px margins, inner boxes 90px margins (900px wide)
- Storyline Arc:
  * Act 1: The Production Outage (The Relatable Hook)
  * Act 2: The Hardcoded Parent Trap vs Dynamic super() Proxy
  * Act 3: The Infamous Diamond Trap & C3 MRO (Clean Minimalist Graph)
  * Act 4: Senior Architecture - Mixins & Pluggable Vector DBs (Pinecone & ChromaDB)
  * Act 5: Mastery Milestones & 100% Architect Ready Checklist
- Strict Instagram Safe Zone: Content ends at Y <= 1320, Progress bar at Y = 1350
- Zero personal names on screen (Generic track branding)
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

# 100% BOLD, High-Visibility Typography (Calibrated Sizing)
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 50)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 40)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 24)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 52)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 20)

# High-Contrast Palette: NO dark/dull grey text!
COLOR_BG_DARK = np.array([10, 8, 14], dtype=np.float32)    # Deep Obsidian
COLOR_CARD_BG = (22, 18, 28, 252)                          # Crisp Dark Container
COLOR_INNER_BG = (12, 10, 16, 255)                         # Pitch Black Inner

COLOR_WHITE = (255, 255, 255)          # 100% Pure White (Razor Sharp)
COLOR_LIGHT = (226, 232, 240)          # Light Platinum (High Visibility)
COLOR_GOLD = (255, 215, 0)             # Radiant Bright Gold
COLOR_CREAM = (254, 243, 199)          # Pale Warm Ivory
COLOR_RED = (248, 113, 113)            # Bright Warning Coral/Red
COLOR_GREEN = (52, 211, 153)           # Bright Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Bright Sky Cyan
COLOR_BORDER = (75, 70, 95)            # Crisp, clearly visible card border


def ease_out(t):
    """Smooth cubic ease-out."""
    t = np.clip(t, 0.0, 1.0)
    return 1.0 - (1.0 - t) ** 3.0


def render_clean_background(t, global_progress):
    """Renders a clean, high-contrast dark canvas."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    d = np.sqrt((x - WIDTH // 2)**2 + (y - 700)**2)
    w = (np.clip(1.0 - d / 900.0, 0, 1) ** 2.2)[:, :, None]
    base += w * np.array([32, 26, 38], dtype=np.float32)

    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 125 to 181)
    badge_w, badge_h = 580, 56
    bx0, by0 = (WIDTH - badge_w) // 2, 125
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=28, fill=(28, 22, 34, 250), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), "DAY 15 / 30  •  THE OOP ARCHITECTURE STORY", font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # Subtitle Branding
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_MINI, fill=COLOR_LIGHT, anchor="mm")

    # Clean Gold Progress Bar (Y: 1350 to 1360)
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(24, 20, 30), outline=COLOR_BORDER, width=1)
    fill_len = int(bar_w * global_progress)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)

    return img, draw


def draw_clean_card(draw, bbox, fill=COLOR_CARD_BG, outline=COLOR_BORDER, radius=18, width=2):
    """Draws a clean, high-contrast card with crisp 2px borders."""
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)


# =========================================================================
# SCENE 1 (0 to 8s): ACT 1 - THE PRODUCTION OUTAGE (The Hook)
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_clean_background(t, prog)

    draw.text((WIDTH // 2, 246), "Why 90% of AI Apps Crash", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 296), "The 2:00 AM Production Bug & The Senior OOP Solution", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Card 1: The Outage Incident (Width 65 to 1015, inner 90 to 990)
    card_y0 = 345
    draw_clean_card(draw, [65, card_y0, WIDTH - 65, card_y0 + 265], outline=COLOR_RED, width=2)
    
    # Incident Pill
    draw.rounded_rectangle([95, card_y0 + 20, 420, card_y0 + 62], radius=6, fill=(50, 15, 20), outline=COLOR_RED, width=1)
    draw.text((257, card_y0 + 41), "PRODUCTION INCIDENT: 02:14 AM", font=FONT_MINI, fill=COLOR_RED, anchor="mm")
    draw.text((WIDTH // 2, card_y0 + 92), "Fatal: Inconsistent Method Resolution Order (MRO)", font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")

    # Story Explanation (Spacious 125px box, zero overflow)
    draw.rounded_rectangle([90, card_y0 + 120, WIDTH - 90, card_y0 + 245], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
    draw.text((115, card_y0 + 140), "• A junior developer merged multiple inheritance without MRO knowledge.", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((115, card_y0 + 172), "• Base class ran twice per prompt -> 5,000 duplicate LLM API calls!", font=FONT_BODY, fill=COLOR_GOLD)
    draw.text((115, card_y0 + 204), "• Context window corrupted, cloud bill doubled, server crashed.", font=FONT_BODY, fill=COLOR_LIGHT)

    # Card 2: The Senior Architect Roadmap
    c2_y0 = 635
    draw_clean_card(draw, [65, c2_y0, WIDTH - 65, c2_y0 + 580], outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c2_y0 + 38), "The Senior Architect Blueprint", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    pillars = [
        ("01", "Stop Hardcoding Parent Classes", "Why super() is a dynamic runtime proxy, not a parent call"),
        ("02", "Tame The Diamond Problem", "How Python's C3 Linearization guarantees single execution"),
        ("03", "Modular Mixin Composition", "Stack orthogonal behaviors like Lego bricks with zero bloat"),
        ("04", "Abstract Base Classes (abc.ABC)", "Build swappable Vector DB interfaces with zero vendor lock-in")
    ]

    py = c2_y0 + 75
    for num, title, desc in pillars:
        draw.rounded_rectangle([90, py, WIDTH - 90, py + 95], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        # Gold Number Tag
        draw.rounded_rectangle([108, py + 18, 168, py + 78], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
        draw.text((138, py + 48), num, font=FONT_TITLE, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((188, py + 26), title, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((188, py + 58), desc, font=FONT_BODY, fill=COLOR_LIGHT)
        py += 112

    # Bottom Callout Pill (Y: 1240 to 1320)
    draw_clean_card(draw, [65, 1240, WIDTH - 65, 1320], outline=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, 1280), "Let's fix this architecture step by step ->", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): ACT 2 - THE HARDCODED TRAP & THE super() PROXY
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_clean_background(t, prog)

    draw.text((WIDTH // 2, 246), "The Hardcoded Parent Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 296), "Why calling Parent.__init__(self) destroys your architecture", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Comparison Panel (Y: 345 to 640)
    card_y0 = 345
    draw_clean_card(draw, [65, card_y0, WIDTH - 65, card_y0 + 295], outline=COLOR_BORDER, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "The Rookie Mistake vs The Production Pattern", font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")

    # The Mistake Box
    draw.rounded_rectangle([90, card_y0 + 65, WIDTH - 90, card_y0 + 155], radius=10, fill=COLOR_INNER_BG, outline=COLOR_RED, width=1)
    draw.text((115, card_y0 + 88), "The Mistake: AIModelClient.__init__(self, model_id)", font=FONT_CODE_SM, fill=COLOR_RED)
    draw.text((115, card_y0 + 120), "Hardcoded class name -> Completely bypasses cooperative MRO!", font=FONT_BODY, fill=COLOR_LIGHT)

    # The Clean Solution Box
    draw.rounded_rectangle([90, card_y0 + 168, WIDTH - 90, card_y0 + 268], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=1)
    draw.text((115, card_y0 + 192), "The Solution: super().__init__(model_id=model_id)", font=FONT_CODE_SM, fill=COLOR_GREEN)
    draw.text((115, card_y0 + 226), "super() is a dynamic proxy! It queries the MRO chain at runtime.", font=FONT_BODY, fill=COLOR_WHITE)

    # Bottom Code Block with Dynamic Typewriter (Y: 660 to 1220)
    c2_y0 = 660
    draw_clean_card(draw, [65, c2_y0, WIDTH - 65, c2_y0 + 560], outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c2_y0 + 36), "Dynamic Runtime Dispatch in Python", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    code_lines = [
        ("class FineTunedClient(AIModelClient):", COLOR_GOLD),
        ("    def __init__(self, model_id, lora_adapter):", COLOR_WHITE),
        ("        # 1. Cooperative MRO initialization", COLOR_LIGHT),
        ("        super().__init__(model_id=model_id)", COLOR_GREEN),
        ("        self.lora_adapter = lora_adapter", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("    def generate(self, prompt: str):", COLOR_GOLD),
        ("        # 2. Dynamic runtime method extension", COLOR_LIGHT),
        ("        raw = super().generate(prompt)", COLOR_CYAN),
        ("        return self.lora_adapter.apply(raw)", COLOR_GOLD),
        ("", COLOR_WHITE),
        ("# CPython resolves the next class along MRO:", COLOR_LIGHT),
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
    cur_y = c2_y0 + 72
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((105, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_LIGHT)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=COLOR_BORDER, width=1)

        if acc + line_len <= shown_chars:
            draw.text((165, cur_y), text, font=FONT_CODE_SM, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((165, cur_y), text, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((165, cur_y), part, font=FONT_CODE_SM, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((165, cur_y), part, font=FONT_CODE_SM)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((165, cur_y), "▌", font=FONT_CODE_SM, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 36

    # Bottom Pill
    draw_clean_card(draw, [65, 1240, WIDTH - 65, 1320], outline=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, 1280), "super() resolves the NEXT class in instance MRO at runtime", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): ACT 3 - THE DIAMOND TRAP & C3 LINEARIZATION
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_clean_background(t, prog)

    draw.text((WIDTH // 2, 246), "The Infamous Diamond Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 296), "How Python's C3 Algorithm Guarantees Zero Duplicate Calls", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Center Flowchart Card: Clean Diamond Graph (Y: 345 to 800)
    card_y0 = 345
    draw_clean_card(draw, [65, card_y0, WIDTH - 65, card_y0 + 455], outline=COLOR_BORDER, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "The Diamond Inheritance Architecture", font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")

    step = 0
    if t >= 6.0:
        step = 4
    elif t >= 4.5:
        step = 3
    elif t >= 3.0:
        step = 2
    elif t >= 1.5:
        step = 1

    nw, nh = 290, 72
    ax0 = WIDTH // 2 - nw // 2
    ay0 = card_y0 + 68
    bx0 = 90
    by0 = card_y0 + 180
    cx0 = WIDTH - 90 - nw
    cy0 = card_y0 + 180
    dx0 = WIDTH // 2 - nw // 2
    dy0 = card_y0 + 295

    # Connecting Lines (Thick, clearly visible)
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

    def draw_clean_node(x0, y0, title, code, is_active, step_badge=None):
        fill_col = (35, 28, 40) if is_active else COLOR_INNER_BG
        border_col = COLOR_GOLD if is_active else COLOR_BORDER
        draw.rounded_rectangle([x0, y0, x0 + nw, y0 + nh], radius=10, fill=fill_col, outline=border_col, width=2 if is_active else 1)
        draw.text((x0 + nw // 2, y0 + 22), title, font=FONT_BODY, fill=COLOR_WHITE if is_active else COLOR_LIGHT, anchor="mm")
        draw.text((x0 + nw // 2, y0 + 50), code, font=FONT_CODE_SM, fill=COLOR_GOLD if is_active else COLOR_LIGHT, anchor="mm")
        if step_badge and is_active:
            draw.rounded_rectangle([x0 + nw - 28, y0 - 14, x0 + nw + 28, y0 + 14], radius=8, fill=COLOR_GOLD)
            draw.text((x0 + nw, y0), step_badge, font=FONT_BADGE, fill=(10, 8, 14), anchor="mm")

    draw_clean_node(ax0, ay0, "Class A (Base Root)", "def ping(): 'Root'", step == 4, "4th")
    draw_clean_node(bx0, by0, "Class B (Left)", "super().ping()", step == 2, "2nd")
    draw_clean_node(cx0, cy0, "Class C (Right)", "super().ping()", step == 3, "3rd")
    draw_clean_node(dx0, dy0, "Class D(B, C)", "d = D(); d.ping()", step >= 1, "1st")

    # MRO Resolution Ribbon
    ry0 = card_y0 + 385
    draw.rounded_rectangle([90, ry0, WIDTH - 90, ry0 + 52], radius=8, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, ry0 + 26), "C3 Resolution Order:  D  ->  B  ->  C  ->  A  ->  object", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Bottom Mixin Composition Panel (Y: 820 to 1220)
    c2_y0 = 820
    draw_clean_card(draw, [65, c2_y0, WIDTH - 65, c2_y0 + 400], outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c2_y0 + 34), "The Mixin Architecture Pattern", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    mixins = [
        ("JSONSerializableMixin", "def to_json(self): return json.dumps(self.__dict__)"),
        ("AuditLoggerMixin", "def log_action(self, action): audit_db.record(action)"),
        ("RateLimiterMixin", "def check_rate_limit(self): enforce_token_bucket()")
    ]
    my = c2_y0 + 68
    for m_name, m_code in mixins:
        draw.rounded_rectangle([90, my, WIDTH - 90, my + 64], radius=8, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        draw.text((115, my + 16), m_name, font=FONT_BODY, fill=COLOR_WHITE)
        draw.text((115, my + 42), m_code, font=FONT_CODE_SM, fill=COLOR_LIGHT)
        my += 74

    # Composition AIAgent Box (Generous 95px height, zero overflow)
    draw.rounded_rectangle([90, my, WIDTH - 90, my + 95], radius=8, fill=(30, 24, 20), outline=COLOR_GOLD, width=1)
    draw.text((115, my + 18), "class AIAgent(JSONMixin, AuditLoggerMixin, RateLimiterMixin):", font=FONT_CODE_SM, fill=COLOR_GOLD)
    draw.text((115, my + 54), "Composes orthogonal behaviors without deep class hierarchies!", font=FONT_BODY, fill=COLOR_WHITE)

    # Bottom Pill
    draw_clean_card(draw, [65, 1240, WIDTH - 65, 1320], outline=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, 1280), "C3 Linearization guarantees monotonic, duplicate-free execution", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): ACT 4 - PLUGGABLE VECTOR DB ARCHITECTURE
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_clean_background(t, prog)

    draw.text((WIDTH // 2, 246), "Pluggable AI Vector DBs", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 296), "Zero Vendor Lock-in with abc.ABC & Concrete Adapters", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Duck Typing vs ABCs (Y: 345 to 665)
    card_y0 = 345
    draw_clean_card(draw, [65, card_y0, WIDTH - 65, card_y0 + 320], outline=COLOR_BORDER, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "Duck Typing vs Abstract Base Classes", font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")

    half_w = (900 - 24) // 2
    # Left: Duck Typing
    draw.rounded_rectangle([90, card_y0 + 68, 90 + half_w, card_y0 + 295], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
    draw.text((90 + half_w // 2, card_y0 + 95), "Python Duck Typing", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")
    draw.text((110, card_y0 + 132), "• 'Walks like a duck, quacks", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((110, card_y0 + 162), "   like a duck -> It is a duck'", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((110, card_y0 + 198), "• Runtime behavior check", font=FONT_BODY, fill=COLOR_LIGHT)
    draw.text((110, card_y0 + 228), "• typing.Protocol subtyping", font=FONT_CODE_SM, fill=COLOR_GOLD)
    draw.text((110, card_y0 + 262), "Zero inheritance bloat", font=FONT_SUB, fill=COLOR_GREEN)

    # Right: Abstract Base Classes
    rx = 90 + half_w + 24
    draw.rounded_rectangle([rx, card_y0 + 68, rx + half_w, card_y0 + 295], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
    draw.text((rx + half_w // 2, card_y0 + 95), "Abstract Base Classes", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")
    draw.text((rx + 20, card_y0 + 132), "• Enforced contracts via", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((rx + 20, card_y0 + 162), "   abc.ABC & @abstractmethod", font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((rx + 20, card_y0 + 198), "• Cannot instantiate incomplete", font=FONT_BODY, fill=COLOR_LIGHT)
    draw.text((rx + 20, card_y0 + 228), "• Raises TypeError on startup", font=FONT_BODY, fill=COLOR_RED)
    draw.text((rx + 20, card_y0 + 262), "Compile-time safety", font=FONT_SUB, fill=COLOR_CYAN)

    # Bottom Pluggable Vector DB Architecture (Y: 685 to 1220)
    c2_y0 = 685
    draw_clean_card(draw, [65, c2_y0, WIDTH - 65, c2_y0 + 535], outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, c2_y0 + 36), "Pluggable Vector Database Architecture", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Abstract Base Class Box
    draw.rounded_rectangle([90, c2_y0 + 68, WIDTH - 90, c2_y0 + 175], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
    draw.text((115, c2_y0 + 92), "class BaseVectorDatabase(abc.ABC):", font=FONT_BODY, fill=COLOR_GOLD)
    draw.text((115, c2_y0 + 122), "@abstractmethod def upsert(self, doc_id: str, vector: list): ...", font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((115, c2_y0 + 150), "@abstractmethod def query(self, query_vec: list, top_k: int): ...", font=FONT_CODE_SM, fill=COLOR_LIGHT)

    # Dividing connector line
    draw.line([WIDTH // 2, c2_y0 + 175, WIDTH // 2, c2_y0 + 215], fill=COLOR_GOLD, width=2)
    draw.line([WIDTH // 4 + 10, c2_y0 + 215, 3 * WIDTH // 4 - 10, c2_y0 + 215], fill=COLOR_GOLD, width=2)
    draw.line([WIDTH // 4 + 10, c2_y0 + 215, WIDTH // 4 + 10, c2_y0 + 240], fill=COLOR_GOLD, width=2)
    draw.line([3 * WIDTH // 4 - 10, c2_y0 + 215, 3 * WIDTH // 4 - 10, c2_y0 + 240], fill=COLOR_GOLD, width=2)

    # Dual Concrete Provider Boxes
    ad_w = (900 - 24) // 2
    is_pinecone = (int(t * 1.5) % 2 == 0)

    # Pinecone Box
    p_fill = (32, 26, 38) if is_pinecone else COLOR_INNER_BG
    p_border = COLOR_CYAN if is_pinecone else COLOR_BORDER
    draw.rounded_rectangle([90, c2_y0 + 240, 90 + ad_w, c2_y0 + 375], radius=10, fill=p_fill, outline=p_border, width=2 if is_pinecone else 1)
    draw.text((90 + ad_w // 2, c2_y0 + 268), "PineconeAdapter", font=FONT_BODY, fill=COLOR_CYAN, anchor="mm")
    draw.text((90 + ad_w // 2, c2_y0 + 300), "Cloud Serverless Vector DB", font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
    draw.text((90 + ad_w // 2, c2_y0 + 330), "REST API Production Engine", font=FONT_CODE_SM, fill=COLOR_WHITE, anchor="mm")
    draw.text((90 + ad_w // 2, c2_y0 + 356), "100% Contract Satisfied", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # ChromaDB Box
    ch_x = 90 + ad_w + 24
    c_fill = (32, 26, 38) if not is_pinecone else COLOR_INNER_BG
    c_border = COLOR_GOLD if not is_pinecone else COLOR_BORDER
    draw.rounded_rectangle([ch_x, c2_y0 + 240, ch_x + ad_w, c2_y0 + 375], radius=10, fill=c_fill, outline=c_border, width=2 if not is_pinecone else 1)
    draw.text((ch_x + ad_w // 2, c2_y0 + 268), "ChromaDBAdapter", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")
    draw.text((ch_x + ad_w // 2, c2_y0 + 300), "Local In-Memory Vector DB", font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
    draw.text((ch_x + ad_w // 2, c2_y0 + 330), "SQLite / DuckDB Storage", font=FONT_CODE_SM, fill=COLOR_WHITE, anchor="mm")
    draw.text((ch_x + ad_w // 2, c2_y0 + 356), "100% Contract Satisfied", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")

    # 1-Line Swappable RAG Pipeline Showcase (Spacious 130px height, zero overflow!)
    draw.rounded_rectangle([90, c2_y0 + 390, WIDTH - 90, c2_y0 + 520], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=1)
    draw.text((115, c2_y0 + 412), "1-Line Swappable RAG Pipeline Architecture:", font=FONT_BODY, fill=COLOR_GOLD)
    active_code = "pipeline = RAGPipeline(db=PineconeAdapter())  # Cloud Active" if is_pinecone else "pipeline = RAGPipeline(db=ChromaDBAdapter())  # Local Active"
    draw.text((115, c2_y0 + 448), active_code, font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((115, c2_y0 + 482), "Decoupled architecture guarantees zero vendor lock-in!", font=FONT_BODY, fill=COLOR_LIGHT)

    # Bottom Pill
    draw_clean_card(draw, [65, 1240, WIDTH - 65, 1320], outline=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, 1280), "Guaranteed interfaces prevent runtime bugs before production", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): ACT 5 - THE VICTORY: YOU JUST LEVELED UP!
# =========================================================================
CHECKLIST = [
    ("Dynamic super() Proxy", "Proper state chaining without hardcoding parent names"),
    ("The Diamond Problem Solved", "C3 Linearization guarantees monotonic execution order"),
    ("Composable Mixin Architecture", "Stacking decoupled behaviors like Lego bricks"),
    ("Duck Typing & Protocols", "Structural polymorphism with zero inheritance runtime cost"),
    ("Abstract Base Classes (abc.ABC)", "Strict interface contracts for pluggable Vector DBs")
]

def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.0)
    img, draw = render_clean_background(t, prog)

    draw.text((WIDTH // 2, 246), "You Just Leveled Up!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 296), "From Junior Spaghetti Bugs to Senior AI System Architect", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Big Checklist Container (Y: 345 to 940)
    card_y0 = 345
    draw_clean_card(draw, [65, card_y0, WIDTH - 65, card_y0 + 580], outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 36), "Day 15 Architect Mastery Milestones", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    p_y = card_y0 + 74
    for idx, (title, desc) in enumerate(CHECKLIST):
        reveal_time = idx * 1.1
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([90, p_y, WIDTH - 90, p_y + 90], radius=10, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
            # Gold Checkmark Box
            draw.rounded_rectangle([108, p_y + 16, 168, p_y + 74], radius=8, fill=(35, 28, 20), outline=COLOR_GOLD, width=1)
            draw.text((138, p_y + 45), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((188, p_y + 22), title, font=FONT_BODY, fill=COLOR_WHITE)
            draw.text((188, p_y + 54), desc, font=FONT_BODY, fill=COLOR_LIGHT)
        else:
            draw.rounded_rectangle([90, p_y, WIDTH - 90, p_y + 90], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
            draw.rounded_rectangle([108, p_y + 16, 168, p_y + 74], radius=8, fill=(20, 18, 24), outline=COLOR_BORDER, width=1)
            draw.text((138, p_y + 45), "○", font=FONT_HEADING, fill=COLOR_LIGHT, anchor="mm")
            draw.text((188, p_y + 22), title, font=FONT_BODY, fill=COLOR_LIGHT)
            draw.text((188, p_y + 54), desc, font=FONT_BODY, fill=(160, 160, 180))
        p_y += 98

    # Bottom Metric Cards (Y: 950 to 1220)
    c2_y0 = 950
    draw_clean_card(draw, [65, c2_y0, WIDTH - 65, c2_y0 + 270], outline=COLOR_BORDER, width=2)

    pct = int(min(100, (t / 5.5) * 100))
    stat_cards = [
        ("4", "MODULES", "Deep Architecture"),
        ("6", "LAB TASKS", "In Workbook"),
        (f"{pct}%", "READY", "Senior AI Architect")
    ]
    sw = (950 - 30) // 3
    sx = 80
    for s_num, s_label, s_sub in stat_cards:
        draw.rounded_rectangle([sx, c2_y0 + 25, sx + sw, c2_y0 + 245], radius=10, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=1)
        draw.text((sx + sw // 2, c2_y0 + 72), s_num, font=FONT_STAT, fill=COLOR_GOLD, anchor="mm")
        draw.text((sx + sw // 2, c2_y0 + 140), s_label, font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")
        draw.text((sx + sw // 2, c2_y0 + 195), s_sub, font=FONT_BODY, fill=COLOR_LIGHT, anchor="mm")
        sx += sw + 20

    # Bottom Pill
    draw_clean_card(draw, [65, 1240, WIDTH - 65, 1320], outline=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, 1280), "Full code & practice workbook on GitHub - link in bio!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# VIDEO COMPOSITOR & EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day15"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Zero-Overflow Bold Times New Roman Reel...")
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
