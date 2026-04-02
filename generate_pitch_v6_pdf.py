"""
MOSAIC_PITCH_V6.html → PDF generator
Captures all 13 slides at 1920×1080 via Playwright, combines into PDF.

Run: python generate_pitch_v6_pdf.py
Output: MOSAIC_PITCH_V6.pdf
"""
import sys
import time
from pathlib import Path

BASE = Path(__file__).parent
HTML_FILE = BASE / "MOSAIC_PITCH_V6.html"
OUTPUT_PDF = BASE / "MOSAIC_PITCH_V6.pdf"
SLIDE_DIR = BASE / "_slide_captures_v6"
SLIDE_DIR.mkdir(exist_ok=True)
TOTAL_SLIDES = 13

def check_deps():
    missing = []
    try: from playwright.sync_api import sync_playwright
    except ImportError: missing.append("playwright")
    try: from reportlab.lib.pagesizes import landscape
    except ImportError: missing.append("reportlab")
    try: from PIL import Image
    except ImportError: missing.append("Pillow")
    if missing:
        print(f"Missing: {', '.join(missing)}")
        print(f"Run: pip install {' '.join(missing)}")
        sys.exit(1)

def capture_slides():
    from playwright.sync_api import sync_playwright
    url = HTML_FILE.as_uri()
    print(f"Opening: {url}")
    slides = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(url, wait_until="networkidle")
        time.sleep(3)  # wait for fonts + images
        # Hide nav dots and progress bar for cleaner PDF
        page.evaluate("""
          const dots = document.getElementById('dots');
          if (dots) dots.style.display = 'none';
          const prog = document.getElementById('progress');
          if (prog) prog.style.display = 'none';
          const counter = document.getElementById('counter');
          if (counter) counter.style.display = 'none';
        """)
        for i in range(TOTAL_SLIDES):
            page.evaluate(f"goTo({i})")
            time.sleep(0.6)
            out = SLIDE_DIR / f"slide_{i+1:02d}.png"
            page.screenshot(path=str(out), full_page=False)
            size_kb = out.stat().st_size // 1024
            print(f"  Slide {i+1:02d}/13  {out.name} ({size_kb}KB)")
            slides.append(out)
        browser.close()
    return slides

def build_pdf(slides):
    from reportlab.pdfgen import canvas as rl_canvas
    W, H = 1920, 1080
    PX_TO_PT = 72 / 96
    page_w = W * PX_TO_PT
    page_h = H * PX_TO_PT
    c = rl_canvas.Canvas(str(OUTPUT_PDF), pagesize=(page_w, page_h))
    for slide in slides:
        c.drawImage(str(slide), 0, 0, width=page_w, height=page_h)
        c.showPage()
    c.save()
    size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
    print(f"\nOK  PDF saved: {OUTPUT_PDF.name} ({size_mb:.1f}MB, {len(slides)} pages)")

if __name__ == "__main__":
    print("=== MOSAIC Pitch V6 — PDF Generator ===\n")
    check_deps()
    print("Step 1: Capturing slides with Playwright...")
    slides = capture_slides()
    print(f"\nStep 2: Building PDF from {len(slides)} slides...")
    build_pdf(slides)
    print(f"\nDone. Open: {OUTPUT_PDF}")
