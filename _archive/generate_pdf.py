from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})

    html_path = "C:/Users/user/Projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_PITCH_V3.html"
    page.goto(f"file:///{html_path}")
    page.wait_for_timeout(2000)

    # Navigate through all slides and print each
    page.pdf(
        path="C:/Users/user/Projects/PR-001_agentic-ventures/projects/pixie/MOSAIC_PITCH_V3.pdf",
        width="1920px",
        height="1080px",
        print_background=True
    )
    browser.close()
    print("PDF saved")
