import re
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
import allure
from config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)

class PracticePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = Config.BASE_URL
        
        # Locators
        self.radio_button_2 = page.locator("input[value='radio2']")
        self.dropdown = page.locator("#dropdown-class-example")
        self.checkbox_1 = page.locator("#checkBoxOption1")
        self.checkbox_3 = page.locator("#checkBoxOption3")
        self.table = page.locator("table[name='courses']")
        self.table_rows = self.table.locator("tr")

    @allure.step("Navigate to Automation Practice page")
    def navigate(self):
        logger.info(f"Navigating to {self.url}")
        self.page.goto(self.url)

    @allure.step("Select Radio Button 2")
    def select_radio_button_2(self):
        logger.info("Selecting Radio Button 2")
        self.radio_button_2.click()

    @allure.step("Check if Radio Button 2 is selected")
    def is_radio_button_2_checked(self) -> bool:
        return self.radio_button_2.is_checked()

    @allure.step("Select option '{option_value}' from dropdown")
    def select_dropdown_option(self, option_value: str):
        logger.info(f"Selecting dropdown option: {option_value}")
        self.dropdown.select_option(option_value)

    @allure.step("Check Checkbox 1 and Checkbox 3")
    def check_checkboxes(self):
        logger.info("Checking Checkbox 1 and Checkbox 3")
        self.checkbox_1.check()
        self.checkbox_3.check()

    @allure.step("Check if Checkbox 1 is selected")
    def is_checkbox_1_checked(self) -> bool:
        return self.checkbox_1.is_checked()

    @allure.step("Get total row count from Web Table")
    def get_table_row_count(self) -> int:
        return self.table_rows.count()

    @allure.step("Get data from row {row_index}")
    def get_table_data(self, row_index: int):
        try:
            # row_index is 1-based for nth-child, but Playwright locator .nth() is 0-based.
            # However, we are getting a specific row locator.
            # Let's use the list of rows logic from the script for consistency.
            row = self.table_rows.nth(row_index) 
            cols = row.locator("td").all()
            if len(cols) >= 3:
                data = {
                    "course": cols[1].inner_text(),
                    "price": cols[2].inner_text()
                }
                logger.debug(f"Row {row_index} data: {data}")
                return data
            return None
        except Exception as e:
            logger.error(f"Error getting data from row {row_index}: {e}")
            return None

    # --- New Methods ---

    @allure.step("Enter name '{name}' in Alert Example")
    def enter_alert_name(self, name: str):
        self.page.locator("#name").fill(name)

    @allure.step("Click Alert Button")
    def click_alert_btn(self):
        self.page.locator("#alertbtn").click()

    @allure.step("Click Confirm Button")
    def click_confirm_btn(self):
        self.page.locator("#confirmbtn").click()

    @allure.step("Click Hide Button")
    def click_hide_btn(self):
        self.page.locator("#hide-textbox").click()

    @allure.step("Click Show Button")
    def click_show_btn(self):
        self.page.locator("#show-textbox").click()

    @allure.step("Check if Displayed Text is visible")
    def is_displayed_text_visible(self) -> bool:
        return self.page.locator("#displayed-text").is_visible()

    @allure.step("Hover over Mouse Hover button")
    def hover_mouse_hover_btn(self):
        self.page.locator("#mousehover").hover()

    @allure.step("Click Top link")
    def click_top_link(self):
        self.page.locator("a[href='#top']").click()

    @allure.step("Enter text '{text}' in Suggestion Input")
    def enter_suggestion_text(self, text: str):
        logger.info(f"Entering suggestion text: {text}")
        self.page.locator("input[id='autocomplete']").fill(text)

    @allure.step("Select suggestion '{text}'")
    def select_suggestion(self, text: str):
        try:
            logger.info(f"Selecting suggestion: {text}")
            # Wait for the suggestion list to appear
            self.page.locator("ul#ui-id-1").wait_for(state="visible", timeout=Config.TIMEOUT)
            # Locator for the specific item
            # Use re.escape to handle special characters like parentheses
            item = self.page.locator("li.ui-menu-item div").filter(has_text=re.compile(f"^\s*{re.escape(text)}\s*$", re.IGNORECASE)).first
            # Wait for the item to be visible
            item.wait_for(state="visible", timeout=Config.TIMEOUT)
            # Click the item
            item.click()
        except PlaywrightTimeoutError:
            logger.error(f"Timeout waiting for suggestion '{text}'")
            raise
        except Exception as e:
            logger.error(f"Error selecting suggestion '{text}': {e}")
            raise

    @allure.step("Get value from Suggestion Input")
    def get_suggestion_input_value(self) -> str:
        return self.page.locator("input[id='autocomplete']").input_value()
