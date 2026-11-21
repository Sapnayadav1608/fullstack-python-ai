"""
Day 15: Cinematic Storyline Tech Reel Generator (Bahnschrift & Modern Narrative)
================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: The Story of the 2 AM Production Outage
       How Junior OOP Mistakes Crash AI Apps, and How Senior Architects Fix Them
       (Inheritance, Dynamic super(), Diamond Problem, C3 MRO, Mixins & Vector DB ABCs)

Visual Design Highlights:
- Premium Typography: Windows Bahnschrift (Geometric DIN 1451) + Consolas Bold
- Story-Driven Narrative Arc (Hook -> The Trap -> The Boss Fight -> The Architect Solution -> Victory)
- Living Canvas: Drifting ambient glowing nebula orbs across all 5 scenes
- Kinetic Visuals:
  * Scene 1: Pulsing Crimson 2 AM Production Crash Alert Box + Architect Roadmap
  * Scene 2: Parent to Child Dynamic super() Proxy Chaining + Animated Typewriter
  * Scene 3: The Living Diamond Graph with traveling electric pulses & step debugger (D -> B -> C -> A)
  * Scene 4: Enterprise Pluggable Vector DB beam splitter (Live Pinecone <-> ChromaDB swap)
  * Scene 5: Animated Level-Up Milestones with satisfying pop-in checkmarks + 100% counter
- Strict Instagram Safe Zone: Content ends at Y <= 1320, Progress bar at Y = 1350
- Zero personal names on screen (Generic track branding)
- Pure silent video (audio=False) for recording real voiceover
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

# Premium Bahnschrift (Modern Geometric Sans) + Consolas Bold
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 52)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 26)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 23)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 25)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 50)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 19)

# Color Palette: Deep Dark Obsidian with Warm Amber / Electric Cyan / Vivid Coral
COLOR_BG_DARK = np.array([10, 8, 14], dtype=np.float32)
COLOR_CARD_BG = (18, 14, 22, 245)
COLOR_INNER_BG = (10, 8, 14, 255)

COLOR_WHITE = (255, 253, 248)
COLOR_CREAM = (254, 243, 199)
COLOR_MUTED = (165, 150, 165)
COLOR_AMBER = (245, 158, 11)
COLOR_GOLD = (251, 191, 36)
COLOR_ORANGE = (251, 146, 60)
COLOR_CORAL = (244, 63, 94)
COLOR_RED = (239, 68, 68)
COLOR_GREEN = (52, 211, 153)
COLOR_CYAN = (56, 189, 248)
COLOR_PURPLE = (192, 132, 252)


def ease_out(t):
    """Cubic ease-out for snappy cinematic animations."""
    t = np.clip(t, 0.0, 1.0)
    return 1.0 - (1.0 - t) ** 3.0


def render_dynamic_background(t, global_progress):
    """Living canvas with smoothly drifting atmospheric ambient glows."""
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    # Drifting Glow 1 (Warm Amber)
    cx1 = 180 + 70 * np.sin(t * 0.8)
    cy1 = 220 + 50 * np.cos(t * 0.7)
    d1 = np.sqrt((x - cx1)**2 + (y - cy1)**2)
    w1 = (np.clip(1.0 - d1 / 650.0, 0, 1) ** 2.8)[:, :, None]
    base += w1 * np.array([217, 119, 6], dtype=np.float32) * 0.40

    # Drifting Glow 2 (Electric Violet)
    cx2 = 880 + 80 * np.cos(t * 0.6)
    cy2 = 780 + 90 * np.sin(t * 0.5)
    d2 = np.sqrt((x - cx2)**2 + (y - cy2)**2)
    w2 = (np.clip(1.0 - d2 / 600.0, 0, 1) ** 3.0)[:, :, None]
    base += w2 * np.array([147, 51, 234], dtype=np.float32) * 0.35

    # Drifting Glow 3 (Cyan / Emerald)
    cx3 = 250 + 60 * np.sin(t * 0.5)
    cy3 = 1250 + 60 * np.cos(t * 0.6)
    d3 = np.sqrt((x - cx3)**2 + (y - cy3)**2)
    w3 = (np.clip(1.0 - d3 / 550.0, 0, 1) ** 3.0)[:, :, None]
    base += w3 * np.array([16, 185, 129], dtype=np.float32) * 0.25

    # High-Tech Micro Dot Grid
    dot_mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    dot_mask[::48, ::48] = True
    base[dot_mask] = np.clip(base[dot_mask] + 16, 0, 255)

    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 125 to 181)
    bx0, by0, bw, bh = (WIDTH - 580) // 2, 125, 580, 56
    draw.rounded_rectangle([bx0, by0, bx0 + bw, by0 + bh], radius=28, fill=(24, 16, 26, 240), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + bh // 2), "✨ DAY 15 / 30  •  THE AI PRODUCTION STORY", font=FONT_BADGE, fill=COLOR_CREAM, anchor="mm")

    # Subtitle Branding (NO PERSONAL NAME)
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar (Y: 1350 to 1360) - Safe above caption zone
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(24, 16, 24, 240), outline=(55, 38, 52, 180))
    fill_len = int(bar_w * global_progress)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)
        spark_x = min(70 + fill_len, 70 + bar_w)
        draw.ellipse([spark_x - 6, bar_y - 2, spark_x + 6, bar_y + 12], fill=(255, 240, 180, 255))

    return img, draw


def draw_glow_card(draw, bbox, fill, outline, glow_color=None, radius=20, width=2):
    """Draws a card with a sleek glowing border."""
    x0, y0, x1, y1 = bbox
    if glow_color:
        draw.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], radius=radius + 2, outline=(*glow_color[:3], 80), width=3)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=width)


# =========================================================================
# SCENE 1 (0 to 8s): ACT 1 - THE 2 AM PRODUCTION CRASH (The Hook)
# =========================================================================
def make_frame_scene_1(t):
    global_prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_dynamic_background(t, global_prog)

    # Dramatic Hero Hook in Bahnschrift
    draw.text((WIDTH // 2, 246), "WHY 90% OF AI APPS CRASH", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "The 2:00 AM OOP Bug That Blew Up A $10,000 Cloud Bill", font=FONT_SUB, fill=COLOR_CORAL, anchor="mm")

    # Dramatic Alert Box: Production Incident (Pops in immediately)
    cy0 = 340
    # Pulsing crimson border
    alert_pulse = (np.sin(t * 5.0) + 1.0) / 2.0
    alert_red = (int(200 + 55 * alert_pulse), int(40 * alert_pulse), int(60 * alert_pulse))
    draw_glow_card(draw, [80, cy0, WIDTH - 80, cy0 + 260], fill=(28, 12, 18, 250), outline=alert_red, glow_color=COLOR_RED, radius=20, width=3)

    # Incident Banner
    draw.rounded_rectangle([110, cy0 + 24, 380, cy0 + 64], radius=8, fill=(60, 15, 20), outline=COLOR_RED, width=1)
    draw.text((245, cy0 + 44), "🚨 INCIDENT #4092: 02:14 AM", font=FONT_MINI, fill=COLOR_RED, anchor="mm")
    draw.text((WIDTH // 2, cy0 + 95), "FATAL: Inconsistent Method Resolution Order (MRO)", font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")

    # Story explanation
    draw.rounded_rectangle([110, cy0 + 125, WIDTH - 110, cy0 + 235], radius=12, fill=COLOR_INNER_BG, outline=(80, 40, 50), width=1)
    draw.text((130, cy0 + 148), "• A Junior dev merged Multiple Inheritance without C3 awareness", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((130, cy0 + 178), "• Base class executed TWICE per prompt -> 5,000 duplicate LLM calls!", font=FONT_BODY, fill=COLOR_CORAL)
    draw.text((130, cy0 + 208), "• Memory leaked, model context corrupted, production crashed.", font=FONT_BODY, fill=COLOR_MUTED)

    # The Quest: The Senior Architect Solution (Pops in at 2.0s)
    if t > 2.0:
        ry0 = 625
        draw_glow_card(draw, [80, ry0, WIDTH - 80, ry0 + 590], fill=COLOR_CARD_BG, outline=COLOR_GOLD, glow_color=COLOR_GOLD, radius=20, width=2)
        draw.text((WIDTH // 2, ry0 + 36), "THE SENIOR ARCHITECT BLUEPRINT", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

        steps = [
            ("01", "Stop Hardcoding Parent Names", "Why super() is a dynamic runtime proxy", COLOR_GREEN),
            ("02", "Solve The Diamond Problem", "Master Python's C3 Linearization algorithm", COLOR_ORANGE),
            ("03", "Build Composable Mixins", "Stack orthogonal behaviors like Lego bricks", COLOR_CYAN),
            ("04", "Abstract Base Classes (abc.ABC)", "1-line swappable Vector DB adapter engine", COLOR_PURPLE)
        ]

        sy = ry0 + 72
        for num, title, desc, col in steps:
            draw.rounded_rectangle([110, sy, WIDTH - 110, sy + 88], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
            # Left Tag
            draw.rounded_rectangle([125, sy + 14, 185, sy + 74], radius=10, fill=(25, 18, 25), outline=col, width=1)
            draw.text((155, sy + 44), num, font=FONT_HEADING, fill=col, anchor="mm")
            # Text
            draw.text((205, sy + 24), title, font=FONT_SUB, fill=COLOR_WHITE)
            draw.text((205, sy + 54), desc, font=FONT_BODY, fill=COLOR_MUTED)
            sy += 102

        # Bottom Architecture Tag
        draw.rounded_rectangle([110, ry0 + 495, WIDTH - 110, ry0 + 560], radius=10, fill=(28, 20, 26), outline=COLOR_GOLD, width=1)
        draw.text((WIDTH // 2, ry0 + 527), "⚡ Level up your code from Junior Spaghetti to Senior Architecture!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Callout Pill (Y: 1240 to 1320)
    pulse = (np.sin(t * 4.0) + 1.0) / 2.0
    gold_val = int(180 + 75 * pulse)
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=(gold_val, int(gold_val * 0.75), 36), width=2)
    draw.text((WIDTH // 2, 1280), "🔥 Let's fix this architecture step by step! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): ACT 2 - THE HARDCODED TRAP & THE super() PROXY
# =========================================================================
def make_frame_scene_2(t):
    global_prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "The Hardcoded Parent Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Why AIModelClient.__init__(self) Destroys Multi-Class Scaling", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: The Rookie Trap vs The Fix (Y: 340 to 650)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 310], fill=COLOR_CARD_BG, outline=COLOR_CORAL, glow_color=COLOR_CORAL, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE CRIME: EXPLICIT HARDCODED CALLS", font=FONT_HEADING, fill=COLOR_CORAL, anchor="mm")

    # Mistake Box
    draw.rounded_rectangle([110, card_y0 + 64, WIDTH - 110, card_y0 + 155], radius=12, fill=COLOR_INNER_BG, outline=COLOR_RED, width=2)
    draw.text((130, card_y0 + 86), "❌ THE MISTAKE: AIModelClient.__init__(self, model_id)", font=FONT_CODE_SM, fill=COLOR_RED)
    draw.text((130, card_y0 + 118), "• Hardcodes class name -> Completely bypasses cooperative MRO!", font=FONT_BODY, fill=COLOR_MUTED)

    # Animated Energy Beam pulsing down from Mistake to Solution
    beam_t = (t * 2.5) % 1.0
    beam_y = card_y0 + 155 + int(beam_t * 40)
    draw.line([WIDTH // 2, card_y0 + 155, WIDTH // 2, card_y0 + 200], fill=(60, 45, 55), width=3)
    draw.line([WIDTH // 2, card_y0 + 155, WIDTH // 2, beam_y], fill=COLOR_GREEN, width=4)
    draw.ellipse([WIDTH // 2 - 5, beam_y - 5, WIDTH // 2 + 5, beam_y + 5], fill=COLOR_GOLD)
    draw.polygon([(WIDTH // 2 - 8, card_y0 + 192), (WIDTH // 2 + 8, card_y0 + 192), (WIDTH // 2, card_y0 + 204)], fill=COLOR_GREEN)

    # The Solution Box
    draw.rounded_rectangle([110, card_y0 + 205, WIDTH - 110, card_y0 + 295], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((130, card_y0 + 227), "✅ THE ARCHITECT FIX: super().__init__(model_id)", font=FONT_CODE_SM, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 258), "• super() is a DYNAMIC PROXY! It queries the MRO chain at runtime.", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Code Box with Dynamic Typewriter (Y: 670 to 1220)
    c_y0 = 670
    draw_glow_card(draw, [80, c_y0, WIDTH - 80, c_y0 + 550], fill=COLOR_CARD_BG, outline=COLOR_CYAN, glow_color=COLOR_CYAN, radius=20, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "THE DYNAMIC DISPATCH ENGINE", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    code_lines = [
        ("class FineTunedClient(AIModelClient):", COLOR_GOLD),
        ("    def __init__(self, model_id, lora_adapter):", COLOR_WHITE),
        ("        # 1. Cooperative MRO initialization", COLOR_MUTED),
        ("        super().__init__(model_id=model_id)", COLOR_GREEN),
        ("        self.lora_adapter = lora_adapter", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("    def generate(self, prompt: str):", COLOR_GOLD),
        ("        # 2. Dynamic runtime method extension", COLOR_MUTED),
        ("        raw = super().generate(prompt)", COLOR_CYAN),
        ("        return self.lora_adapter.apply(raw)", COLOR_ORANGE),
        ("", COLOR_WHITE),
        ("# CPython resolves the next class dynamically!", COLOR_MUTED),
        ("print(FineTunedClient.mro())", COLOR_GOLD)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = c_y0 + 64
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((105, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_MUTED)
        draw.line([145, cur_y - 2, 145, cur_y + 24], fill=(55, 40, 52), width=1)

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
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1280), "💡 super() searches the NEXT class in instance MRO at runtime!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): ACT 3 - THE BOSS FIGHT: THE DIAMOND TRAP & C3 MRO
# =========================================================================
def make_frame_scene_3(t):
    global_prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "The Infamous Diamond Trap", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "How C3 Linearization Guarantees Zero Duplicate Method Calls", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Center Flowchart: The Living Diamond Graph (Y: 340 to 800)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 460], fill=COLOR_CARD_BG, outline=COLOR_ORANGE, glow_color=COLOR_ORANGE, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE DIAMOND INHERITANCE GRAPH", font=FONT_HEADING, fill=COLOR_ORANGE, anchor="mm")

    step = 0
    if t >= 6.0:
        step = 4
    elif t >= 4.5:
        step = 3
    elif t >= 3.0:
        step = 2
    elif t >= 1.5:
        step = 1

    nw, nh = 270, 72
    ax0 = WIDTH // 2 - nw // 2
    ay0 = card_y0 + 64
    bx0 = 110
    by0 = card_y0 + 180
    cx0 = WIDTH - 110 - nw
    cy0 = card_y0 + 180
    dx0 = WIDTH // 2 - nw // 2
    dy0 = card_y0 + 295

    # Glowing Connecting Diamond Lines with Traveling Energy Packets
    pulse_t = (t * 3.0) % 1.0

    def draw_pulsing_line(p1, p2, col, is_firing):
        draw.line([p1[0], p1[1], p2[0], p2[1]], fill=(60, 45, 60), width=3)
        if is_firing:
            draw.line([p1[0], p1[1], p2[0], p2[1]], fill=col, width=3)
            px = int(p1[0] + (p2[0] - p1[0]) * pulse_t)
            py = int(p1[1] + (p2[1] - p1[1]) * pulse_t)
            draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=COLOR_WHITE)

    draw_pulsing_line((dx0 + nw // 4, dy0), (bx0 + nw // 2, by0 + nh), COLOR_CYAN, step >= 2)
    draw_pulsing_line((dx0 + 3 * nw // 4, dy0), (cx0 + nw // 2, cy0 + nh), COLOR_PURPLE, step >= 3)
    draw_pulsing_line((bx0 + nw // 2, by0), (ax0 + nw // 4, ay0 + nh), COLOR_AMBER, step >= 4)
    draw_pulsing_line((cx0 + nw // 2, cy0), (ax0 + 3 * nw // 4, ay0 + nh), COLOR_AMBER, step >= 4)

    def draw_node(x0, y0, title, code, col, active, step_label=None):
        outline = col if active else (70, 50, 70)
        glow = col if active else None
        draw_glow_card(draw, [x0, y0, x0 + nw, y0 + nh], fill=COLOR_INNER_BG, outline=outline, glow_color=glow, radius=12, width=3 if active else 1)
        draw.text((x0 + nw // 2, y0 + 22), title, font=FONT_SUB, fill=col if active else COLOR_MUTED, anchor="mm")
        draw.text((x0 + nw // 2, y0 + 50), code, font=FONT_CODE_SM, fill=COLOR_WHITE if active else (130, 115, 125), anchor="mm")
        if step_label and active:
            draw.rounded_rectangle([x0 + nw - 30, y0 - 14, x0 + nw + 30, y0 + 14], radius=14, fill=col)
            draw.text((x0 + nw, y0), step_label, font=FONT_CODE_SM, fill=(10, 8, 12), anchor="mm")

    draw_node(ax0, ay0, "Class A (Base Root)", "def ping(): 'Root'", COLOR_AMBER, step == 4, "4th")
    draw_node(bx0, by0, "Class B (Left)", "super().ping()", COLOR_CYAN, step == 2, "2nd")
    draw_node(cx0, cy0, "Class C (Right)", "super().ping()", COLOR_PURPLE, step == 3, "3rd")
    draw_node(dx0, dy0, "Class D(B, C)", "d = D(); d.ping()", COLOR_GREEN, step >= 1, "1st")

    # MRO Dynamic Resolution Ribbon (Lights up sequentially)
    ry0 = card_y0 + 390
    draw.rounded_rectangle([100, ry0, WIDTH - 100, ry0 + 54], radius=12, fill=(28, 18, 28), outline=COLOR_GOLD, width=1)
    
    badges = [
        ("D", COLOR_GREEN, step >= 1),
        ("→", COLOR_MUTED, True),
        ("B", COLOR_CYAN, step >= 2),
        ("→", COLOR_MUTED, True),
        ("C", COLOR_PURPLE, step >= 3),
        ("→", COLOR_MUTED, True),
        ("A", COLOR_AMBER, step >= 4),
        ("→", COLOR_MUTED, True),
        ("object", COLOR_WHITE, step >= 4)
    ]
    cur_rx = 135
    draw.text((cur_rx, ry0 + 27), "MRO: ", font=FONT_SUB, fill=COLOR_GOLD, anchor="lm")
    cur_rx += 75
    for txt, col, active in badges:
        text_col = col if active else (90, 75, 85)
        draw.text((cur_rx, ry0 + 27), txt, font=FONT_HEADING if len(txt) == 1 and txt != "→" else FONT_SUB, fill=text_col, anchor="lm")
        cur_rx += 52

    # Bottom Mixin Composition Architecture Card (Y: 820 to 1220)
    c_y0 = 820
    draw_glow_card(draw, [80, c_y0, WIDTH - 80, c_y0 + 400], fill=COLOR_CARD_BG, outline=COLOR_PURPLE, glow_color=COLOR_PURPLE, radius=20, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "THE MIXIN ARCHITECTURE PATTERN", font=FONT_HEADING, fill=COLOR_PURPLE, anchor="mm")

    mixins = [
        ("JSONSerializableMixin", "def to_json(self): return json.dumps(self.__dict__)", COLOR_CYAN),
        ("AuditLoggerMixin", "def log_action(self, action): audit_db.record(action)", COLOR_AMBER),
        ("RateLimiterMixin", "def check_rate_limit(self): enforce_token_bucket()", COLOR_GREEN)
    ]
    my = c_y0 + 64
    for m_name, m_code, m_col in mixins:
        draw.rounded_rectangle([110, my, WIDTH - 110, my + 64], radius=10, fill=COLOR_INNER_BG, outline=m_col, width=1)
        draw.text((130, my + 14), f"🧩 {m_name}", font=FONT_SUB, fill=m_col)
        draw.text((130, my + 38), m_code, font=FONT_CODE_SM, fill=COLOR_MUTED)
        my += 74

    # Composition Agent
    draw.rounded_rectangle([110, my, WIDTH - 110, my + 80], radius=10, fill=(28, 16, 26), outline=COLOR_GOLD, width=2)
    draw.text((130, my + 16), "class AIAgent(JSONMixin, AuditLoggerMixin, RateLimiterMixin):", font=FONT_CODE_SM, fill=COLOR_GOLD)
    draw.text((130, my + 46), "✓ Composes clean, decoupled behavior without inheritance hierarchy bloat!", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Pill
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1280), "⚡ C3 Linearization guarantees monotonic, duplicate-free execution!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): ACT 4 - SENIOR ARCHITECTURE: PLUGGABLE VECTOR DBS
# =========================================================================
def make_frame_scene_4(t):
    global_prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "Pluggable AI Vector DBs", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Zero Vendor Lock-in with abc.ABC & Concrete Adapters", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Split Card: Duck Typing vs ABCs (Y: 340 to 670)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 330], fill=COLOR_CARD_BG, outline=COLOR_CORAL, glow_color=COLOR_CORAL, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DUCK TYPING VS ABSTRACT BASE CLASSES", font=FONT_HEADING, fill=COLOR_CORAL, anchor="mm")

    half_w = (WIDTH - 200 - 24) // 2
    # Left Card: Duck Typing
    draw.rounded_rectangle([110, card_y0 + 64, 110 + half_w, card_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((110 + half_w // 2, card_y0 + 92), "🦆 Duck Typing", font=FONT_SUB, fill=COLOR_AMBER, anchor="mm")
    draw.text((130, card_y0 + 128), "• 'Walks like a duck, quacks", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((130, card_y0 + 158), "   like a duck → It's a duck'", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((130, card_y0 + 196), "• Runtime behavior check", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((130, card_y0 + 226), "• Structural Subtyping via", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((130, card_y0 + 254), "   typing.Protocol", font=FONT_CODE_SM, fill=COLOR_GOLD)
    draw.text((130, card_y0 + 284), "⚡ Zero inheritance bloat", font=FONT_BODY, fill=COLOR_GREEN)

    # Right Card: Abstract Base Classes
    rx = 110 + half_w + 24
    draw.rounded_rectangle([rx, card_y0 + 64, rx + half_w, card_y0 + 310], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CORAL, width=2)
    draw.text((rx + half_w // 2, card_y0 + 92), "🛡️ Abstract Base Classes", font=FONT_SUB, fill=COLOR_CORAL, anchor="mm")
    draw.text((rx + 20, card_y0 + 128), "• Enforced contracts via", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((rx + 20, card_y0 + 158), "   abc.ABC & @abstractmethod", font=FONT_CODE_SM, fill=COLOR_CORAL)
    draw.text((rx + 20, card_y0 + 196), "• Cannot instantiate incomplete!", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((rx + 20, card_y0 + 226), "• Instantly raises TypeError", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((rx + 20, card_y0 + 254), "   if missing implementation", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((rx + 20, card_y0 + 284), "🔒 Startup compile safety", font=FONT_BODY, fill=COLOR_CYAN)

    # Bottom Flowchart Card: The Enterprise Vector DB Adapter Architecture (Y: 690 to 1220)
    c_y0 = 690
    draw_glow_card(draw, [80, c_y0, WIDTH - 80, c_y0 + 530], fill=COLOR_CARD_BG, outline=COLOR_GREEN, glow_color=COLOR_GREEN, radius=20, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "PLUGGABLE VECTOR DATABASE ARCHITECTURE", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Abstract Base Class Box
    draw.rounded_rectangle([110, c_y0 + 64, WIDTH - 110, c_y0 + 175], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((130, c_y0 + 86), "class BaseVectorDatabase(abc.ABC):", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((130, c_y0 + 118), "  @abstractmethod def upsert(self, doc_id: str, vector: list): ...", font=FONT_CODE_SM, fill=COLOR_CREAM)
    draw.text((130, c_y0 + 146), "  @abstractmethod def query(self, query_vec: list, top_k: int): ...", font=FONT_CODE_SM, fill=COLOR_MUTED)

    # Dynamic Beam Splitter to Concrete Adapters
    draw.line([WIDTH // 2, c_y0 + 175, WIDTH // 2, c_y0 + 215], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 30, c_y0 + 215, 3 * WIDTH // 4 - 30, c_y0 + 215], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 30, c_y0 + 215, WIDTH // 4 + 30, c_y0 + 240], fill=COLOR_CYAN, width=3)
    draw.line([3 * WIDTH // 4 - 30, c_y0 + 215, 3 * WIDTH // 4 - 30, c_y0 + 240], fill=COLOR_AMBER, width=3)

    # Dual Concrete Provider Boxes
    ad_w = (WIDTH - 220 - 24) // 2
    is_pinecone_active = (int(t * 1.5) % 2 == 0)
    pine_border = COLOR_CYAN if is_pinecone_active else (60, 45, 60)
    draw.rounded_rectangle([110, c_y0 + 240, 110 + ad_w, c_y0 + 380], radius=12, fill=COLOR_INNER_BG, outline=pine_border, width=2)
    draw.text((110 + ad_w // 2, c_y0 + 268), "PineconeAdapter", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")
    draw.text((110 + ad_w // 2, c_y0 + 300), "Cloud Serverless Vector DB", font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
    draw.text((110 + ad_w // 2, c_y0 + 332), "REST API Production Engine", font=FONT_CODE_SM, fill=COLOR_CREAM, anchor="mm")
    draw.text((110 + ad_w // 2, c_y0 + 360), "✓ Full Contract Implemented", font=FONT_BODY, fill=COLOR_GREEN, anchor="mm")

    # ChromaDB
    chroma_border = COLOR_AMBER if not is_pinecone_active else (60, 45, 60)
    ch_x = 110 + ad_w + 24
    draw.rounded_rectangle([ch_x, c_y0 + 240, ch_x + ad_w, c_y0 + 380], radius=12, fill=COLOR_INNER_BG, outline=chroma_border, width=2)
    draw.text((ch_x + ad_w // 2, c_y0 + 268), "ChromaDBAdapter", font=FONT_SUB, fill=COLOR_AMBER, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 300), "Local In-Memory Vector DB", font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 332), "SQLite / DuckDB Storage", font=FONT_CODE_SM, fill=COLOR_CREAM, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 360), "✓ Full Contract Implemented", font=FONT_BODY, fill=COLOR_GREEN, anchor="mm")

    # Dynamic Switcher Showcase Ribbon
    draw.rounded_rectangle([110, c_y0 + 400, WIDTH - 110, c_y0 + 505], radius=12, fill=(28, 18, 24), outline=COLOR_GOLD, width=1)
    draw.text((130, c_y0 + 424), "💡 1-Line Swappable RAG Pipeline:", font=FONT_SUB, fill=COLOR_GOLD)
    active_code = "pipeline = RAGPipeline(db=PineconeAdapter())  # Cloud Active" if is_pinecone_active else "pipeline = RAGPipeline(db=ChromaDBAdapter())  # Local Active"
    draw.text((130, c_y0 + 458), active_code, font=FONT_CODE_SM, fill=COLOR_WHITE)
    draw.text((130, c_y0 + 486), "→ Decoupled architecture prevents vendor lock-in completely!", font=FONT_BODY, fill=COLOR_GREEN)

    # Bottom Pill
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1280), "🔒 Guaranteed API interfaces prevent runtime bugs before production!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): ACT 5 - THE VICTORY: YOU JUST LEVELED UP!
# =========================================================================
CHECKLIST = [
    ("Dynamic super() Proxy", "Proper state chaining without hardcoding parent names", COLOR_GREEN),
    ("The Diamond Problem Solved", "C3 Linearization guarantees monotonic execution order", COLOR_ORANGE),
    ("Composable Mixin Architecture", "Stacking decoupled behaviors like Lego bricks", COLOR_CYAN),
    ("Duck Typing & Protocols", "Structural polymorphism with zero inheritance runtime cost", COLOR_CORAL),
    ("Abstract Base Classes (abc.ABC)", "Strict interface contracts for pluggable Vector DBs", COLOR_GOLD)
]

def make_frame_scene_5(t):
    global_prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.0)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "YOU JUST LEVELED UP!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "From Junior Spaghetti Bugs to Senior AI System Architect", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Big Checklist Container (Y: 340 to 930)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 580], fill=COLOR_CARD_BG, outline=COLOR_GOLD, glow_color=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "DAY 15 ARCHITECT MASTERY MILESTONES", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    p_y = card_y0 + 72
    for idx, (title, desc, col) in enumerate(CHECKLIST):
        reveal_time = idx * 1.1
        is_revealed = (t >= reveal_time)
        
        if is_revealed:
            draw.rounded_rectangle([105, p_y, WIDTH - 105, p_y + 90], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
            draw.rounded_rectangle([125, p_y + 16, 185, p_y + 74], radius=10, fill=(20, 40, 26), outline=col, width=2)
            draw.text((155, p_y + 45), "✓", font=FONT_HEADING, fill=col, anchor="mm")
            draw.text((205, p_y + 22), title, font=FONT_SUB, fill=COLOR_WHITE)
            draw.text((205, p_y + 54), desc, font=FONT_BODY, fill=COLOR_MUTED)
        else:
            draw.rounded_rectangle([105, p_y, WIDTH - 105, p_y + 90], radius=12, fill=(16, 12, 18), outline=(50, 35, 48), width=1)
            draw.rounded_rectangle([125, p_y + 16, 185, p_y + 74], radius=10, fill=(18, 14, 20), outline=(65, 48, 60), width=1)
            draw.text((155, p_y + 45), "○", font=FONT_HEADING, fill=COLOR_MUTED, anchor="mm")
            draw.text((205, p_y + 22), title, font=FONT_SUB, fill=(110, 95, 105))
            draw.text((205, p_y + 54), desc, font=FONT_BODY, fill=(80, 68, 76))
        p_y += 98

    # Metric Cards (Y: 940 to 1220)
    c_y0 = 940
    draw_glow_card(draw, [80, c_y0, WIDTH - 80, c_y0 + 280], fill=COLOR_CARD_BG, outline=COLOR_AMBER, glow_color=COLOR_AMBER, radius=20, width=2)

    pct = int(min(100, (t / 5.5) * 100))
    stat_cards = [
        ("4", "MODULES", "Architecture Deep Dive", COLOR_GREEN),
        ("6", "LAB TASKS", "In Workbook", COLOR_CYAN),
        (f"{pct}%", "READY", "Senior AI Architect", COLOR_GOLD)
    ]
    sw = (WIDTH - 160 - 30) // 3
    sx = 95
    for s_num, s_label, s_sub, s_col in stat_cards:
        draw.rounded_rectangle([sx, c_y0 + 25, sx + sw, c_y0 + 255], radius=14, fill=COLOR_INNER_BG, outline=s_col, width=2)
        draw.text((sx + sw // 2, c_y0 + 75), s_num, font=FONT_STAT, fill=s_col, anchor="mm")
        draw.text((sx + sw // 2, c_y0 + 145), s_label, font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")
        draw.text((sx + sw // 2, c_y0 + 205), s_sub, font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
        sx += sw + 20

    # Bottom Pill
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1280), "⭐ Code & Practice Workbook on GitHub! Link in bio / comments! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# VIDEO COMPOSITOR & EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day15"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Day 15 Storyline Tech Reel (Bahnschrift & Motion)...")
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
