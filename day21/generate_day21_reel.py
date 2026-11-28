"""
Day 21: Personal Journey Daily Vlog Reel Generator (Phase 2 FastAPI Kickoff Edition)
====================================================================================
30-Day Full Stack Python + AI Engineering Challenge

Theme: "Day 21/30: Phase 2 Kickoff — FastAPI Architecture & Modern REST APIs!"
Milestone: Phase 2 Begins! 70% Challenge Completed (21/30 Days)!

Scene Flow:
  - Scene 1 (0-8s):   Hook: Phase 2 Official Kickoff — Modern Full Stack Web & FastAPI
  - Scene 2 (8-16s):  Core Tech: ASGI vs WSGI — 10,000+ Concurrent Requests on Uvicorn
  - Scene 3 (16-24s): Data Safety: Request-Response Lifecycle & Pydantic V2 Sanitization
  - Scene 4 (24-32s): Superpower: Dependency Injection (Depends) & Yield Lifecycle
  - Scene 5 (32-40s): Milestone: 70% Challenge Complete, GitHub Repo, Day 22 Teaser

Aesthetic:
  - 100% Minimalist Luxury Dark Mode (Apple / Linear / Vercel style)
  - Zero Neon Colors (Warm Champagne Gold, Platinum White, Slate Silver, Deep Matte Obsidian)
  - Clean Segoe UI Modern Screen Typography (Zero text overlap or container spill)
  - Pure Silent Video: audio=False (40.0s, 24 FPS)
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

# Clean Modern Sans-Serif Typography (Segoe UI for Screen Elegance & Consolas for Code)
FONT_HERO = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52)
FONT_CARD_TITLE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 34)
FONT_HEADING = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
FONT_BODY = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_DESC = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 21)
FONT_BADGE = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
FONT_CODE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 21)

# Refined Minimalist Palette (Zero Neon — Luxury Dark Mode)
COLOR_BG_DARK = np.array([10, 10, 14], dtype=np.float32)     # Deep Matte Obsidian
COLOR_CARD_BG = (20, 20, 28, 255)                            # Premium Frosted Glass Card
COLOR_INNER_BG = (14, 14, 20, 255)                           # Deep Pitch Box

COLOR_WHITE = (255, 255, 255)          # 100% Pure Crisp White
COLOR_LIGHT = (230, 235, 242)          # Platinum White
COLOR_SILVER = (160, 165, 180)         # Refined Slate Silver (#A0A5B4)
COLOR_GOLD = (245, 200, 66)            # Warm Champagne Gold / Amber (#F5C842)
COLOR_BORDER = (65, 60, 78)            # Crisp Subtle Matte Border
COLOR_RED_MUTED = (235, 105, 105)      # Muted Warning Red (for legacy bottlenecks)

# Standardized Global Geometry Constants
CARD_X0, CARD_X1 = 60, WIDTH - 60      # Left 60, Right 1020 (Width: 960px)
CARD_Y0, CARD_Y1 = 450, 1050           # Top 450, Bottom 1050 (Height: 600px)
INNER_X0, INNER_X1 = 100, WIDTH - 100  # Left 100, Right 980 (Width: 880px)


def ease_out_cubic(x: float) -> float:
    """Smooth deceleration curve (Apple / iOS style)."""
    x = max(0.0, min(1.0, x))
    return 1.0 - (1.0 - x) ** 3


def create_base_canvas():
    canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    canvas[:, :] = COLOR_BG_DARK
    return Image.fromarray(canvas)


def render_journey_canvas(t, scene_progress, step_badge="DAY 21 / 30  •  PHASE 2 FULL STACK WEB"):
    img = create_base_canvas()
    draw = ImageDraw.Draw(img, "RGBA")

    # 1. Top Eyebrow Badge (Y: 160 to 220)
    badge_w = 620
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
# SCENE 1 (0 to 8s): PHASE 2 KICKOFF HOOK — FASTAPI ARCHITECTURE
# =========================================================================
def make_frame_scene_1(t):
    prog = np.clip((t / 8.0) * 0.20, 0.0, 0.20)
    img, draw = render_journey_canvas(t, prog, "DAY 21 / 30  •  PHASE 2 FULL STACK WEB")

    # Header
    draw.text((WIDTH // 2, 265), "Day 21: FastAPI Kickoff!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Modern Asynchronous Web APIs", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Building High-Throughput REST Backends with ASGI & Pydantic V2", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Phase 2 Core Web Architecture", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    modules = [
        ("01", "ASGI vs WSGI Architecture", "Asynchronous event loops & Uvicorn server processing"),
        ("02", "Pydantic V2 Request & Response", "Strict schema validation & automatic data sanitization"),
        ("03", "Modular APIRouter Composition", "Enterprise microservices with /api/v1 namespaces"),
        ("04", "Dependency Injection Engine", "Inversion of control with Depends & yield lifecycle")
    ]

    base_py = 540
    for idx, (num, title, desc) in enumerate(modules):
        start_t = 0.2 + idx * 0.15
        progress = ease_out_cubic((t - start_t) / 0.4)
        y_offset = int(20 * (1.0 - progress))
        py = base_py + idx * 122 + y_offset

        if progress > 0.01:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 102], radius=14, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            # Gold Tag
            draw.rounded_rectangle([INNER_X0 + 16, py + 16, INNER_X0 + 76, py + 86], radius=10, fill=(40, 34, 22), outline=COLOR_GOLD, width=1)
            draw.text((INNER_X0 + 46, py + 51), num, font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")
            # Text
            draw.text((INNER_X0 + 98, py + 22), title, font=FONT_HEADING, fill=COLOR_WHITE)
            draw.text((INNER_X0 + 98, py + 58), desc, font=FONT_DESC, fill=COLOR_SILVER)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🚀 Kicking off Phase 2: Modern Full Stack Web Development!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 2 (8 to 16s): ASGI vs WSGI ARCHITECTURE BENCHMARK
# =========================================================================
def make_frame_scene_2(t):
    prog = np.clip(0.20 + (t / 8.0) * 0.20, 0.20, 0.40)
    img, draw = render_journey_canvas(t, prog, "STEP 01  •  ASGI vs WSGI ARCHITECTURE")

    draw.text((WIDTH // 2, 265), "ASGI vs Legacy WSGI", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "10,000+ Concurrent Requests", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Why asynchronous event loops outperform synchronous worker threads.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Web Server Throughput Benchmark", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    bench_prog = ease_out_cubic(t / 3.0)

    # Box 1: Legacy WSGI (Flask / Django)
    py1 = 540
    draw.rounded_rectangle([INNER_X0, py1, INNER_X1, py1 + 140], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 26, py1 + 20), "Legacy WSGI (Flask / Django REST)", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X1 - 26, py1 + 20), "Thread Exhaustion", font=FONT_BODY, fill=COLOR_RED_MUTED, anchor="ra")
    # Red Bar
    draw.rounded_rectangle([INNER_X0 + 26, py1 + 65, INNER_X1 - 26, py1 + 85], radius=6, fill=(36, 32, 40))
    bar1_w = int((INNER_X1 - INNER_X0 - 52) * 0.35 * bench_prog)
    draw.rounded_rectangle([INNER_X0 + 26, py1 + 65, INNER_X0 + 26 + bar1_w, py1 + 85], radius=6, fill=COLOR_RED_MUTED)
    draw.text((INNER_X0 + 26, py1 + 98), "1 thread per request. Blocking I/O stalls workers and wastes server memory.", font=FONT_DESC, fill=COLOR_SILVER)

    # Box 2: Modern ASGI (FastAPI + Uvicorn)
    py2 = 700
    draw.rounded_rectangle([INNER_X0, py2, INNER_X1, py2 + 140], radius=16, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((INNER_X0 + 26, py2 + 20), "Modern ASGI (FastAPI + Uvicorn)", font=FONT_HEADING, fill=COLOR_GOLD)
    draw.text((INNER_X1 - 26, py2 + 20), "10x Concurrency", font=FONT_BODY, fill=COLOR_GOLD, anchor="ra")
    # Gold Bar
    draw.rounded_rectangle([INNER_X0 + 26, py2 + 65, INNER_X1 - 26, py2 + 85], radius=6, fill=(36, 32, 40))
    bar2_w = int((INNER_X1 - INNER_X0 - 52) * 0.95 * bench_prog)
    draw.rounded_rectangle([INNER_X0 + 26, py2 + 65, INNER_X0 + 26 + bar2_w, py2 + 85], radius=6, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 26, py2 + 98), "Non-blocking event loop handles 10,000+ connections with low RAM footprint!", font=FONT_DESC, fill=COLOR_WHITE)

    # Box 3: Modern Lifespan
    py3 = 860
    draw.rounded_rectangle([INNER_X0, py3, INNER_X1, py3 + 140], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
    draw.text((INNER_X0 + 26, py3 + 20), "Modern Application Lifespan Protocol", font=FONT_HEADING, fill=COLOR_WHITE)
    draw.text((INNER_X0 + 26, py3 + 60), "@asynccontextmanager lifecycle initializes DB pools & AI models", font=FONT_CODE, fill=COLOR_GOLD)
    draw.text((INNER_X0 + 26, py3 + 98), "Guarantees zero database connection leaks and graceful server shutdowns.", font=FONT_DESC, fill=COLOR_SILVER)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⚡ ASGI handles massive concurrent web traffic effortlessly!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 3 (16 to 24s): REQUEST-RESPONSE LIFECYCLE & PYDANTIC V2
# =========================================================================
def make_frame_scene_3(t):
    prog = np.clip(0.40 + (t / 8.0) * 0.20, 0.40, 0.60)
    img, draw = render_journey_canvas(t, prog, "STEP 02  •  PYDANTIC V2 DATA SANITIZATION")

    draw.text((WIDTH // 2, 265), "Request-Response Lifecycle", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Automatic Type Safety & 422s", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "How Pydantic V2 validates inputs and response_model filters secrets.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Type Coercion & Schema Validation", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # Code Box: Y = 540 to 1020
    draw.rounded_rectangle([INNER_X0, 540, INNER_X1, 1020], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)

    code_lines = [
        ("@app.post('/api/v1/tracks', response_model=TrackOut)", COLOR_GOLD),
        ("async def create_track(payload: TrackCreate):", COLOR_WHITE),
        ("    # Automatic Pydantic V2 validation & parsing", COLOR_SILVER),
        ("    return await db.save(payload)", COLOR_LIGHT),
        ("class TrackCreate(BaseModel):", COLOR_WHITE),
        ("    title: str = Field(..., min_length=3)", COLOR_LIGHT),
        ("    category: str = Field(pattern=r'^(sleep|focus)$')", COLOR_GOLD),
        ("    duration_seconds: int = Field(gt=0, le=7200)", COLOR_LIGHT),
        ("class TrackOut(BaseModel):", COLOR_WHITE),
        ("    id: int; title: str; stream_url: str", COLOR_LIGHT),
        ("    # Sensitive passwords & notes automatically filtered!", COLOR_SILVER)
    ]

    total_chars = sum(len(line) for line, _ in code_lines)
    if t < 0.5:
        shown_chars = 0
    elif t >= 6.0:
        shown_chars = total_chars
    else:
        shown_chars = int(((t - 0.5) / 5.5) * total_chars)

    cursor_visible = (int(t * 4) % 2 == 0)
    cur_y = 556
    acc = 0
    cursor_drawn = False

    for idx, (text, col) in enumerate(code_lines, start=1):
        line_len = len(text)
        draw.text((INNER_X0 + 20, cur_y), f"{idx:2d}", font=FONT_BODY, fill=COLOR_SILVER)
        draw.line([INNER_X0 + 55, cur_y - 2, INNER_X0 + 55, cur_y + 26], fill=COLOR_BORDER, width=2)

        if acc + line_len <= shown_chars:
            draw.text((INNER_X0 + 75, cur_y), text, font=FONT_CODE, fill=col)
            if acc + line_len == shown_chars and cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 75, cur_y), text, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        elif acc < shown_chars:
            part = text[:shown_chars - acc]
            draw.text((INNER_X0 + 75, cur_y), part, font=FONT_CODE, fill=col)
            if cursor_visible and not cursor_drawn:
                bb = draw.textbbox((INNER_X0 + 75, cur_y), part, font=FONT_CODE)
                draw.text((bb[2] + 4, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True
        else:
            if cursor_visible and not cursor_drawn:
                draw.text((INNER_X0 + 75, cur_y), "▌", font=FONT_CODE, fill=COLOR_GOLD)
                cursor_drawn = True

        acc += line_len
        cur_y += 42

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "🔒 response_model guarantees sensitive data never leaks!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 4 (24 to 32s): DEPENDENCY INJECTION ENGINE (DEPENDS & YIELD)
# =========================================================================
def make_frame_scene_4(t):
    prog = np.clip(0.60 + (t / 8.0) * 0.20, 0.60, 0.80)
    img, draw = render_journey_canvas(t, prog, "STEP 03  •  FASTAPI'S SUPERPOWER: DEPENDS")

    draw.text((WIDTH // 2, 265), "Dependency Injection Engine", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "Inversion of Control & Depends", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Resource lifecycle management, auth chaining & zero connection leaks.", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Production Inversion of Control", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    cards = [
        ("Dependencies with yield", "Opens DB transaction before route -> auto-commits & closes in finally block", "Zero Connection Leaks • Safe Rollback"),
        ("Multi-Tier Security Chaining", "Header Token -> Verify JWT -> Fetch Member Record -> Check Admin Role", "Modular Guards • Single Source of Truth"),
        ("app.dependency_overrides", "Instantly swap production authentication & live databases in automated tests", "Lightning Fast CI/CD • 100% Mockable")
    ]

    base_py = 540
    for idx, (title, desc, metric) in enumerate(cards):
        start_t = 0.2 + idx * 0.18
        progress = ease_out_cubic((t - start_t) / 0.4)
        y_offset = int(20 * (1.0 - progress))
        py = base_py + idx * 155 + y_offset

        if progress > 0.01:
            draw.rounded_rectangle([INNER_X0, py, INNER_X1, py + 138], radius=16, fill=COLOR_INNER_BG, outline=COLOR_BORDER, width=2)
            # Title
            draw.text((INNER_X0 + 26, py + 20), title, font=FONT_HEADING, fill=COLOR_GOLD)
            # Description
            draw.text((INNER_X0 + 26, py + 60), desc, font=FONT_DESC, fill=COLOR_LIGHT)
            # Metric Tag
            draw.rounded_rectangle([INNER_X0 + 26, py + 94, INNER_X0 + 380, py + 124], radius=6, fill=(36, 32, 44))
            draw.text((INNER_X0 + 36, py + 98), metric, font=FONT_BODY, fill=COLOR_GOLD)

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "💉 Clean code, effortless testability & rock-solid architecture!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# SCENE 5 (32 to 40s): PHASE 2 KICKOFF & 70% MILESTONE
# =========================================================================
TASKS_DONE = [
    ("ASGI & Uvicorn Architecture Mastered", "Event-loop processing & modern lifespan context managers"),
    ("Request Validation & Data Sanitization", "Path/query bounds, Pydantic V2 & response_model filtering"),
    ("Modular APIRouter & Dependency Injection", "Enterprise namespaces, yield sessions & auth chaining")
]


def make_frame_scene_5(t):
    prog = np.clip(0.80 + (t / 8.0) * 0.20, 0.80, 1.00)
    img, draw = render_journey_canvas(t, prog, "DAY 21 COMPLETE  •  70% MILESTONE UNLOCKED")

    draw.text((WIDTH // 2, 265), "Day 21 of 30 Complete!", font=FONT_HERO, fill=COLOR_WHITE, anchor="mm")
    draw.text((WIDTH // 2, 330), "70% of the Challenge Done!", font=FONT_HERO, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 390), "Phase 2 officially underway. Full-stack Python engineering in full gear!", font=FONT_SUB, fill=COLOR_SILVER, anchor="mm")

    # Card Title
    draw.text((WIDTH // 2, 495), "Today's Verified Accomplishments", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")

    # 3 Spacious Boxes: Height 95px each, gap 18px
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
        py += 114

    # Milestone Box: Y = 890 to 1010 (Height: 120px)
    pct = int(min(70, 67 + (t / 5.5) * 3))
    draw.rounded_rectangle([INNER_X0, 890, INNER_X1, 1010], radius=18, fill=COLOR_INNER_BG, outline=COLOR_GOLD, width=2)
    draw.text((WIDTH // 2, 930), f"CHALLENGE PROGRESS: {pct}% / 100%", font=FONT_CARD_TITLE, fill=COLOR_GOLD, anchor="mm")
    draw.text((WIDTH // 2, 975), "21 Days Down • 9 Days to Go • Day 22 Tomorrow!", font=FONT_BODY, fill=COLOR_WHITE, anchor="mm")

    # Bottom Pill Text
    draw.text((WIDTH // 2, 1120), "⭐ Full code on my GitHub repository. Link in bio!", font=FONT_HEADING, fill=COLOR_GOLD, anchor="mm")

    return np.array(img)


# =========================================================================
# EXPORTER (PURE SILENT VIDEO — audio=False)
# =========================================================================
def main():
    out_dir = "D:/learn-python/day21"
    preview_dir = os.path.join(out_dir, "reel_preview_frames")
    os.makedirs(preview_dir, exist_ok=True)

    print("=" * 65)
    print("🎬 Rendering Sophisticated Motion Silent Day 21 Vlog Reel...")
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

    video_output_path = os.path.join(out_dir, "day21_reel_video.mp4")
    print(f"\n🎥 Encoding Pure Silent Video -> {video_output_path} (40.0s, 24fps)...")

    final_video.write_videofile(
        video_output_path,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast"
    )

    print("\n" + "=" * 65)
    print(f"🎉 Day 21 Video Rendered Successfully: {video_output_path}")
    print("=" * 65)


if __name__ == "__main__":
    main()
