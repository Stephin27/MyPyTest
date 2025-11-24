import pytest
import openpyxl
from playwright.sync_api import Page
from pages.practice_page import PracticePage
import allure
from config import Config
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_country_data():
    try:
        file_path = Config.DATA_DIR / "countries.xlsx"
        logger.info(f"Loading country data from {file_path}")
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        countries = []
        # Skip header row
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0]:
                countries.append(row[0])
        logger.info(f"Loaded {len(countries)} countries")
        return countries
    except FileNotFoundError:
        logger.error(f"Data file not found at {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading country data: {e}")
        raise

@allure.feature("Suggestion Class Example")
@allure.story("Data Driven Testing for Country Suggestion")
@pytest.mark.parametrize("country_name", get_country_data())
def test_suggestion_class_example(page: Page, country_name: str):
    logger.info(f"Starting test for country: {country_name}")
    practice_page = PracticePage(page)
    practice_page.navigate()
    
    # Input first 3 characters
    partial_text = country_name[:3]
    practice_page.enter_suggestion_text(partial_text)
    
    # Select the full country name from suggestions
    practice_page.select_suggestion(country_name)
    
    # Verify the input value matches the country name
    assert practice_page.get_suggestion_input_value() == country_name
    logger.info(f"Test passed for country: {country_name}")
