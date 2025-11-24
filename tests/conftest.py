import pytest
import allure
from playwright.sync_api import Page
from pages.practice_page import PracticePage

@pytest.fixture(scope="function")
def practice_page(page: Page):
    practice_page = PracticePage(page)
    practice_page.navigate()
    return practice_page

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Page):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name=f"failure-screenshot-{request.node.name}",
            attachment_type=allure.attachment_type.PNG
        )
