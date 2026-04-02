from playwright.sync_api import sync_playwright
import os

HTML_PATH = "C:/Users/user/Projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_PITCH_V3.html"
PDF_PATH = "C:/Users/user/Projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_PITCH_V3.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(f"file:///{HTML_PATH}")
    page.wait_for_timeout(3000)

    # Find total number of slides
    total = page.evaluate("() => document.querySelectorAll('.slide, [class*=\"slide\"]').length || 12")
    print(f"Total slides detected: {total}")

    # Navigate to each slide and take a screenshot, combine into PDF
    import base64
    from reportlab.lib.pagesizes import landscape
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Image as RLImage
    from reportlab.lib.pagesizes import A4
    import io

    screenshots = []

    # Try clicking through slides
    for i in range(12):
        page.wait_for_timeout(500)
        screenshot = page.screenshot(type='png', full_page=False)
        screenshots.append(screenshot)
        print(f"Captured slide {i+1}")

        # Try pressing right arrow to advance
        page.keyboard.press('ArrowRight')
        page.wait_for_timeout(600)

    # Save as PDF using reportlab canvas (zero-margin, exact pixel fit)
    try:
        from reportlab.pdfgen import canvas as rl_canvas
        from reportlab.lib.utils import ImageReader

        W, H = 1920, 1080
        c = rl_canvas.Canvas(PDF_PATH, pagesize=(W, H))
        for i, ss in enumerate(screenshots):
            img_reader = ImageReader(io.BytesIO(ss))
            c.drawImage(img_reader, 0, 0, width=W, height=H)
            c.showPage()
        c.save()
        print(f"PDF with {len(screenshots)} slides saved to {PDF_PATH}")
    except ImportError:
        # Fallback: save individual screenshots and use Pillow to combine
        try:
            from PIL import Image as PILImage
            images = [PILImage.open(io.BytesIO(ss)).convert('RGB') for ss in screenshots]
            images[0].save(PDF_PATH, save_all=True, append_images=images[1:])
            print(f"PDF saved with {len(images)} slides using Pillow")
        except ImportError:
            # Just save the first screenshot as PDF via playwright
            page.goto(f"file:///{HTML_PATH}")
            page.wait_for_timeout(1000)
            page.pdf(path=PDF_PATH, width="1920px", height="1080px", print_background=True)
            print("Saved single-page PDF (install reportlab or Pillow for multi-slide)")

    browser.close()
