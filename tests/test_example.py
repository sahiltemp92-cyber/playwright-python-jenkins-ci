import allure
from playwright.sync_api import Page
import pytest


@pytest.mark.regression
@allure.feature("Title verification")
@allure.story("Google home page")
def test_verify_google_title(page: Page):
    """
    Smoke Test:
    Validate title for Google page
    """
    page.goto("https://www.google.com")
    page.wait_for_load_state(state="domcontentloaded")
    assert "Google" in page.title()


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Title verification")
@allure.story("Selectors hub practice page")
def test_verify_selectors_hub_title(page):
    """
    Smoke Test:
    Validate title for selectorshub practice page
    """

    page.goto("https://selectorshub.com/xpath-practice-page/")
    assert "Xpath Practice Page" in page.title()


@pytest.mark.smoke
@allure.feature("Title verification")
@allure.story("Automation testing practice page")
def test_verify_automation_practice_title(page):
    """
    Smoke Test:
    Validate title for test automation practice page
    """

    page.goto("https://testautomationpractice.blogspot.com/")
    assert "Automation Testing Practice" in page.title()
