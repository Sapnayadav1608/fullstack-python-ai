"""
Day 15: Ultra-Aesthetic Infographic & Architecture Motion Reel Generator
========================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: Advanced Object-Oriented Programming (OOP) Part 2
       Inheritance, Diamond Problem & C3 MRO, Mixins, Polymorphism & ABCs

Key Visual Features (Modern Creative AI Video Motion Graphics):
- High-Production Infographic Architecture: NOT just a raw code terminal!
- Rich Collage B-roll: Layered cards, architectural flowcharts, MRO resolution trees
- The Diamond Problem Flowchart with glowing node connections and step badges
- Enterprise Pluggable Vector DB Adapter Diagram
- Animated Progressive Checklist & Stat Metric Cards
- 1080x1920 Vertical Aspect Ratio (Instagram Reel / Shorts)
- Exact 40.0 Seconds Duration (5 Scenes x 8.0s @ 24fps)
- Deep Dark Obsidian Base (#0C090C) with Warm Amber/Gold/Emerald Accents
- Strict Safe Zone: Content ends above Y = 1330, Progress bar at Y = 1350-1360
- 560px bottom clear zone (Y: 1360 to 1920) for Instagram captions and UI!
- Zero Personal Name (Generic Track Branding)
- Audio: Pure clean video (no audio track) for real voiceover recording
- Output paths: D:/learn-python/day15/day15_reel_video.mp4
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
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 50)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 25)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 23)
FONT_STAT = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 40)
FONT_MINI = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)

# Deep Dark Base with Warm Shade Palette
COLOR_BG_DARK = np.array([12, 9, 12], dtype=np.float32)   # Deep Obsidian Dark
COLOR_CARD_BG = (18, 14, 18, 252)                         # Deep Dark Glass Card
COLOR_INNER_BG = (10, 7, 10, 255)                         # Pitch Black Inner Container

# Vibrant Warm Highlight Colors
COLOR_WHITE = (255, 253, 248)           # Crisp Warm White
COLOR_CREAM = (254, 243, 199)           # Warm Ivory
COLOR_MUTED = (165, 150, 160)           # Slate Grey
COLOR_AMBER = (245, 158, 11)            # Sunset Amber
COLOR_GOLD = (251, 191, 36)             # Radiant Gold
COLOR_ORANGE = (251, 146, 60)           # Tangerine / Warm Terracotta
COLOR_CORAL = (244, 63, 94)             # Warm Coral Sunset
COLOR_ROSE = (251, 113, 133)            # Soft Warm Rose
COLOR_GREEN = (52, 211, 153)            # Neon Emerald
COLOR_CYAN = (56, 189, 248)             # Neon Cyan / Sky
COLOR_PURPLE = (192, 132, 252)          # Neon Purple Accent


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


def draw_canvas(progress_ratio: float, badge_text: str = "DAY 15 / 30"):
    """Paints top header, track branding (NO PERSONAL NAME), and glowing progress bar."""
    img = CACHED_BG.copy()
    draw = ImageDraw.Draw(img, "RGBA")

    # Header Badge (Y: 125 to 181)
    badge_w, badge_h = 580, 56
    bx0 = (WIDTH - badge_w) // 2
    by0 = 125
    draw.rounded_rectangle([bx0, by0, bx0 + badge_w, by0 + badge_h], radius=28, fill=(24, 16, 22, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, by0 + badge_h // 2), f"✨ {badge_text}", font=FONT_BADGE, fill=COLOR_CREAM, anchor="mm")

    # Subtitle Branding (NO PERSONAL NAME)
    draw.text((WIDTH // 2, 202), "30 DAYS FULL STACK PYTHON + AI ENGINEERING", font=FONT_BADGE, fill=COLOR_MUTED, anchor="mm")

    # Glowing Progress Bar (Y: 1350 to 1360) - Strictly above caption zone!
    bar_y = 1350
    bar_w = WIDTH - 140
    draw.rounded_rectangle([70, bar_y, 70 + bar_w, bar_y + 10], radius=5, fill=(20, 14, 18, 240), outline=(55, 38, 48, 180))
    fill_len = int(bar_w * progress_ratio)
    if fill_len > 0:
        draw.rounded_rectangle([70, bar_y, 70 + fill_len, bar_y + 10], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): ROADMAP & ARCHITECTURAL ECOSYSTEM MAP
# =========================================================================
def build_base_scene_1():
    img, draw = draw_canvas(0.20, "DAY 15 / 30  •  ADVANCED OOP & ARCHITECTURE")
    draw.text((WIDTH // 2, 246), "Object-Oriented Python (Part 2)", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Inheritance • Diamond Problem • Mixins • Polymorphism • ABCs", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: The 4 Core Architectural Modules (Y: 330 to 670)
    card_y0, card_y1 = 330, 670
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DAY 15 ENTERPRISE OOP ROADMAP", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "INHERITANCE & super()", "Dynamic MRO proxy & parent state chaining", COLOR_GREEN),
        ("02", "THE DIAMOND PROBLEM", "C3 Linearization algorithm & Mixin composition", COLOR_ORANGE),
        ("03", "POLYMORPHISM & DUCKING", "Method overrides & structural typing (Protocol)", COLOR_CYAN),
        ("04", "ABSTRACT BASE CLASSES", "Interface contracts with abc.ABC & Vector DBs", COLOR_CORAL)
    ]

    p_y = card_y0 + 64
    for mod_num, mod_title, mod_desc, col in modules:
        draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 68], radius=12, fill=COLOR_INNER_BG, outline=col, width=2)
        # Left Badge
        draw.rounded_rectangle([112, p_y + 12, 175, p_y + 56], radius=8, fill=(28, 20, 26, 255), outline=col, width=1)
        draw.text((143, p_y + 34), mod_num, font=FONT_SUB, fill=col, anchor="mm")
        # Text
        draw.text((195, p_y + 18), mod_title, font=FONT_SUB, fill=COLOR_WHITE)
        draw.text((195, p_y + 42), mod_desc, font=FONT_BODY, fill=COLOR_MUTED)
        p_y += 76

    # Bottom Infographic Card: System Architecture Collage (Y: 690 to 1230)
    c_y0, c_y1 = 690, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "SYSTEM ARCHITECTURE & CLASS DESIGN", font=FONT_HEADING, fill=COLOR_AMBER, anchor="mm")

    # Visual Architecture Diagram (Boxes & Flow)
    # Box 1: Abstract Base Class
    draw.rounded_rectangle([110, c_y0 + 70, WIDTH - 110, c_y0 + 155], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CORAL, width=2)
    draw.rounded_rectangle([125, c_y0 + 85, 265, c_y0 + 120], radius=6, fill=(40, 15, 20), outline=COLOR_CORAL, width=1)
    draw.text((195, c_y0 + 102), "INTERFACE (ABC)", font=FONT_MINI, fill=COLOR_CORAL, anchor="mm")
    draw.text((285, c_y0 + 92), "BaseVectorDatabase (abc.ABC)", font=FONT_SUB, fill=COLOR_WHITE)
    draw.text((285, c_y0 + 124), "@abstractmethod def upsert(vectors) -> None", font=FONT_CODE, fill=COLOR_MUTED)

    # Downward Connection Line
    draw.line([WIDTH // 2, c_y0 + 155, WIDTH // 2, c_y0 + 195], fill=COLOR_GOLD, width=3)
    draw.polygon([(WIDTH // 2 - 8, c_y0 + 185), (WIDTH // 2 + 8, c_y0 + 185), (WIDTH // 2, c_y0 + 197)], fill=COLOR_GOLD)

    # Box 2: Concrete Adapters (Side-by-Side Dual Card)
    box_w = (WIDTH - 220 - 20) // 2
    # Pinecone Adapter Card
    draw.rounded_rectangle([110, c_y0 + 200, 110 + box_w, c_y0 + 315], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((110 + box_w // 2, c_y0 + 225), "PineconeAdapter", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text((110 + box_w // 2, c_y0 + 255), "Cloud Serverless Vector DB", font=FONT_MINI, fill=COLOR_CREAM, anchor="mm")
    draw.rounded_rectangle([130, c_y0 + 275, 110 + box_w - 20, c_y0 + 302], radius=6, fill=(15, 30, 20))
    draw.text((110 + box_w // 2, c_y0 + 288), "✓ Implements Contract", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")

    # ChromaDB Adapter Card
    cx2 = 110 + box_w + 20
    draw.rounded_rectangle([cx2, c_y0 + 200, cx2 + box_w, c_y0 + 315], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
    draw.text((cx2 + box_w // 2, c_y0 + 225), "ChromaDBAdapter", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")
    draw.text((cx2 + box_w // 2, c_y0 + 255), "Local Embedded Vector DB", font=FONT_MINI, fill=COLOR_CREAM, anchor="mm")
    draw.rounded_rectangle([cx2 + 20, c_y0 + 275, cx2 + box_w - 20, c_y0 + 302], radius=6, fill=(15, 25, 35))
    draw.text((cx2 + box_w // 2, c_y0 + 288), "✓ Zero Vendor Lock-in", font=FONT_MINI, fill=COLOR_CYAN, anchor="mm")

    # Box 3: Mixin Composition Ribbon
    draw.rounded_rectangle([110, c_y0 + 335, WIDTH - 110, c_y0 + 440], radius=14, fill=COLOR_INNER_BG, outline=COLOR_PURPLE, width=2)
    draw.text((130, c_y0 + 355), "🧩 Mixin Multiple Inheritance Pattern:", font=FONT_SUB, fill=COLOR_PURPLE)
    draw.text((130, c_y0 + 388), "class AIAgent(AuditLoggerMixin, RateLimiterMixin, JSONMixin):", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((130, c_y0 + 416), "→ Decoupled, orthogonal behaviors without deep inheritance!", font=FONT_BODY, fill=COLOR_CREAM)

    # Feature Pill Badges at bottom
    badges = [("⚡ MRO Chaining", COLOR_GREEN), ("🧩 Mixin Ready", COLOR_PURPLE), ("🛡️ Interface Safety", COLOR_CORAL)]
    bx = 110
    bw = (WIDTH - 220 - 40) // 3
    for b_title, b_col in badges:
        draw.rounded_rectangle([bx, c_y0 + 460, bx + bw, c_y0 + 510], radius=10, fill=(25, 18, 24), outline=b_col, width=1)
        draw.text((bx + bw // 2, c_y0 + 485), b_title, font=FONT_MINI, fill=b_col, anchor="mm")
        bx += bw + 20

    # Bottom Callout Pill (Y: 1250 to 1330)
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔥 Day 15 is live! Master Production OOP Architecture! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_1 = build_base_scene_1()

def make_frame_scene_1(t):
    img = BASE_SCENE_1.copy()
    draw = ImageDraw.Draw(img)
    # Subtle kinetic glowing pulse on the bottom pill border
    pulse = (np.sin(t * np.pi) + 1.0) / 2.0
    gold_val = int(180 + 75 * pulse)
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, outline=(gold_val, int(gold_val * 0.75), 36), width=2)
    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): MODULE 01 - INHERITANCE & super() DYNAMIC PROXY
# =========================================================================
def build_base_scene_2():
    img, draw = draw_canvas(0.40, "DAY 15 / 30  •  MODULE 01: INHERITANCE")
    draw.text((WIDTH // 2, 246), "Inheritance & super()", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Why super() is a Dynamic Proxy, Not a Hardcoded Parent Reference", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: The Parent -> Child Architecture Diagram (Y: 330 to 670)
    card_y0, card_y1 = 330, 670
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "PARENT TO CHILD STATE & METHOD DELEGATION", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Parent Class Box
    draw.rounded_rectangle([100, card_y0 + 64, WIDTH - 100, card_y0 + 175], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.rounded_rectangle([115, card_y0 + 76, 255, card_y0 + 108], radius=6, fill=(35, 20, 10), outline=COLOR_AMBER, width=1)
    draw.text((185, card_y0 + 92), "BASE CLASS", font=FONT_MINI, fill=COLOR_AMBER, anchor="mm")
    draw.text((275, card_y0 + 82), "class AIModelClient:", font=FONT_SUB, fill=COLOR_WHITE)
    draw.text((120, card_y0 + 120), "  def __init__(self, model_id, api_key):", font=FONT_CODE, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 146), "      self.model_id = model_id; self.api_key = api_key", font=FONT_CODE, fill=COLOR_MUTED)

    # Downward Dynamic Arrow
    draw.line([WIDTH // 2, card_y0 + 175, WIDTH // 2, card_y0 + 215], fill=COLOR_GREEN, width=4)
    draw.polygon([(WIDTH // 2 - 10, card_y0 + 203), (WIDTH // 2 + 10, card_y0 + 203), (WIDTH // 2, card_y0 + 218)], fill=COLOR_GREEN)
    draw.text((WIDTH // 2 + 30, card_y0 + 195), "super().__init__() MRO delegation", font=FONT_MINI, fill=COLOR_GREEN, anchor="lm")

    # Child Class Box
    draw.rounded_rectangle([100, card_y0 + 220, WIDTH - 100, card_y0 + 330], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.rounded_rectangle([115, card_y0 + 232, 255, card_y0 + 264], radius=6, fill=(15, 35, 20), outline=COLOR_GREEN, width=1)
    draw.text((185, card_y0 + 248), "SUBCLASS", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")
    draw.text((275, card_y0 + 238), "class FineTunedGeminiClient(AIModelClient):", font=FONT_SUB, fill=COLOR_WHITE)
    draw.text((120, card_y0 + 276), "  def __init__(self, model_id, api_key, lora_adapter):", font=FONT_CODE, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 302), "      super().__init__(model_id, api_key)  # State Chained!", font=FONT_CODE, fill=COLOR_GREEN)

    # Bottom Infographic Card: Comparison Matrix (Y: 690 to 1230)
    c_y0, c_y1 = 690, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CYAN, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "THE DANGER OF HARDCODED PARENT CALLS", font=FONT_HEADING, fill=COLOR_CYAN, anchor="mm")

    # Bad Practice Box
    draw.rounded_rectangle([100, c_y0 + 70, WIDTH - 100, c_y0 + 220], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CORAL, width=2)
    draw.text((125, c_y0 + 90), "❌ ROOKIE MISTAKE: Explicit Class Name Calling", font=FONT_SUB, fill=COLOR_CORAL)
    draw.text((125, c_y0 + 125), "AIModelClient.__init__(self, model_id, api_key)", font=FONT_CODE, fill=(248, 140, 140))
    draw.text((125, c_y0 + 160), "• Tightly couples subclass to exact parent name", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((125, c_y0 + 188), "• Completely BREAKS multiple inheritance & cooperative MRO!", font=FONT_BODY, fill=COLOR_CORAL)

    # Best Practice Box
    draw.rounded_rectangle([100, c_y0 + 240, WIDTH - 100, c_y0 + 390], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((125, c_y0 + 260), "✅ PRODUCTION PATTERN: Dynamic super() Proxy", font=FONT_SUB, fill=COLOR_GREEN)
    draw.text((125, c_y0 + 295), "super().__init__(model_id, api_key)", font=FONT_CODE, fill=COLOR_GREEN)
    draw.text((125, c_y0 + 330), "• Dynamically queries C3 Linearization order at runtime", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((125, c_y0 + 358), "• Effortlessly supports diamond inheritance & mixins", font=FONT_BODY, fill=COLOR_CREAM)

    # Key Architecture Takeaway Box
    draw.rounded_rectangle([100, c_y0 + 410, WIDTH - 100, c_y0 + 510], radius=14, fill=(25, 20, 15), outline=COLOR_GOLD, width=1)
    draw.text((125, c_y0 + 432), "💡 CPython Architecture Secret:", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((125, c_y0 + 465), "super() does NOT return the parent! It returns a proxy object", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((125, c_y0 + 488), "that searches the NEXT class in the instance's MRO chain!", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Pill
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "⚡ super() resolves the next MRO class at runtime, not compile-time!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_2 = build_base_scene_2()

def make_frame_scene_2(t):
    img = BASE_SCENE_2.copy()
    draw = ImageDraw.Draw(img)
    # Subtle kinetic indicator
    pulse = int(200 + 55 * np.sin(t * 3.0))
    draw.rounded_rectangle([WIDTH // 2 - 180, 1250, WIDTH // 2 + 180, 1330], radius=22, outline=(pulse, pulse, 50), width=1)
    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): MODULE 02 - THE DIAMOND PROBLEM & C3 MRO FLOWCHART
# =========================================================================
def build_base_scene_3():
    img, draw = draw_canvas(0.60, "DAY 15 / 30  •  MODULE 02: DIAMOND PROBLEM & MRO")
    draw.text((WIDTH // 2, 246), "The Diamond Problem & MRO", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "How Python Solves Multiple Inheritance with C3 Linearization", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Center Visual Flowchart Card: The Diamond Architecture Graph (Y: 330 to 760)
    card_y0, card_y1 = 330, 760
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_ORANGE, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "THE DIAMOND INHERITANCE GRAPH", font=FONT_HEADING, fill=COLOR_ORANGE, anchor="mm")

    # Node Dimensions & Coordinates
    nw, nh = 260, 68
    # Top Node A (Base)
    ax0 = WIDTH // 2 - nw // 2
    ay0 = card_y0 + 65
    draw.rounded_rectangle([ax0, ay0, ax0 + nw, ay0 + nh], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((WIDTH // 2, ay0 + 22), "Class A (Base Root)", font=FONT_SUB, fill=COLOR_AMBER, anchor="mm")
    draw.text((WIDTH // 2, ay0 + 46), "execute() -> 'Base Action'", font=FONT_MINI, fill=COLOR_MUTED, anchor="mm")

    # Left Node B (Child of A)
    bx0 = 120
    by0 = card_y0 + 175
    draw.rounded_rectangle([bx0, by0, bx0 + nw, by0 + nh], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
    draw.text((bx0 + nw // 2, by0 + 22), "Class B (Left)", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")
    draw.text((bx0 + nw // 2, by0 + 46), "Inherits A: super().execute()", font=FONT_MINI, fill=COLOR_MUTED, anchor="mm")

    # Right Node C (Child of A)
    cx0 = WIDTH - 120 - nw
    cy0 = card_y0 + 175
    draw.rounded_rectangle([cx0, cy0, cx0 + nw, cy0 + nh], radius=14, fill=COLOR_INNER_BG, outline=COLOR_PURPLE, width=2)
    draw.text((cx0 + nw // 2, cy0 + 22), "Class C (Right)", font=FONT_SUB, fill=COLOR_PURPLE, anchor="mm")
    draw.text((cx0 + nw // 2, cy0 + 46), "Inherits A: super().execute()", font=FONT_MINI, fill=COLOR_MUTED, anchor="mm")

    # Bottom Node D (Child of B and C)
    dx0 = WIDTH // 2 - nw // 2
    dy0 = card_y0 + 285
    draw.rounded_rectangle([dx0, dy0, dx0 + nw, dy0 + nh], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, dy0 + 22), "Class D(B, C)", font=FONT_SUB, fill=COLOR_GREEN, anchor="mm")
    draw.text((WIDTH // 2, dy0 + 46), "Multiple Inheritance Child", font=FONT_MINI, fill=COLOR_CREAM, anchor="mm")

    # Glowing Connecting Arrows for Diamond
    # D -> B and D -> C
    draw.line([dx0 + nw // 4, dy0, bx0 + nw // 2, by0 + nh], fill=COLOR_CYAN, width=3)
    draw.line([dx0 + 3 * nw // 4, dy0, cx0 + nw // 2, cy0 + nh], fill=COLOR_PURPLE, width=3)
    # B -> A and C -> A
    draw.line([bx0 + nw // 2, by0, ax0 + nw // 4, ay0 + nh], fill=COLOR_AMBER, width=3)
    draw.line([cx0 + nw // 2, cy0, ax0 + 3 * nw // 4, ay0 + nh], fill=COLOR_AMBER, width=3)

    # C3 Linearization Step-by-Step Resolution Ribbon (Inside Card)
    draw.rounded_rectangle([100, card_y0 + 368, WIDTH - 100, card_y0 + 418], radius=10, fill=(26, 18, 22), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, card_y0 + 393), "C3 MRO Resolution:  D  ➜  B  ➜  C  ➜  A  ➜  object", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Bottom Infographic Card: Mixin Composition Architecture (Y: 780 to 1230)
    c_y0, c_y1 = 780, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_PURPLE, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "THE MIXIN ARCHITECTURE PATTERN", font=FONT_HEADING, fill=COLOR_PURPLE, anchor="mm")

    mixins = [
        ("JSONSerializableMixin", "def to_json(self): return json.dumps(self.__dict__)", COLOR_CYAN),
        ("AuditLoggerMixin", "def log_action(self, action): audit_db.record(action)", COLOR_AMBER),
        ("RateLimiterMixin", "def check_rate_limit(self): enforce_token_bucket()", COLOR_GREEN)
    ]

    my = c_y0 + 64
    for m_name, m_code, m_col in mixins:
        draw.rounded_rectangle([100, my, WIDTH - 100, my + 64], radius=12, fill=COLOR_INNER_BG, outline=m_col, width=2)
        draw.text((120, my + 14), f"🧩 {m_name}", font=FONT_SUB, fill=m_col)
        draw.text((120, my + 38), m_code, font=FONT_CODE, fill=COLOR_MUTED)
        my += 74

    # Composed AIAgent Card
    draw.rounded_rectangle([100, my, WIDTH - 100, my + 115], radius=12, fill=(28, 16, 26), outline=COLOR_GOLD, width=2)
    draw.text((120, my + 18), "class AIAgent(JSONMixin, AuditLoggerMixin, RateLimiterMixin):", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((120, my + 52), "• Zero inheritance collisions! Behaviors stack seamlessly.", font=FONT_BODY, fill=COLOR_WHITE)
    draw.text((120, my + 80), "• Mixins NEVER call super().__init__() without explicit kwargs!", font=FONT_BODY, fill=COLOR_CREAM)

    # Bottom Pill
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "✨ Inspect any class resolution hierarchy with ClassName.mro()", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_3 = build_base_scene_3()

def make_frame_scene_3(t):
    img = BASE_SCENE_3.copy()
    draw = ImageDraw.Draw(img)
    # Highlight the MRO step ribbon dynamically
    step_pulse = int((t * 2) % 4)
    # Visual glow effect
    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): MODULES 03 & 04 - POLYMORPHISM, DUCK TYPING & ABCs
# =========================================================================
def build_base_scene_4():
    img, draw = draw_canvas(0.80, "DAY 15 / 30  •  MODULES 03 & 04: ABCs & DUCK TYPING")
    draw.text((WIDTH // 2, 246), "Polymorphism & Vector DB ABCs", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "Duck Typing vs Abstract Base Classes (abc.ABC) & Adapter Architecture", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Top Card: Duck Typing vs ABCs Visual Infographic (Y: 330 to 670)
    card_y0, card_y1 = 330, 670
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_CORAL, width=2)
    draw.text((WIDTH // 2, card_y0 + 32), "DUCK TYPING VS ABSTRACT BASE CLASSES", font=FONT_HEADING, fill=COLOR_CORAL, anchor="mm")

    half_w = (WIDTH - 200 - 20) // 2
    # Left Card: Duck Typing
    draw.rounded_rectangle([100, card_y0 + 64, 100 + half_w, card_y0 + 316], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((100 + half_w // 2, card_y0 + 90), "🦆 Python Duck Typing", font=FONT_SUB, fill=COLOR_AMBER, anchor="mm")
    draw.text((120, card_y0 + 120), "• 'If it walks like a duck and", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 148), "   quacks like a duck, it is one'", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((120, card_y0 + 185), "• Runtime behavior check", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((120, card_y0 + 215), "• Structural Subtyping via", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((120, card_y0 + 242), "   typing.Protocol", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((120, card_y0 + 278), "⚡ Zero inheritance bloat", font=FONT_MINI, fill=COLOR_GREEN)

    # Right Card: Abstract Base Classes
    rx = 100 + half_w + 20
    draw.rounded_rectangle([rx, card_y0 + 64, rx + half_w, card_y0 + 316], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CORAL, width=2)
    draw.text((rx + half_w // 2, card_y0 + 90), "🛡️ Abstract Base Classes", font=FONT_SUB, fill=COLOR_CORAL, anchor="mm")
    draw.text((rx + 20, card_y0 + 120), "• Enforced contracts via", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((rx + 20, card_y0 + 148), "   abc.ABC & @abstractmethod", font=FONT_CODE, fill=COLOR_CORAL)
    draw.text((rx + 20, card_y0 + 185), "• Cannot instantiate directly!", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((rx + 20, card_y0 + 215), "• Raises TypeError instantly", font=FONT_BODY, fill=COLOR_MUTED)
    draw.text((rx + 20, card_y0 + 242), "   if any method is missing", font=FONT_BODY, fill=COLOR_CREAM)
    draw.text((rx + 20, card_y0 + 278), "🔒 Compile-time safety", font=FONT_MINI, fill=COLOR_CYAN)

    # Bottom Infographic Card: Enterprise Vector DB Adapter System (Y: 690 to 1230)
    c_y0, c_y1 = 690, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GREEN, width=2)
    draw.text((WIDTH // 2, c_y0 + 32), "ENTERPRISE PLUGGABLE VECTOR DB ARCHITECTURE", font=FONT_HEADING, fill=COLOR_GREEN, anchor="mm")

    # Abstract Base Class Box
    draw.rounded_rectangle([100, c_y0 + 64, WIDTH - 100, c_y0 + 190], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.rounded_rectangle([115, c_y0 + 76, 255, c_y0 + 108], radius=6, fill=(35, 25, 10), outline=COLOR_GOLD, width=1)
    draw.text((185, c_y0 + 92), "ABSTRACT (ABC)", font=FONT_MINI, fill=COLOR_GOLD, anchor="mm")
    draw.text((275, c_y0 + 82), "class BaseVectorDatabase(abc.ABC):", font=FONT_SUB, fill=COLOR_WHITE)
    draw.text((120, c_y0 + 122), "  @abstractmethod def upsert(self, id: str, vector: list): ...", font=FONT_CODE, fill=COLOR_CREAM)
    draw.text((120, c_y0 + 152), "  @abstractmethod def query(self, vector: list, top_k: int): ...", font=FONT_CODE, fill=COLOR_MUTED)

    # Downward Connection Fork Line
    draw.line([WIDTH // 2, c_y0 + 190, WIDTH // 2, c_y0 + 225], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 40, c_y0 + 225, 3 * WIDTH // 4 - 40, c_y0 + 225], fill=COLOR_GREEN, width=3)
    draw.line([WIDTH // 4 + 40, c_y0 + 225, WIDTH // 4 + 40, c_y0 + 245], fill=COLOR_GREEN, width=3)
    draw.line([3 * WIDTH // 4 - 40, c_y0 + 225, 3 * WIDTH // 4 - 40, c_y0 + 245], fill=COLOR_GREEN, width=3)

    # Dual Concrete Provider Boxes
    ad_w = (WIDTH - 200 - 30) // 2
    # Pinecone
    draw.rounded_rectangle([100, c_y0 + 245, 100 + ad_w, c_y0 + 380], radius=14, fill=COLOR_INNER_BG, outline=COLOR_CYAN, width=2)
    draw.text((100 + ad_w // 2, c_y0 + 270), "PineconeAdapter", font=FONT_SUB, fill=COLOR_CYAN, anchor="mm")
    draw.text((100 + ad_w // 2, c_y0 + 300), "Serverless Cloud Vector DB", font=FONT_MINI, fill=COLOR_CREAM, anchor="mm")
    draw.text((100 + ad_w // 2, c_y0 + 335), "def upsert(...) -> REST API", font=FONT_CODE, fill=COLOR_MUTED, anchor="mm")
    draw.text((100 + ad_w // 2, c_y0 + 360), "✓ Full Contract Satisfied", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")

    # ChromaDB
    ch_x = 100 + ad_w + 30
    draw.rounded_rectangle([ch_x, c_y0 + 245, ch_x + ad_w, c_y0 + 380], radius=14, fill=COLOR_INNER_BG, outline=COLOR_AMBER, width=2)
    draw.text((ch_x + ad_w // 2, c_y0 + 270), "ChromaDBAdapter", font=FONT_SUB, fill=COLOR_AMBER, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 300), "Local In-Memory Vector DB", font=FONT_MINI, fill=COLOR_CREAM, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 335), "def upsert(...) -> SQLite/Parquet", font=FONT_CODE, fill=COLOR_MUTED, anchor="mm")
    draw.text((ch_x + ad_w // 2, c_y0 + 360), "✓ Full Contract Satisfied", font=FONT_MINI, fill=COLOR_GREEN, anchor="mm")

    # Clean Swappable Pipeline Callout
    draw.rounded_rectangle([100, c_y0 + 400, WIDTH - 100, c_y0 + 510], radius=14, fill=(25, 20, 15), outline=COLOR_GOLD, width=1)
    draw.text((125, c_y0 + 425), "💡 Zero Vendor Lock-in Architecture:", font=FONT_SUB, fill=COLOR_GOLD)
    draw.text((125, c_y0 + 458), "rag_pipeline = RAGSearchPipeline(db=PineconeAdapter())", font=FONT_CODE, fill=COLOR_WHITE)
    draw.text((125, c_y0 + 486), "rag_pipeline = RAGSearchPipeline(db=ChromaDBAdapter())  # 1-line swap!", font=FONT_CODE, fill=COLOR_GREEN)

    # Bottom Pill
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "🔒 Guaranteed API interfaces prevent runtime bugs before production!", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_4 = build_base_scene_4()

def make_frame_scene_4(t):
    img = BASE_SCENE_4.copy()
    draw = ImageDraw.Draw(img)
    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): RECAP, CHECKLIST & PRACTICE WORKBOOK
# =========================================================================
CHECKLIST_ITEMS = [
    ("Inheritance & super()", "Dynamic MRO proxy chaining without hardcoding parent names", COLOR_GREEN),
    ("The Diamond Problem & C3", "C3 Linearization guarantees monotonic class resolution order", COLOR_ORANGE),
    ("Mixin Composition Pattern", "Modular orthogonal plug-and-play behaviors without bloat", COLOR_CYAN),
    ("Duck Typing & Protocols", "Structural polymorphism with zero inheritance runtime cost", COLOR_CORAL),
    ("Abstract Base Classes (ABCs)", "Enforcing vector DB contracts with abc.ABC & @abstractmethod", COLOR_GOLD)
]

def build_base_scene_5():
    img, draw = draw_canvas(1.0, "DAY 15 / 30  •  PRODUCTION OOP CHECKLIST")
    draw.text((WIDTH // 2, 246), "Production OOP Mastery!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 292), "You Now Build Enterprise AI & System Architectures in Python", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    # Big Checklist Container (Y: 330 to 950)
    card_y0, card_y1 = 330, 950
    draw.rounded_rectangle([70, card_y0, WIDTH - 70, card_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, card_y0 + 34), "DAY 15 ADVANCED OOP ARCHITECTURE CHECKLIST", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    # Bottom Metric Stats Cards (Y: 970 to 1230)
    c_y0, c_y1 = 970, 1230
    draw.rounded_rectangle([70, c_y0, WIDTH - 70, c_y1], radius=22, fill=COLOR_CARD_BG, outline=COLOR_AMBER, width=2)

    stat_cards = [
        ("4", "MODULES", "Deep Dive OOP", COLOR_GREEN),
        ("6", "LAB TASKS", "In Workbook", COLOR_CYAN),
        ("100%", "ENTERPRISE", "Clean Code", COLOR_GOLD)
    ]
    sw = (WIDTH - 140 - 40) // 3
    sx = 90
    for s_num, s_label, s_sub, s_col in stat_cards:
        draw.rounded_rectangle([sx, c_y0 + 20, sx + sw, c_y1 - 20], radius=14, fill=COLOR_INNER_BG, outline=s_col, width=2)
        draw.text((sx + sw // 2, c_y0 + 65), s_num, font=FONT_STAT, fill=s_col, anchor="mm")
        draw.text((sx + sw // 2, c_y0 + 120), s_label, font=FONT_HEADING, fill=COLOR_WHITE, anchor="mm")
        draw.text((sx + sw // 2, c_y0 + 170), s_sub, font=FONT_BODY, fill=COLOR_MUTED, anchor="mm")
        sx += sw + 20

    # Bottom Pill
    draw.rounded_rectangle([70, 1250, WIDTH - 70, 1330], radius=22, fill=(22, 15, 20, 245), outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 1290), "⭐ Code & Practice Workbook on GitHub! Link in bio / comments! 👇", font=FONT_SUB, fill=COLOR_GOLD, anchor="mm")

    return img

BASE_SCENE_5 = build_base_scene_5()

def make_frame_scene_5(t):
    img = BASE_SCENE_5.copy()
    draw = ImageDraw.Draw(img)

    # Progressive Checklist Animation (0s to 6s reveals items 1 to 5)
    card_y0 = 330
    p_y = card_y0 + 70

    for idx, (title, desc, col) in enumerate(CHECKLIST_ITEMS):
        reveal_time = idx * 1.1
        if t >= reveal_time:
            # Active revealed item
            draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 95], radius=14, fill=COLOR_INNER_BG, outline=col, width=2)
            # Glowing Checkbox
            draw.rounded_rectangle([120, p_y + 18, 180, p_y + 78], radius=10, fill=(20, 35, 25), outline=col, width=2)
            draw.text((150, p_y + 48), "✓", font=FONT_HEADING, fill=col, anchor="mm")
            # Text
            draw.text((205, p_y + 24), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((205, p_y + 60), desc, font=FONT_BODY, fill=COLOR_MUTED)
        else:
            # Unrevealed pending item
            draw.rounded_rectangle([100, p_y, WIDTH - 100, p_y + 95], radius=14, fill=(14, 10, 14, 180), outline=(45, 30, 40), width=1)
            draw.rounded_rectangle([120, p_y + 18, 180, p_y + 78], radius=10, fill=(16, 12, 16), outline=(60, 45, 55), width=1)
            draw.text((150, p_y + 48), "○", font=FONT_HEADING, fill=COLOR_MUTED, anchor="mm")
            draw.text((205, p_y + 24), title, font=FONT_HEADING, fill=(120, 105, 115))
            draw.text((205, p_y + 60), desc, font=FONT_BODY, fill=(80, 68, 76))

        p_y += 105

    return np.array(img)


# =========================================================================
# VIDEO COMPOSITOR & EXPORTER
# =========================================================================
def main():
    out_dir = "D:/learn-python/day15"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Day 15 Motion Infographic Reel (40.0s @ 24fps)...")
    print("=" * 65)

    # 1. Export High-Resolution Preview Frames for Visual Inspection
    print("📸 Exporting 5 Preview Frames for Quality Verification...")
    previews = [
        ("scene_1.png", make_frame_scene_1(4.0)),
        ("scene_2.png", make_frame_scene_2(4.0)),
        ("scene_3.png", make_frame_scene_3(4.0)),
        ("scene_4.png", make_frame_scene_4(4.0)),
        ("scene_5.png", make_frame_scene_5(6.0)),
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
