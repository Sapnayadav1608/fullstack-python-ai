"""
Day 18: Personal Journey Daily Vlog Reel Generator (Unified Mathematical Grid Edition)
======================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 18/30: What I Learned & Built Today!" (Personal Learning Journey)
       File Systems, Serialization, JSONL & Streaming Large-Scale AI Datasets

Unified Mathematical Grid Architecture (100% Symmetrical Spacing & Zero Overflow):
  - Top Badge:           Y = 160 to 220 (Height: 60px, Radius: 18)
  - Hero Line 1:         Y = 265 (56px Bold White, anchor="mm")
  - Hero Line 2:         Y = 330 (56px Bold Gold, anchor="mm")
  - Subtitle:            Y = 390 (28px Italic Silver, anchor="mm")
  - Main Card:           Y = 450 to 1050 (Exact 600px Height, Left 60, Right 1020, Radius: 24)
  - Card Title:          Y = 495 (38px Bold Gold, anchor="mm")
  - Card Content:        Y = 535 to 1020 (Available 485px, Symmetrical padding)
  - Bottom Callout Pill: Y = 1080 to 1160 (Exact 80px Height, Left 60, Right 1020, Radius: 22)
  - Animated Progress:   Y = 1200 to 1210 (Clean 10px Bar, Left 80, Right 1000)
  - Safe UI Zone:        Y = 1210 to 1920 (710px completely clear for Instagram/YouTube UI)
  - Pure Silent Video:   audio=False
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
FONT_BIG_MATH = ImageFont.truetype("C:/Windows/Fonts/timesbd.ttf", 40)

# High-Contrast Luxury Palette
COLOR_BG_DARK = np.array([8, 8, 12], dtype=np.float32)      # Deep Obsidian
COLOR_CARD_BG = (22, 20, 30, 255)                          # High Contrast Glass Card
COLOR_INNER_BG = (14, 12, 18, 255)                         # Deep Pitch Box

COLOR_WHITE = (255, 255, 255)          # 100% Pure White
COLOR_LIGHT = (226, 232, 240)          # Light Platinum
COLOR_SILVER = (203, 213, 225)         # Bright Silver (#CBD5E1)
COLOR_GOLD = (255, 215, 0)             # Radiant Vivid Gold
COLOR_GREEN = (52, 211, 153)           # Neon Emerald
COLOR_CYAN = (56, 189, 248)            # Vivid Electric Cyan
COLOR_BORDER = (80, 72, 100)           # High Visibility Crisp Border

# Standardized Global Geometry Constants
CARD_X0, CARD_X1 = 60, WIDTH - 60      # Left 60, Right 1020 (Width: 960px)
CARD_Y0, CARD_Y1 = 450, 1050           # Top 450, Bottom 1050 (Height: 600px)
INNER_X0, INNER_X1 = 90, WIDTH - 90    # Left 90, Right 990 (Width: 900px)


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
    draw.rounded_rectangle([bx0, 160, bx0 + badge_w, 220], radius=18, fill=(32, 28, 42), outline=COLOR_GOLD, width=1)
    draw.text((WIDTH // 2, 190), step_badge, font=FONT_BADGE, fill=COLOR_GOLD, anchor="mm")

    # 2. Main Card Shell (Y: 450 to 1050) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([CARD_X0, CARD_Y0, CARD_X1, CARD_Y1], radius=24, fill=COLOR_CARD_BG, outline=COLOR_GOLD, width=2)

    # 3. Bottom Callout Pill (Y: 1080 to 1160) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([CARD_X0, 1080, CARD_X1, 1160], radius=22, fill=(28, 24, 36), outline=COLOR_GOLD, width=2)

    # 4. Animated Progress Bar (Y: 1200 to 1210) — IDENTICAL ON ALL SCENES!
    draw.rounded_rectangle([80, 1200, WIDTH - 80, 1210], radius=5, fill=(40, 36, 52))
    fill_w = int((WIDTH - 160) * scene_progress)
    if fill_w > 0:
        draw.rounded_rectangle([80, 1200, 80 + fill_w, 1210], radius=5, fill=COLOR_GOLD)

    return img, draw


# =========================================================================
# SCENE 1 (0 to 8s): JOURNEY HOOK
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 18 / 30  •  MY PYTHON + AI JOURNEY")

    # Header (Even vertical spacing: 265, 330, 390)
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

    # 4 Boxes: Height 100px each, gap 24px (540, 664, 788, 912) -> ends at 1012 (38px bottom gap!)
    py = 540
    for num, title, desc in modules:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        # Gold Tag
        draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 85, py + 84], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((INNER_X0 + 52, py + 50), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((INNER_X0 + 115, py + 20), title, font=FONT_HEADING, fill=COLOR_WHITE)
        draw.text((INNER_X0 + 115, py + 56), desc, font=FONT_DESC, fill=COLOR_SILVER)
        py += 124

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
        ("    # 1. Write and force flush to physical disk:", COLOR_GREEN),
        ("    with open(temp, \"w\", encoding=\"utf-8\") as f:", COLOR_WHITE),
        ("        f.write(content)", COLOR_CYAN),
        ("        f.flush()", COLOR_GOLD),
        ("        os.fsync(f.fileno())  # Hardware sync!", COLOR_GREEN),
        ("    # 2. Atomic rename replaces old file safely:", COLOR_LIGHT),
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
# SCENE 3 (16 to 24s): STEP 2 - JSONL for LLMs & Pickle Vulnerabilities
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  WHAT I EXPLORED NEXT")

    draw.text((WIDTH // 2, 265), "Step 2: JSONL for LLMs & The", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Deadly Pickle RCE Exploit", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Why standard JSON fails at scale and why AI moved to safetensors.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Data Serialization Architecture", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Base Root Box: Y = 540 to 630 (Height: 90px)
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 630], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=3)
    draw.text((WIDTH // 2, 570), "JSONL: 1 JSON Object Per Line", font=FONT_CODE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 602), "Streams 100GB fine-tuning datasets with O(1) constant RAM!", font=FONT_DESC, fill=COLOR_SILVER, anchor="mm")

    cards = [
        ("JSONL Dataset", "Enables streamable training pairs for Gemini & OpenAI"),
        ("Pickle Danger", "__reduce__ allows arbitrary Remote Code Execution (RCE)"),
        ("Safetensors", "Zero-copy, non-executable model weights standard")
    ]

    # 3 Cards: Height 100px each, gap 30px (660, 790, 920) -> ends at 1020 (Exact 30px bottom gap!)
    py = 660
    for tag, desc in cards:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 100], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        # Tag
        draw.rounded_rectangle([INNER_X0 + 20, py + 16, INNER_X0 + 210, py + 84], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
        draw.text((INNER_X0 + 115, py + 50), tag, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
        # Text
        draw.text((INNER_X0 + 230, py + 50), desc, font=FONT_DESC, fill=COLOR_WHITE, anchor="lm")
        py += 130

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🔒 NEVER use pickle.loads() on untrusted AI model files!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - Zero-Copy mmap & Large-Scale Streaming
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  WHAT I BUILT TODAY")

    draw.text((WIDTH // 2, 265), "Step 3: Zero-Copy mmap &", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "High-Throughput Token Streams", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Mapping disk pages directly into virtual memory address space.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Large-Scale AI Data Pipeline", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    protocols = [
        (
            "1. Chunked Buffer Streamer",
            "stream_chunks(file, chunk_size=64KB)",
            "Processes files larger than physical RAM with O(1) memory!"
        ),
        (
            "2. Zero-Copy mmap Protocol",
            "mmap.mmap(fileno, length=0)",
            "Instant binary pattern search & slicing without copying to RAM!"
        ),
        (
            "3. StreamingTokenBatcher",
            "Continuous micro-batch generator",
            "Feeds millions of tokens to PyTorch models without OOM crashes!"
        )
    ]

    # 3 Cards: Height 135px each, gap 20px (545, 700, 855) -> ends at 990 (60px bottom gap!)
    py = 545
    for title, sig, desc in protocols:
        draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
        draw.text((INNER_X0 + 30, py + 22), title, font=FONT_HEADING, fill=COLOR_GOLD)
        draw.text((INNER_X0 + 30, py + 62), sig, font=FONT_CODE, fill=COLOR_CYAN)
        draw.text((INNER_X0 + 30, py + 100), desc, font=FONT_DESC, fill=COLOR_WHITE)
        py += 155

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
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(45, 36, 24), outline=COLOR_GOLD, width=2)
            draw.text((INNER_X0 + 48, py + 48), "✓", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 95, py + 22), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((INNER_X0 + 95, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)
        else:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 95], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            draw.rounded_rectangle([INNER_X0 + 18, py + 18, INNER_X0 + 78, py + 78], radius=10, fill=(28, 24, 36), outline=COLOR_BORDER, width=1)
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
    print("🎬 Rendering Unified Grid Silent Day 18 Vlog Reel...")
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
