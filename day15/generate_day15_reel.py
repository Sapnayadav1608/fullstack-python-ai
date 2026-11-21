"""
Day 15: High-Production Creative AI Motion Reel Generator (HyperFrames Style)
=============================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: Advanced Object-Oriented Programming (OOP) Part 2
       Inheritance, Diamond Problem & C3 MRO, Mixins, Polymorphism & ABCs

Key Visual Innovations (High-Energy Motion Graphics):
- Living Canvas: Dynamic drifting ambient nebula glows across all frames
- Spring Physics: Smooth ease-out entrances (no jarring jumps, no static slides)
- Living Diamond Graph (Scene 3):
  * Electric energy pulses travel along inheritance lines
  * Step-by-step MRO debugger trace: Nodes D -> B -> C -> A illuminate sequentially
  * Glowing neon halos around active classes
- Dynamic Typewriter & State Chaining (Scene 2):
  * Parent to child animated energy beam
  * Code types out character-by-character with glowing amber cursor
  * Glowing dynamic proxy badges
- Pluggable Adapter Switcher (Scene 4):
  * Dynamic beam splitter from Abstract Base Class
  * Live interactive swap between Pinecone & ChromaDB
- Kinetic Mastery Checklist & Counter (Scene 5):
  * Staggered animated checkmarks popping in with spring scale
  * Real-time counter ticking up to 100%
- Strict Instagram Safe Zone: Content ends at Y <= 1320, Progress bar at Y = 1350
- Zero Personal Names on Screen (Generic Track Branding)
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

# Bold, High-Contrast Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 32)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 23)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 26)
FONT_CODE_SM = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 22)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 46)

# Colors
COLOR_BG_DARK = np.array([10, 8, 12], dtype=np.float32)
COLOR_CARD_BG = (18, 14, 22, 245)
COLOR_INNER_BG = (10, 8, 14, 255)

COLOR_WHITE = (255, 253, 248)
COLOR_CREAM = (254, 243, 199)
COLOR_MUTED = (165, 150, 165)
COLOR_AMBER = (245, 158, 11)
COLOR_GOLD = (251, 191, 36)
COLOR_ORANGE = (251, 146, 60)
COLOR_CORAL = (244, 63, 94)
COLOR_GREEN = (52, 211, 153)
COLOR_CYAN = (56, 189, 248)
COLOR_PURPLE = (192, 132, 252)


def ease_out(t):
    """Snappy cubic ease-out for smooth animations."""
    t = np.clip(t, 0.0, 1.0)
    return 1.0 - (1.0 - t) ** 3.0


def ease_in_out(t):
    """Smooth sigmoid-like easing."""
    t = np.clip(t, 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def render_dynamic_background(t, global_progress):
    """
    Renders a living canvas: subtle ambient glowing nebula lights that drift smoothly,
    creating dynamic depth across every frame.
    """
    y, x = np.ogrid[:HEIGHT, :WIDTH]
    base = np.zeros((HEIGHT, WIDTH, 3), dtype=np.float32)
    base[:, :] = COLOR_BG_DARK

    # Drifting Orb 1 (Warm Amber, Top-Left)
    cx1 = 180 + 70 * np.sin(t * 0.8)
    cy1 = 220 + 50 * np.cos(t * 0.7)
    d1 = np.sqrt((x - cx1)**2 + (y - cy1)**2)
    w1 = (np.clip(1.0 - d1 / 650.0, 0, 1) ** 2.8)[:, :, None]
    base += w1 * np.array([217, 119, 6], dtype=np.float32) * 0.45

    # Drifting Orb 2 (Violet / Indigo, Center-Right)
    cx2 = 880 + 80 * np.cos(t * 0.6)
    cy2 = 780 + 90 * np.sin(t * 0.5)
    d2 = np.sqrt((x - cx2)**2 + (y - cy2)**2)
    w2 = (np.clip(1.0 - d2 / 600.0, 0, 1) ** 3.0)[:, :, None]
    base += w2 * np.array([147, 51, 234], dtype=np.float32) * 0.35

    # Drifting Orb 3 (Emerald / Cyan, Bottom-Left)
    cx3 = 250 + 60 * np.sin(t * 0.5)
    cy3 = 1250 + 60 * np.cos(t * 0.6)
    d3 = np.sqrt((x - cx3)**2 + (y - cy3)**2)
    w3 = (np.clip(1.0 - d3 / 550.0, 0, 1) ** 3.0)[:, :, None]
    base += w3 * np.array([16, 185, 129], dtype=np.float32) * 0.25

    # High-Tech Micro Dot Grid
    dot_mask = np.zeros((HEIGHT, WIDTH), dtype=bool)
    dot_mask[::48, ::48] = True
    base[dot_mask] = np.clip(base[dot_mask] + 18, 0, 255)

    img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(img, "RGBA")

    # Persistent HUD Header Badge (Y: 125 to 181)
    bx0, by0, bw, bh = (WIDTH - 580) // 2, 125, 580, 56
    draw.rounded_rectangle([bx0, by0, bx0 + bw, by0 + bh], radius=28, fill=(24, 16, 26, 240), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + bh // 2), "✨ DAY 15 / 30  •  PRODUCTION OOP", font=FONT_BADGE, fill=COLOR_CREAM, anchor="mm")

    # Subtitle Branding (NO PERSONAL NAME)
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar (Y: 1350 to 1360) - Safe above caption zone
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(24, 16, 24, 240), outline=(55, 38, 52, 180))
    fill_len = int(bar_w * global_progress)
    if fill_len > 0:
        # Gradient glowing head
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)
        # Glowing head spark
        spark_x = min(70 + fill_len, 70 + bar_w)
        draw.ellipse([spark_x - 6, bar_y - 2, spark_x + 6, bar_y + 12], fill=(255, 240, 180, 255))

    return img, draw


def draw_glow_card(draw, bbox, fill, outline, glow_color=None, radius=20, width=2):
    """Draws a card with a sleek glowing border."""
    x0, y0, x1, y1 = bbox
    if glow_color:
        # Subtle outer neon halo
        draw.rounded_rectangle([x0 - 2, y0 - 2, x1 + 2, y1 + 2], radius=radius + 2, outline=(*glow_color[:3], 80), width=3)
    draw.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline, width=width)


# =========================================================================
# SCENE 1 (0 to 8s): HIGH-ENERGY HOOK & 4-PILLAR ROADMAP (Dynamic Pop-in)
# =========================================================================
def make_frame_scene_1(t):
    global_prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_dynamic_background(t, global_prog)

    # Animated Title Entrance
    title_scale = ease_out(t / 0.8)
    draw.text((WIDTH // 2, 246), "Object-Oriented Python", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Advanced Architecture • MRO • Mixins • ABCs", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # 4 Modular Pillars that animate in with staggered spring delays
    pillars = [
        ("01", "INHERITANCE & super()", "Dynamic MRO proxy & parent state chaining", COLOR_GREEN, 0.4),
        ("02", "THE DIAMOND PROBLEM", "C3 Linearization algorithm & zero duplicate calls", COLOR_ORANGE, 0.9),
        ("03", "POLYMORPHISM & PROTOCOLS", "Method overriding & Pythonic Duck Typing", COLOR_CYAN, 1.4),
        ("04", "ABSTRACT BASE CLASSES", "Pluggable Vector DB architecture (abc.ABC)", COLOR_CORAL, 1.9)
    ]

    p_y = 350
    for num, title, desc, col, delay in pillars:
        prog = ease_out((t - delay) / 0.6)
        if prog > 0:
            # Slide in from left
            x_offset = int((1.0 - prog) * -300)
            box_x0 = 80 + x_offset
            box_x1 = WIDTH - 80 + x_offset
            
            draw_glow_card(draw, [box_x0, p_y, box_x1, p_y + 90], fill=COLOR_CARD_BG, outline=col, glow_color=col, radius=16, width=2)
            # Left Tag
            draw.rounded_rectangle([box_x0 + 16, p_y + 16, box_x0 + 95, p_y + 74], radius=10, fill=COLOR_INNER_BG, outline=col, width=1)
            draw.text((box_x0 + 55, p_y + 45), num, font=FONT_HEADING, fill=col, anchor="mm")
            # Text
            draw.text((box_x0 + 115, p_y + 24), title, font=FONT_SUB, fill=COLOR_WHITE)
            draw.text((box_x0 + 115, p_y + 54), desc, font=FONT_BODY, fill=COLOR_MUTED)
        p_y += 106

    # Bottom Hero Visual: The Enterprise Adapter Showcase Card (Pops in at 2.4s)
    if t > 2.4:
        c_prog = ease_out((t - 2.4) / 0.7)
        cy0 = 800
        draw_glow_card(draw, [80, cy0, WIDTH - 80, cy0 + 410], fill=COLOR_CARD_BG, outline=COLOR_AMBER, glow_color=COLOR_AMBER, radius=20, width=2)
        draw.text((WIDTH // 2, cy0 + 36), "ENTERPRISE PLUGGABLE ARCHITECTURE", font=FONT_HEADING, fill=COLOR_AMBER, anchor="mm")

        # Visual Interface Box
        draw.rounded_rectangle([110, cy0 + 74, WIDTH - 110, cy0 + 165], radius=12, fill=COLOR_INNER_BG, outline=COLOR_CORAL, width=2)
        draw.text((130, cy0 + 96), "INTERFACE: BaseVectorDatabase (ABC)", font=FONT_SUB, fill=COLOR_CORAL)
        draw.text((130, cy0 + 130), "@abstractmethod def query(vector) -> list", font=FONT_CODE_SM, fill=COLOR_CREAM)

        # Pulsing Beam from Interface to Adapters
        beam_pulse = (np.sin(t * 6.0) + 1.0) / 2.0
        beam_col = (int(251 * beam_pulse), 191, 36)
        draw.line([WIDTH // 2, cy0 + 165, WIDTH // 2, cy0 + 215], fill=beam_col, width=4)
        draw.polygon([(WIDTH // 2 - 8, cy0 + 205), (WIDTH // 2 + 8, cy0 + 205), (WIDTH // 2, cy0 + 218)], fill=beam_col)

        # Dual Adapter Cards
        bw = (WIDTH - 220 - 24) // 2
        # Pinecone
        draw.rounded_rectangle([110, cy0 + 220, 110 + bw, cy0 + 330], radius=12, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
        draw.text((110 + bw // 2, cy0 + 248), "PineconeAdapter", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")
        draw.text((110 + bw // 2, cy0 + 282), "Cloud Serverless Vector DB", font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
        draw.text((110 + bw // 2, cy0 + 308), "✓ 100% Contract Satisfied", font=FONT_BODY, fill=COLOR_GREEN, anchor="mm")

        # ChromaDB
        cx2 = 110 + bw + 24
        draw.rounded_rectangle([cx2, cy0 + 220, cx2 + bw, cy0 + 330], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
        draw.text((cx2 + bw // 2, cy0 + 248), "ChromaDBAdapter", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
        draw.text((cx2 + bw // 2, cy0 + 282), "Local Embedded Vector DB", font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
        draw.text((cx2 + bw // 2, cy0 + 308), "✓ Zero Vendor Lock-in", font=FONT_BODY, fill=COLOR_GOLD, anchor="mm")

        # Plug and play tag
        draw.rounded_rectangle([110, cy0 + 348, WIDTH - 110, cy0 + 392], radius=8, fill=(28, 20, 26), outline=COLOR_PURPLE, width=1)
        draw.text((WIDTH // 2, cy0 + 370), "⚡ Switch vector backends with a 1-line configuration change!", font=FONT_BODY, fill=COLOR_CREAM, anchor="mm")

    # Bottom Callout Pill (Y: 1240 to 1320)
    pulse = (np.sin(t * 4.0) + 1.0) / 2.0
    gold_val = int(180 + 75 * pulse)
    draw.rounded_rectangle([70, 1240, WIDTH - 70, 1320], radius=22, fill=(22, 15, 22, 245), outline=(gold_val, int(gold_val * 0.75), 36), width=2)
    draw.text((WIDTH // 2, 1280), "🔥 Day 15 is live! Master Production OOP Architecture! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 - INHERITANCE & DYNAMIC super() PROXY
# =========================================================================
def make_frame_scene_2(t):
    global_prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "Inheritance & State Chaining", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Why super() is a Dynamic Proxy, Not a Hardcoded Parent Reference", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Flowchart Card: Parent -> Child Component Flow (Y: 340 to 650)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 310], fill=COLOR_CARD_BG, outline=COLOR_GREEN, glow_color=COLOR_GREEN, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "COOPERATIVE PARENT-CHILD DELEGATION", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Parent Class Box
    draw.rounded_rectangle([110, card_y0 + 60, WIDTH - 110, card_y0 + 140], radius=12, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((130, card_y0 + 82), "class AIModelClient:", font=FONT_SUB, fill=COLOR_AMBER)
    draw.text((130, card_y0 + 112), "  def __init__(self, model_id, api_key): self.model_id = model_id", font=FONT_CODE_SM, fill=COLOR_CREAM)

    # Animated Energy Beam pulsing down from Parent to Child
    beam_t = (t * 2.5) % 1.0
    beam_y = card_y0 + 140 + int(beam_t * 50)
    draw.line([WIDTH // 2, card_y0 + 140, WIDTH // 2, card_y0 + 195], fill=(55, 40, 50), width=3)
    draw.line([WIDTH // 2, card_y0 + 140, WIDTH // 2, beam_y], fill=COLOR_GREEN, width=4)
    draw.ellipse([WIDTH // 2 - 5, beam_y - 5, WIDTH // 2 + 5, beam_y + 5], fill=COLOR_GOLD)
    draw.polygon([(WIDTH // 2 - 8, card_y0 + 185), (WIDTH // 2 + 8, card_y0 + 185), (WIDTH // 2, card_y0 + 197)], fill=COLOR_GREEN)

    # Child Subclass Box
    draw.rounded_rectangle([110, card_y0 + 200, WIDTH - 110, card_y0 + 285], radius=12, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((130, card_y0 + 222), "class FineTunedGeminiClient(AIModelClient):", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((130, card_y0 + 254), "  super().__init__(model_id, api_key)  # State Chained!", font=FONT_CODE_SM, fill=COLOR_GOLD)

    # Bottom Code Box with Dynamic Typewriter (Y: 670 to 1220)
    c_y0 = 670
    draw_glow_card(draw, [80, c_y0, WIDTH - 80, c_y0 + 550], fill=COLOR_CARD_BG, outline=COLOR_CYAN, glow_color=COLOR_CYAN, radius=20, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "THE DYNAMIC DISPATCH ENGINE", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    code_lines = [
        ("class FineTunedClient(AIModelClient):", COLOR_GOLD),
        ("    def __init__(self, model, adapter):", COLOR_WHITE),
        ("        # 1. Cooperative MRO initialization", COLOR_MUTED),
        ("        super().__init__(model_id=model)", COLOR_GREEN),
        ("        self.adapter = adapter  # LoRA layer", COLOR_WHITE),
        ("", COLOR_WHITE),
        ("    def generate(self, prompt: str):", COLOR_GOLD),
        ("        # 2. Dynamic method extension", COLOR_MUTED),
        ("        raw = super().generate(prompt)", COLOR_CYAN),
        ("        return self.adapter.apply(raw)", COLOR_ORANGE),
        ("", COLOR_WHITE),
        ("# Client resolves next MRO class at runtime!", COLOR_MUTED),
        ("print(FineTunedClient.mro())", COLOR_GOLD)
    ]

    # Typewriter progression (starts at 0.5s, finishes at 6.0s)
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
        # Gutter line number
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
# SCENE 3 (16 to 24s): MODULE 02 - THE DIAMOND PROBLEM & C3 LINEARIZATION
# =========================================================================
def make_frame_scene_3(t):
    global_prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "The Diamond Problem Solved", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "How Python Uses C3 Linearization to Prevent Duplicate Calls", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Center Flowchart: Dynamic Interactive Diamond Graph (Y: 340 to 800)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 460], fill=COLOR_CARD_BG, outline=COLOR_ORANGE, glow_color=COLOR_ORANGE, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE DIAMOND INHERITANCE GRAPH", font=FONT_HEADING, fill=COLOR_ORANGE, anchor="mm")

    # MRO resolution timeline:
    # 0.0s to 1.5s: All nodes normal
    # 1.5s to 3.0s: Step 1 -> Node D active
    # 3.0s to 4.5s: Step 2 -> Node B active
    # 4.5s to 6.0s: Step 3 -> Node C active
    # 6.0s to 7.8s: Step 4 -> Node A active
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
    # Node Coordinates
    # Node A (Root Top)
    ax0 = WIDTH // 2 - nw // 2
    ay0 = card_y0 + 64
    # Node B (Left)
    bx0 = 110
    by0 = card_y0 + 180
    # Node C (Right)
    cx0 = WIDTH - 110 - nw
    cy0 = card_y0 + 180
    # Node D (Child Bottom)
    dx0 = WIDTH // 2 - nw // 2
    dy0 = card_y0 + 295

    # Glowing Connecting Diamond Lines with Traveling Energy Packets
    # Lines: D -> B, D -> C, B -> A, C -> A
    pulse_t = (t * 3.0) % 1.0

    def draw_pulsing_line(p1, p2, col, is_firing):
        draw.line([p1[0], p1[1], p2[0], p2[1]], fill=(60, 45, 60), width=3)
        if is_firing:
            draw.line([p1[0], p1[1], p2[0], p2[1]], fill=col, width=3)
            # Traveling comet packet
            px = int(p1[0] + (p2[0] - p1[0]) * pulse_t)
            py = int(p1[1] + (p2[1] - p1[1]) * pulse_t)
            draw.ellipse([px - 6, py - 6, px + 6, py + 6], fill=COLOR_WHITE)

    draw_pulsing_line((dx0 + nw // 4, dy0), (bx0 + nw // 2, by0 + nh), COLOR_CYAN, step >= 2)
    draw_pulsing_line((dx0 + 3 * nw // 4, dy0), (cx0 + nw // 2, cy0 + nh), COLOR_PURPLE, step >= 3)
    draw_pulsing_line((bx0 + nw // 2, by0), (ax0 + nw // 4, ay0 + nh), COLOR_AMBER, step >= 4)
    draw_pulsing_line((cx0 + nw // 2, cy0), (ax0 + 3 * nw // 4, ay0 + nh), COLOR_AMBER, step >= 4)

    # Draw Nodes with Active Glow
    def draw_node(x0, y0, title, code, col, active, step_label=None):
        outline = col if active else (70, 50, 70)
        glow = col if active else None
        draw_glow_card(draw, [x0, y0, x0 + nw, y0 + nh], fill=COLOR_INNER_BG, outline=outline, glow_color=glow, radius=12, width=3 if active else 1)
        draw.text((x0 + nw // 2, y0 + 22), title, font=FONT_SUB, fill=col if active else COLOR_MUTED, anchor="mm")
        draw.text((x0 + nw // 2, y0 + 50), code, font=FONT_CODE_SM, fill=COLOR_WHITE if active else (130, 115, 125), anchor="mm")
        if step_label and active:
            # Floating Step Badge
            draw.rounded_rectangle([x0 + nw - 30, y0 - 14, x0 + nw + 30, y0 + 14], radius=14, fill=col)
            draw.text((x0 + nw, y0), step_label, font=FONT_CODE_SM, fill=(10, 8, 12), anchor="mm")

    draw_node(ax0, ay0, "Class A (Root)", "def ping(): 'Root'", COLOR_AMBER, step == 4, "4th")
    draw_node(bx0, by0, "Class B (Left)", "super().ping()", COLOR_CYAN, step == 2, "2nd")
    draw_node(cx0, cy0, "Class C (Right)", "super().ping()", COLOR_PURPLE, step == 3, "3rd")
    draw_node(dx0, dy0, "Class D(B, C)", "d = D(); d.ping()", COLOR_GREEN, step >= 1, "1st")

    # MRO Dynamic Resolution Ribbon (Lights up sequentially)
    ry0 = card_y0 + 390
    draw.rounded_rectangle([100, ry0, WIDTH - 100, ry0 + 54], radius=12, fill=(28, 18, 28), outline=COLOR_GOLD, width=1)
    
    # Render Step badges inside ribbon
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
# SCENE 4 (24 to 32s): MODULES 03 & 04 - DUCK TYPING & VECTOR DB ABCs
# =========================================================================
def make_frame_scene_4(t):
    global_prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "Duck Typing & Vector DB ABCs", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Structural Polymorphism vs Interface Enforcement with abc.ABC", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

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
    splitter_t = (t * 2.0) % 1.0
    split_y = c_y0 + 175 + int(splitter_t * 40)
    draw.line([WIDTH // 2, c_y0 + 175, WIDTH // 2, c_y0 + 215], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 30, c_y0 + 215, 3 * WIDTH // 4 - 30, c_y0 + 215], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 30, c_y0 + 215, WIDTH // 4 + 30, c_y0 + 240], fill=COLOR_CYAN, width=3)
    draw.line([3 * WIDTH // 4 - 30, c_y0 + 215, 3 * WIDTH // 4 - 30, c_y0 + 240], fill=COLOR_AMBER, width=3)

    # Dual Concrete Provider Boxes
    ad_w = (WIDTH - 220 - 24) // 2
    # Pinecone
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
# SCENE 5 (32 to 40s): ANIMATED MASTERY CHECKLIST & METRIC STATS
# =========================================================================
CHECKLIST = [
    ("Inheritance & super()", "Dynamic cooperative MRO proxy chaining without hardcoding", COLOR_GREEN),
    ("Diamond Problem & C3", "C3 Linearization guarantees monotonic execution order", COLOR_ORANGE),
    ("Mixin Architecture", "Composable orthogonal behaviors without hierarchy bloat", COLOR_CYAN),
    ("Duck Typing & Protocols", "Structural polymorphism with zero inheritance runtime cost", COLOR_CORAL),
    ("Abstract Base Classes", "Strict interface enforcement with abc.ABC & Vector DBs", COLOR_GOLD)
]

def make_frame_scene_5(t):
    global_prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.0)
    img, draw = render_dynamic_background(t, global_prog)

    draw.text((WIDTH // 2, 246), "Production OOP Mastery!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "You Now Build Enterprise AI & System Architectures in Python", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Big Checklist Container (Y: 340 to 930)
    card_y0 = 340
    draw_glow_card(draw, [80, card_y0, WIDTH - 80, card_y0 + 580], fill=COLOR_CARD_BG, outline=COLOR_GOLD, glow_color=COLOR_GOLD, radius=20, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "DAY 15 ADVANCED ARCHITECTURE CHECKLIST", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    p_y = card_y0 + 72
    for idx, (title, desc, col) in enumerate(CHECKLIST):
        reveal_time = idx * 1.1
        is_revealed = (t >= reveal_time)
        
        if is_revealed:
            # Pop-in spring effect
            box_prog = ease_out((t - reveal_time) / 0.5)
            draw.rounded_rectangle([105, p_y, WIDTH - 105, p_y + 90], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
            # Glowing Checkbox
            draw.rounded_rectangle([125, p_y + 16, 185, p_y + 74], radius=10, fill=(20, 40, 26), outline=col, width=2)
            draw.text((155, p_y + 45), "✓", font=FONT_HEADING, fill=col, anchor="mm")
            # Text
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

    # Dynamic counter calculation
    pct = int(min(100, (t / 5.5) * 100))
    stat_cards = [
        ("4", "MODULES", "Deep Dive OOP", COLOR_GREEN),
        ("6", "LAB TASKS", "In Workbook", COLOR_CYAN),
        (f"{pct}%", "MASTERY", "Enterprise Ready", COLOR_GOLD)
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
    print("🎬 Rendering Day 15 HyperFrames Kinetic Motion Reel (40.0s @ 24fps)...")
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
