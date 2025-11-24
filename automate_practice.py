from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to https://rahulshettyacademy.com/AutomationPractice/")
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        # 1. Radio Button Example
        print("Interacting with Radio Buttons...")
        # Select 'Radio2'
        page.locator("input[value='radio2']").click()
        print("Selected Radio2")
        
        # Verify it's checked
        is_checked = page.locator("input[value='radio2']").is_checked()
        print(f"Radio2 is checked: {is_checked}")

        # 2. Dropdown Example
        print("\nInteracting with Dropdown...")
        # Select 'Option2'
        page.locator("#dropdown-class-example").select_option("Option2")
        print("Selected Option2")

        # 3. Checkbox Example
        print("\nInteracting with Checkboxes...")
        # Check 'Option1' and 'Option3'
        page.locator("#checkBoxOption1").check()
        page.locator("#checkBoxOption3").check()
        print("Checked Option1 and Option3")
        
        # Verify Option1 is checked
        print(f"Option1 is checked: {page.locator('#checkBoxOption1').is_checked()}")

        # 4. Web Table Example
        print("\nInteracting with Web Table...")
        # Locate the table (assuming name='courses' based on analysis, or using the structure)
        # Using a more robust selector just in case
        table = page.locator("table[name='courses']")
        
        # Get all rows
        rows = table.locator("tr").all()
        print(f"Total rows found in table: {len(rows)}")
        
        # Print data from the first few rows (skipping header)
        for i, row in enumerate(rows[1:4], start=1):
            cols = row.locator("td").all()
            if cols:
                course_name = cols[1].inner_text()
                price = cols[2].inner_text()
                print(f"Row {i}: Course='{course_name}', Price='{price}'")

        # Optional: Screenshot
        page.screenshot(path="screenshot.png")
        print("\nScreenshot saved as screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
