from playwright.sync_api import Page
from pages.practice_page import PracticePage
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SuggestionAgent:
    """
    Agent responsible for handling the Suggestion Class Example workflow.
    Encapsulates the logic for selecting a country from the suggestion dropdown.
    """

    def __init__(self, page: Page):
        self.page = page
        self.practice_page = PracticePage(page)

    def select_country(self, country_name: str) -> bool:
        """
        Executes the workflow to select a country.
        
        Args:
            country_name: The full name of the country to select.
            
        Returns:
            bool: True if the selection was successful and verified, False otherwise.
        """
        try:
            logger.info(f"Agent starting country selection for: {country_name}")
            
            # Ensure we are on the correct page
            if self.page.url != self.practice_page.url:
                self.practice_page.navigate()

            # Input partial text (first 3 chars)
            partial_text = country_name[:3]
            self.practice_page.enter_suggestion_text(partial_text)

            # Select the suggestion
            self.practice_page.select_suggestion(country_name)

            # Verify the selection
            actual_value = self.practice_page.get_suggestion_input_value()
            if actual_value == country_name:
                logger.info(f"Agent successfully selected and verified: {country_name}")
                return True
            else:
                logger.error(f"Agent verification failed. Expected: {country_name}, Got: {actual_value}")
                return False

        except Exception as e:
            logger.error(f"Agent failed to select country '{country_name}': {e}")
            raise
