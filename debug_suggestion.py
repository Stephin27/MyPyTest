from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")
        
        page.locator("input[id='autocomplete']").fill("Uni")
        page.locator("ul#ui-id-1").wait_for(state="visible")
        
        # Wait a bit for list to populate
        time.sleep(2)
        
        items = page.locator("li.ui-menu-item div").all_inner_texts()
        print("Suggestions for 'Uni':")
        for item in items:
            print(f"'{item}'")
            
        browser.close()

if __name__ == "__main__":
    run()
