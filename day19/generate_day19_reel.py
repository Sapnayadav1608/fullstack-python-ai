"""
Day 19: Personal Journey Daily Vlog Reel Generator (Client Project & Python Edition)
=====================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 19/30: Real Client Website Pitch (Mindifestation) + Python Architecture!"
       Balancing the 30-Day Python Journey with Real-World Freelance Engineering

Aesthetic:
  - 100% Minimalist Luxury Dark Mode (Apple / Linear / Vercel style)
  - Zero Neon Colors (Warm Champagne Gold, Platinum White, Slate Silver, Deep Matte Obsidian)
  - Smooth Kinetic Staggered Card Entrances (ease-out cubic cascade)
  - Live Animated Hosting Cost Benchmark in Scene 4
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
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 23)

# Refined Minimalist Palette (Zero Neon — Luxury Dark Mode)
COLOR_BG_DARK = np.array([10, 10, 14], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (20, 20, 28, 255)                            # Premium Frosted Glass Card
COLOR_INNER_BG = (14, 14, 20, 255)                           # Deep Pitch Box

COLOR_WHITE = (255, 255, 255)          # 100% Pure Crisp White
COLOR_LIGHT = (230, 235, 242)          # Platinum White
COLOR_SILVER = (160, 165, 180)         # Refined Slate Silver (#A0A5B4)
COLOR_GOLD = (245, 200, 66)            # Warm Champagne Gold / Amber (#F5C842)
COLOR_BORDER = (65, 60, 78)            # Crisp Subtle Matte Border
COLOR_RED_MUTED = (220, 95, 95)        # Muted Warning Red (for cost benchmark)

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


def render_journey_canvas(t, scene_progress, step_badge="DAY 19 / 30  •  MY PYTHON + AI JOURNEY"):
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
# SCENE 1 (0 to 8s): JOURNEY HOOK (CLIENT PITCH ANNOUNCEMENT)
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 19 / 30  •  MY PYTHON + AI JOURNEY")

    # Header
    draw.text((WIDTH // 2, 265), "Day 19: Real Client Pitch!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Meditation Web Platform", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Building Mindifestation with Next.js 16 & Python", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's 4 Core Breakthroughs", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "Mindifestation Client Scope", "Digital sanctuary for @manifestation_meditator"),
        ("02", "Next.js 16 & Direct UPI QR", "Zero-maintenance serverless stack with 0% fee"),
        ("03", "Python Protocols & Pydantic", "Structural streaming types & UTR validation"),
        ("04", "Clean Generic Repositories", "Decoupled domain architecture & zero-cost engine")
    ]

    base_py = 540
    for idx, (num, title, desc) in enumerate(modules):
        start_t = 0.2 + idx * 0.15
        progress = ease_out_cubic((t - start_t) / 0.4)
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
    draw.text((WIDTH // 2, 1120), "👉 Combining Day 19 with a real client platform!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): STEP 1 - Client Stack & Python Typed Contracts
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  REAL CLIENT ARCHITECTURE")

    draw.text((WIDTH // 2, 265), "Step 1: Next.js 16 + React 19", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Mindifestation Tech Stack", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Warm minimalist sanctuary for audio streaming & e-books.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "My Code: Audio Protocol & UTR Verification", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Code Inner Box: Y = 540 to 1020
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)

    code_lines = [
        ("@runtime_checkable", COLOR_GOLD),
        ("class IAudioStreamable(Protocol):", COLOR_WHITE),
        ("    title: str", COLOR_LIGHT),
        ("    duration_seconds: int", COLOR_LIGHT),
        ("    audio_url: str", COLOR_LIGHT),
        ("    def get_stream_manifest(self) -> dict: ...", COLOR_SILVER),
        ("# Pydantic V2 UTR Payment Verification:", COLOR_GOLD),
        ("class UTRPaymentSchema(BaseModel):", COLOR_WHITE),
        ("    utr_number: str = Field(pattern=r\"^[0-9]{12}$\")", COLOR_LIGHT),
        ("    amount_paid_inr: float = Field(gt=0.0)", COLOR_GOLD)
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
    draw.text((WIDTH // 2, 1120), "⚡ Next.js 16 frontend + Python typed contracts!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): STEP 2 - Direct Dynamic UPI QR Payment Engine
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  ZERO-FEE PAYMENT ENGINE")

    draw.text((WIDTH // 2, 265), "Step 2: Direct Dynamic UPI QR", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Zero Transaction Gateway Fees", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Instant GPay, PhonePe & Paytm with UTR verification.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Client Payment & Checkout Engine", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Base Header Box: Y = 540 to 630
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 630], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 570), "NPCI Dynamic UPI QR Protocol", font=FONT_CODE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 602), "Direct instant bank transfer without 2-3% gateway cuts!", font=FONT_DESC, fill=COLOR_SILVER, anchor="mm")

    cards = [
        ("Dynamic QR", "Auto-generates UPI QR with exact product amount"),
        ("Zero Gateway Fee", "Saves client thousands in monthly transaction cuts"),
        ("Instant Access", "Customer submits UTR to unlock library automatically")
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
    draw.text((WIDTH // 2, 1120), "🔒 Direct UPI QR scanner powers instant client checkouts!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): STEP 3 - Serverless JSON Hosting Benchmark
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  ZERO-COST SERVERLESS STACK")

    draw.text((WIDTH // 2, 265), "Step 3: Serverless JSON Engine", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Zero Monthly Hosting Costs", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Reactive database engine with instant cross-component updates.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Client Hosting Cost Benchmark", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    bench_prog = ease_out_cubic(t / 3.0)

    # Box 1: Traditional Cloud Database
    py1 = 545
    draw.rounded_rectangle([INNER_X0, py1, INNER_X1, py1 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 30, py1 + 22), "Traditional Cloud Database (Supabase Pro / RDS)", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X1 - 30, py1 + 22), "₹2,500+ / mo (Expensive)", font=FONT_BODY, fill=COLOR_RED_MUTED, anchor="ra")
    # Red Warning Bar
    draw.rounded_rectangle([INNER_X0 + 30, py1 + 65, INNER_X1 - 30, py1 + 85], radius=6, fill=(36, 32, 40))
    bar1_w = int((INNER_X1 - INNER_X0 - 60) * bench_prog)
    if bar1_w > 0:
        draw.rounded_rectangle([INNER_X0 + 30, py1 + 65, INNER_X0 + 30 + bar1_w, py1 + 85], radius=6, fill=COLOR_RED_MUTED)
    draw.text((INNER_X0 + 30, py1 + 102), "Recurring server fees eat into the creator's digital sales revenue!", font=FONT_DESC, fill=COLOR_SILVER)

    # Box 2: Our Serverless JSON Engine
    py2 = 700
    draw.rounded_rectangle([INNER_X0, py2, INNER_X1, py2 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((INNER_X0 + 30, py2 + 22), "Our Serverless JSON & LocalStorage Engine", font=FONT_HEADING, fill=COLOR_GOLD)
    draw.text((INNER_X1 - 30, py2 + 22), "₹0 / Month (100% Free!)", font=FONT_BODY, fill=COLOR_GOLD, anchor="ra")
    # Gold Bar
    draw.rounded_rectangle([INNER_X0 + 30, py2 + 65, INNER_X1 - 30, py2 + 85], radius=6, fill=(36, 32, 40))
    bar2_w = max(18, int((INNER_X1 - INNER_X0 - 60) * 0.02 * bench_prog))
    draw.rounded_rectangle([INNER_X0 + 30, py2 + 65, INNER_X0 + 30 + bar2_w, py2 + 85], radius=6, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 30, py2 + 102), "Zero server cost, instant static hydration & lifetime zero maintenance!", font=FONT_DESC, fill=COLOR_WHITE)

    # Box 3: Architecture Advantage
    py3 = 855
    draw.rounded_rectangle([INNER_X0, py3, INNER_X1, py3 + 135], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 30, py3 + 22), "Client Business Value", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X0 + 30, py3 + 62), "100% Creator Profit Retention", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 30, py3 + 100), "Client keeps 100% of revenue without subscription overheads.", font=FONT_DESC, fill=COLOR_SILVER)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🧠 Smart full-stack engineering saves real client money!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): DAY 19 COMPLETE & CTA (SPACIOUS & ELEGANT)
# =========================================================================
TASKS_DONE = [
    ("Client Platform Architecture Set", "Mindifestation sanctuary, Next.js & Direct UPI QR"),
    ("4 Deep Python Modules Mastered", "Protocols, slotted dataclasses, Pydantic & Repos"),
    ("63% Challenge Milestone Unlocked", "19 days down, 11 more exciting days to go!")
]


def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 19 COMPLETE  •  MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 265), "Day 19 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "63% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Here is everything I accomplished today:", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's Achievements & Progress", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # 3 Spacious Boxes: Height 95px each, gap 20px
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

    # Milestone Box: Y = 890 to 1010 (Height: 120px)
    pct = int(min(63, 60 + (t / 5.5) * 3))
    draw.rounded_rectangle([INNER_X0, 890, INNER_X1, 1010], radius=18, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 930), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 975), "Follow along my 30-Day Python + AI Journey! Day 20 tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER (PURE SILENT VIDEO — audio=False)
# =========================================================================
def main():
    out_dir = "D:/learn-python/day19"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Sophisticated Motion Silent Day 19 Vlog Reel...")
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

    video_output_path = os.path.join(out_dir, "day19_reel_video.mp4")
    print(f"\n🎥 Encoding Pure Silent Video -> {video_output_path} (40.0s, 24fps)...")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast"
    )

    print("\n" + "=" * 65)
    print(f"🎉 Day 19 Video Rendered Successfully: {video_output_path}")
    print("=" * 65)


if __name__ == "__main__":
    main()
