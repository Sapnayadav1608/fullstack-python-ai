"""
Day 18: Personal Journey Daily Vlog Reel Generator (Sophisticated Motion Edition)
==================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 18/30: What I Learned & Built Today!" (Personal Learning Journey)
       File Systems, Serialization, JSONL & Streaming Large-Scale AI Datasets

Aesthetic:
  - 100% Minimalist, Premium Luxury Engineering (Apple / Linear / Vercel style)
  - Zero Neon Colors (Refined Champagne Gold, Platinum White, Slate Silver, Deep Matte Obsidian)
  - Smooth Kinetic Staggered Card Entrances (ease-out cubic cascade)
  - Live Animated Memory Efficiency Gauge in Scene 4
  - Pure Silent Video: audio=False

Unified Mathematical Grid Architecture:
  - Top Badge:           Y = 160 to 220 (Height: 60px, Radius: 18)
  - Hero Line 1:         Y = 265 (56px Bold White, anchor="mm")
  - Hero Line 2:         Y = 330 (56px Bold Gold, anchor="mm")
  - Subtitle:            Y = 390 (28px Italic Silver, anchor="mm")
  - Main Card:           Y = 450 to 1050 (Exact 600px Height, Left 60, Right 1020, Radius: 24)
  - Card Title:          Y = 495 (38px Bold Gold, anchor="mm")
  - Card Content:        Y = 540 to 1020 (Available 480px)
  - Bottom Callout Pill: Y = 1080 to 1160 (Exact 80px Height, Left 60, Right 1020, Radius: 22)
  - Animated Progress:   Y = 1200 to 1210 (Clean 10px Bar, Left 80, Right 1000)
  - Safe UI Zone:        Y = 1210 to 1920 (710px completely clear for Instagram/YouTube UI)
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

# Calibrated Unified Typography
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 56)
FONT_CARD_TITLE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 38)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 30)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/timesbi.ttf", 28)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 26)
FONT_DESC = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 23)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 24)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 25)
FONT_BIG_STAT = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 34)

# Refined Minimalist Palette (Zero Neon — Luxury Dark Mode)
COLOR_BG_DARK = np.array([10, 10, 14], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (20, 20, 28, 255)                            # Premium Frosted Glass Card
COLOR_INNER_BG = (14, 14, 20, 255)                           # Deep Pitch Box

COLOR_WHITE = (255, 255, 255)          # 100% Pure Crisp White
COLOR_LIGHT = (230, 235, 242)          # Platinum White
COLOR_SILVER = (160, 165, 180)         # Refined Slate Silver (#A0A5B4)
COLOR_GOLD = (245, 200, 66)            # Warm Champagne Gold / Amber (#F5C842)
COLOR_BORDER = (65, 60, 78)            # Crisp Subtle Matte Border
COLOR_RED_MUTED = (220, 95, 95)        # Muted Warning Red (for OOM benchmark)

# Standardized Global Geometry Constants
CARD_X0, CARD_X1 = 60, WIDTH - 60      # Left 60, Right 1020 (Width: 960px)
CARD_Y0, CARD_Y1 = 450, 1050           # Top 450, Bottom 1050 (Height: 600px)
INNER_X0, INNER_X1 = 90, WIDTH - 90    # Left 90, Right 990 (Width: 900px)


def ease_out_cubic(x: float) -> float:
    """Natural, smooth deceleration curve (Apple / iOS style)."""
    x = max(0.0, min(1.0, x))
    return 1.0 - (1.0 - x) ** 3


def create_base_canvas():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    canvas[:, :] = COLOR_BG_DARK
    return Image.fromarray(canvas)


def render_journey_canvas(t, scene_progress, step_badge="DAY 18 / 30  •  MY PYTHON + AI JOURNEY"):
    img = create_base_canvas()
    draw = ImageDraw.Draw(img, "RGBA")

    # 1. Top Eyebrow Badge (Y: 160 to 220)
    badge_w = 580
    bx0 = (WIDTH - badge_w) // 2
    draw.rounded_rectangle([bx0, 160, bx0 + badge_w, 220], radius=18, fill=(28, 26, 36), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 190), step_badge, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # 2. Main Card Shell (Y: 450 to 1050)
    draw.rounded_rectangle([CARD_X0, CARD_Y0, CARD_X1, CARD_Y1], radius=24, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)

    # 3. Bottom Callout Pill (Y: 1080 to 1160)
    draw.rounded_rectangle([CARD_X0, 1080, CARD_X1, 1160], radius=22, fill=(26, 24, 34), outline=COLOR_GOLD, width=2)

    # 4. Animated Progress Bar (Y: 1200 to 1210)
    draw.rounded_rectangle([80, 1200, WIDTH - 80, 1210], radius=5, fill=(36, 34, 46))
    fill_w = int((WIDTH - 160) * scene_progress)
    if fill_w > 0:
        draw.rounded_rectangle([80, 1200, 80 + fill_w, 1210], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK (STAGGERED SMOOTH CASCADE)
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 18 / 30  •  MY PYTHON + AI JOURNEY")

    # Header (Even vertical rhythm)
    draw.text((WIDTH // 2, 265), "Day 18 of 30 Days", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Python + AI Engineering!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "File Systems, JSONL & Large Dataset Streaming", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's 4 Core Breakthroughs", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "Modern Pathlib Architecture", "PEP 428 path algebra, / operator & recursive rglob"),
        ("02", "Encodings & Atomic Persistence", "UTF-8-SIG BOM trap, os.fsync() & crash-proof writes"),
        ("03", "JSONL & The Pickle RCE Exploit", "O(1) LLM fine-tuning data & why AI uses safetensors"),
        ("04", "Zero-Copy mmap & Token Streams", "Memory-mapped files & high-throughput batching")
    ]

    # Staggered Kinetic Slide-In (Cards smoothly settle into place)
    base_py = 540
    for idx, (num, title, desc) in enumerate(modules):
        # Stagger start by 0.12s per card over 0.35s duration
        start_t = 0.2 + idx * 0.15
        progress = ease_out_cubic((t - start_t) / 0.4)

        # Slide upward from +25px
        y_offset = int(25 * (1.0 - progress))
        py = base_py + idx * 124 + y_offset

        if progress > 0.01:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            # Gold Tag
            draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 85, py + 84], radius=10, fill=(40, 34, 22), outline=COLOR_GOLD, width=1)
            draw.text((INNER_X0 + 52, py + 50), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 115, py + 20), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((INNER_X0 + 115, py + 56), desc, font=FONT_DESC, fill=COLOR_SILVER)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "👉 Come along with me on Day 18!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - Crash-Proof Atomic Persistence
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  WHAT I MASTERED FIRST")

    draw.text((WIDTH // 2, 265), "Step 1: Crash-Proof Atomic", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Persistence & os.fsync()", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Preventing data corruption and partial writes during crashes.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "My Code: Atomic File Write Pattern", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Code Inner Box: Y = 540 to 1020 (Exact 480px Height, Left 90, Right 990)
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)

    code_lines = [
        ("def atomic_write(filepath, content):", COLOR_GOLD),
        ("    target = Path(filepath).resolve()", COLOR_WHITE),
        ("    temp = target.with_name(f\".{target.name}.tmp\")", COLOR_LIGHT),
        ("    # 1. Write and force flush to physical disk:", COLOR_SILVER),
        ("    with open(temp, \"w\", encoding=\"utf-8\") as f:", COLOR_WHITE),
        ("        f.write(content)", COLOR_GOLD),
        ("        f.flush()", COLOR_LIGHT),
        ("        os.fsync(f.fileno())  # Hardware sync!", COLOR_GOLD),
        ("    # 2. Atomic rename replaces old file safely:", COLOR_SILVER),
        ("    os.replace(temp, target)", COLOR_GOLD)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = 562
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((INNER_X0 + 25, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_SILVER)
        draw.line([INNER_X0 + 65, cur_y - 2, INNER_X0 + 65, cur_y + 28], fill=COLOR_BORDER, width=2)

        if acc + line_len <= shown_chars:
            draw.text((INNER_X0 + 85, cur_y), text, font=FONT_CODE, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 85, cur_y), text, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((INNER_X0 + 85, cur_y), part, font=FONT_CODE, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 85, cur_y), part, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((INNER_X0 + 85, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 44

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⚡ os.replace guarantees readers NEVER see half-written files!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - JSONL & The Pickle RCE Exploit
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I EXPLORED NEXT")

    draw.text((WIDTH // 2, 265), "Step 2: JSONL for LLMs & The", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Deadly Pickle RCE Exploit", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Why standard JSON fails at scale and why AI moved to safetensors.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Data Serialization Architecture", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Base Header Box: Y = 540 to 630 (Height: 90px)
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 630], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 570), "JSONL: 1 JSON Object Per Line", font=FONT_CODE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 602), "Streams 100GB fine-tuning datasets with O(1) constant RAM!", font=FONT_DESC, fill=COLOR_SILVER, anchor="mm")

    cards = [
        ("JSONL Dataset", "Enables streamable training pairs for Gemini & OpenAI"),
        ("Pickle Danger", "__reduce__ allows arbitrary Remote Code Execution (RCE)"),
        ("Safetensors", "Zero-copy, non-executable model weights standard")
    ]

    base_py = 660
    for idx, (tag, desc) in enumerate(cards):
        start_t = 0.2 + idx * 0.18
        progress = ease_out_cubic((t - start_t) / 0.4)
        y_offset = int(20 * (1.0 - progress))
        py = base_py + idx * 130 + y_offset

        if progress > 0.01:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            # Gold Tag
            draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 210, py + 84], radius=10, fill=(40, 34, 22), outline=COLOR_GOLD, width=1)
            draw.text((INNER_X0 + 115, py + 50), tag, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 230, py + 50), desc, font=FONT_DESC, fill=COLOR_WHITE, anchor="lm")

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🔒 NEVER use pickle.loads() on untrusted AI model files!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - LIVE ANIMATED MEMORY BENCHMARK (ZERO NEON)
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 265), "Step 3: Zero-Copy mmap &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "High-Throughput Token Streams", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Mapping disk pages directly into virtual memory address space.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "10 GB Dataset Memory Benchmark", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Smooth animation progress for the benchmark bars
    bench_prog = ease_out_cubic(t / 3.0)

    # Box 1: Standard f.read() (10,240 MB - RAM Crash)
    py1 = 545
    draw.rounded_rectangle([INNER_X0, py1, INNER_X1, py1 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 30, py1 + 22), "Standard f.read() / f.readlines()", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X1 - 30, py1 + 22), "10,240 MB (OOM Crash!)", font=FONT_BODY, fill=COLOR_RED_MUTED, anchor="ra")
    # Red Warning Bar
    draw.rounded_rectangle([INNER_X0 + 30, py1 + 65, INNER_X1 - 30, py1 + 85], radius=6, fill=(36, 32, 40))
    bar1_w = int((INNER_X1 - INNER_X0 - 60) * bench_prog)
    if bar1_w > 0:
        draw.rounded_rectangle([INNER_X0 + 30, py1 + 65, INNER_X0 + 30 + bar1_w, py1 + 85], radius=6, fill=COLOR_RED_MUTED)
    draw.text((INNER_X0 + 30, py1 + 102), "Allocates entire 10GB into Python heap -> Crashes container!", font=FONT_DESC, fill=COLOR_SILVER)

    # Box 2: Zero-Copy mmap / Chunked Streaming (15 MB Constant)
    py2 = 700
    draw.rounded_rectangle([INNER_X0, py2, INNER_X1, py2 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((INNER_X0 + 30, py2 + 22), "Zero-Copy mmap & Streaming", font=FONT_HEADING, fill=COLOR_GOLD)
    draw.text((INNER_X1 - 30, py2 + 22), "15 MB (99.8% Less RAM!)", font=FONT_BODY, fill=COLOR_GOLD, anchor="ra")
    # Gold Efficiency Bar (Only tiny fraction of width)
    draw.rounded_rectangle([INNER_X0 + 30, py2 + 65, INNER_X1 - 30, py2 + 85], radius=6, fill=(36, 32, 40))
    bar2_w = max(18, int((INNER_X1 - INNER_X0 - 60) * 0.02 * bench_prog))
    draw.rounded_rectangle([INNER_X0 + 30, py2 + 65, INNER_X0 + 30 + bar2_w, py2 + 85], radius=6, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 30, py2 + 102), "Maps disk pages to virtual memory -> Blazing fast O(1) RAM!", font=FONT_DESC, fill=COLOR_WHITE)

    # Box 3: Enterprise Takeaway
    py3 = 855
    draw.rounded_rectangle([INNER_X0, py3, INNER_X1, py3 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 30, py3 + 22), "Architecture Takeaway", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X0 + 30, py3 + 62), "StreamingTokenBatcher Protocol", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 30, py3 + 100), "Feeds continuous mini-batches to PyTorch without memory leaks.", font=FONT_DESC, fill=COLOR_SILVER)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🧠 Zero-copy mmap powers modern high-speed AI data loaders!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): DAY 18 COMPLETE & CTA (SPACIOUS & ELEGANT)
# =========================================================================
TASKS_DONE = [
    ("4 Deep Python Modules Mastered", "Pathlib, atomic I/O, JSONL, Pickle exploits & mmap"),
    ("6/6 Practice Tasks Solved", "All automated tests passed in my practice workbook"),
    ("60% Challenge Milestone Unlocked", "18 days down, 12 more exciting days to go!")
]


def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 18 COMPLETE  •  MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 265), "Day 18 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "60% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Here is everything I accomplished today:", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's Achievements & Progress", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # 3 Spacious Boxes: Height 95px each, gap 20px (540, 655, 770)
    py = 540
    for idx, (title, desc) in enumerate(TASKS_DONE):
        reveal_time = idx * 1.5
        is_revealed = (t >= reveal_time)

        if is_revealed:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 95], radius=14, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
            # Gold Checkmark Badge
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(40, 34, 22), outline=COLOR_GOLD, width=1)
            draw.text((INNER_X0 + 48, py + 48), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 95, py + 22), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((INNER_X0 + 95, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        else:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 95], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(26, 24, 32), outline=COLOR_BORDER, width=1)
            draw.text((INNER_X0 + 48, py + 48), "○", font=FONT_HEADING, fill=COLOR_SILVER, anchor="mm")
            draw.text((INNER_X0 + 95, py + 22), title, font=FONT_HEADING, fill=COLOR_SILVER)
            draw.text((INNER_X0 + 95, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 115

    # Milestone Box: Y = 890 to 1010 (Height: 120px, Symmetrical 40px gaps!)
    pct = int(min(60, 57 + (t / 5.5) * 3))
    draw.rounded_rectangle([INNER_X0, 890, INNER_X1, 1010], radius=18, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 930), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 975), "Follow along my 30-Day Python + AI Journey! Day 19 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER (PURE SILENT VIDEO — audio=False)
# =========================================================================
def main():
    out_dir = "D:/learn-python/day18"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Sophisticated Motion Silent Day 18 Vlog Reel...")
    print("=" * 65)

    print("📸 Exporting 5 High-Resolution Preview Frames...")
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

    clip1 = VideoClip(make_frame_scene_1, duration=SCENE_DURATION)
    clip2 = VideoClip(make_frame_scene_2, duration=SCENE_DURATION)
    clip3 = VideoClip(make_frame_scene_3, duration=SCENE_DURATION)
    clip4 = VideoClip(make_frame_scene_4, duration=SCENE_DURATION)
    clip5 = VideoClip(make_frame_scene_5, duration=SCENE_DURATION)

    final_video = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5])

    video_output_path = os.path.join(out_dir, "day18_reel_video.mp4")
    print(f"\n🎥 Encoding Pure Silent Video -> {video_output_path} (40.0s, 24fps)...")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast"
    )

    print("\n" + "=" * 65)
    print(f"🎉 Day 18 Video Rendered Successfully: {video_output_path}")
    print("=" * 65)


if __name__ == "__main__":
    main()
