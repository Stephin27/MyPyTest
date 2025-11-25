import pytest
import allure
from playwright.sync_api import Page
from agents.suggestion_agent import SuggestionAgent
from config import Config

@allure.feature("Playwright Agents")
@allure.story("Suggestion Agent Workflow")
def test_suggestion_agent_flow(page: Page):
    agent = SuggestionAgent(page)
    
    # Test with a specific country
    country = "United States (USA)"
    
    allure.dynamic.title(f"Verify Suggestion Agent for {country}")
    
    result = agent.select_country(country)
    
    assert result is True, f"Agent failed to select {country}"
