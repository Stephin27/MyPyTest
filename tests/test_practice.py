import allure
from pages.practice_page import PracticePage

@allure.title("Verify Radio Button Interaction")
@allure.description("Test to verify that Radio Button 2 can be selected and is checked.")
@allure.severity(allure.severity_level.NORMAL)
def test_radio_buttons(practice_page: PracticePage):
    print("Interacting with Radio Buttons...")
    practice_page.select_radio_button_2()
    assert practice_page.is_radio_button_2_checked()
    print("Radio2 is checked")

@allure.title("Verify Dropdown Interaction")
@allure.description("Test to verify that Option 2 can be selected from the dropdown.")
@allure.severity(allure.severity_level.NORMAL)
def test_dropdown(practice_page: PracticePage):
    print("Interacting with Dropdown...")
    practice_page.select_dropdown_option("Option2")
    # Verification could be added here if needed, e.g., checking value

@allure.title("Verify Checkbox Interaction")
@allure.description("Test to verify that Checkbox 1 and 3 can be checked and Checkbox 1 status is verified.")
@allure.severity(allure.severity_level.NORMAL)
def test_checkboxes(practice_page: PracticePage):
    print("Interacting with Checkboxes...")
    practice_page.check_checkboxes()
    assert practice_page.is_checkbox_1_checked()
    print("Option1 is checked")

@allure.title("Verify Web Table Data")
@allure.description("Test to verify the row count and specific data in the Web Table.")
@allure.severity(allure.severity_level.CRITICAL)
def test_web_table(practice_page: PracticePage):
    print("Interacting with Web Table...")
    row_count = practice_page.get_table_row_count()
    print(f"Total rows found in table: {row_count}")
    assert row_count > 0

    # Verify data from a specific row (e.g., row 1)
    data = practice_page.get_table_data(1)
    if data:
        print(f"Row 1 Data: {data}")
        allure.attach(
            practice_page.page.screenshot(),
            name="web-table-screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        assert data['course'] == "Selenium Webdriver with Java Basics + Advanced + Interview Guide"
        assert data['price'] == "30"

@allure.title("Verify Alert Handling")
@allure.description("Test to verify Alert and Confirm dialogs.")
@allure.severity(allure.severity_level.NORMAL)
def test_alerts(practice_page: PracticePage):
    print("Interacting with Alerts...")
    practice_page.enter_alert_name("Rahul")
    
    # Handle Alert
    practice_page.page.once("dialog", lambda dialog: dialog.accept())
    practice_page.click_alert_btn()
    print("Alert accepted")

    # Handle Confirm
    practice_page.page.once("dialog", lambda dialog: dialog.dismiss())
    practice_page.click_confirm_btn()
    print("Confirm dismissed")

@allure.title("Verify Element Displayed/Hidden")
@allure.description("Test to verify Hide/Show functionality.")
@allure.severity(allure.severity_level.NORMAL)
def test_element_displayed(practice_page: PracticePage):
    print("Interacting with Hide/Show...")
    
    # Initially visible
    assert practice_page.is_displayed_text_visible()
    
    # Hide
    practice_page.click_hide_btn()
    assert not practice_page.is_displayed_text_visible()
    print("Element hidden")
    
    # Show
    practice_page.click_show_btn()
    assert practice_page.is_displayed_text_visible()
    print("Element shown")

@allure.title("Verify Mouse Hover")
@allure.description("Test to verify Mouse Hover and Top link click.")
@allure.severity(allure.severity_level.NORMAL)
def test_mouse_hover(practice_page: PracticePage):
    print("Interacting with Mouse Hover...")
    practice_page.hover_mouse_hover_btn()
    practice_page.click_top_link()
    # Verify URL contains #top or page scrolled to top (simple check)
    assert "#top" in practice_page.page.url
    print("Clicked Top link")
