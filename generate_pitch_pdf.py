"""
MOSAIC_PITCH_V4.html → PDF generator
Uses Playwright to capture each of the 13 slides at 1920×1080
then combines into a proper PDF using reportlab.

Run: python generate_pitch_pdf.py
Output: MOSAIC_PITCH_V4.pdf
"""
import os
import sys
import time
from pathlib import Path

BASE = Path(__file__).parent
HTML_FILE = BASE / "MOSAIC_PITCH_V4.html"
OUTPUT_PDF = BASE / "MOSAIC_PITCH_V4.pdf"
SLIDE_DIR = BASE / "_slide_captures"
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
        if 'playwright' not in missing:
            pass
        else:
            print("Then: python -m playwright install chromium")
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
        # Wait for fonts
        time.sleep(2)
        # Hide nav bar for clean captures
        page.evaluate("document.getElementById('nav').style.display='none'")
        for i in range(TOTAL_SLIDES):
            page.evaluate(f"goTo({i})")
            time.sleep(0.5)
            out = SLIDE_DIR / f"slide_{i+1:02d}.png"
            page.screenshot(path=str(out), full_page=False)
            size_kb = out.stat().st_size // 1024
            print(f"  Slide {i+1:02d}/13  {out.name} ({size_kb}KB)")
            slides.append(out)
        browser.close()
    return slides

def build_pdf(slides):
    from reportlab.lib.pagesizes import landscape
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    W, H = 1920, 1080  # px
    # Convert px to points at 96dpi
    PX_TO_PT = 72 / 96
    page_w = W * PX_TO_PT
    page_h = H * PX_TO_PT
    c = canvas.Canvas(str(OUTPUT_PDF), pagesize=(page_w, page_h))
    for i, slide in enumerate(slides):
        c.drawImage(str(slide), 0, 0, width=page_w, height=page_h)
        c.showPage()
    c.save()
    size_mb = OUTPUT_PDF.stat().st_size / (1024 * 1024)
    print(f"\nOK PDF saved: {OUTPUT_PDF.name} ({size_mb:.1f}MB, {len(slides)} pages)")

if __name__ == "__main__":
    print("=== MOSAIC Pitch V4 — PDF Generator ===\n")
    check_deps()
    print("Step 1: Capturing slides with Playwright...")
    slides = capture_slides()
    print(f"\nStep 2: Building PDF from {len(slides)} slides...")
    build_pdf(slides)
    print(f"\nDone. Open: {OUTPUT_PDF}")
