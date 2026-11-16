
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Representa el proceso de checkout de SauceDemo."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def complete_customer_information(
        self, first_name, last_name, postal_code
    ):
        """Completa los datos del comprador y avanza."""

        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

        self.wait.until(
            EC.text_to_be_present_in_element(
                self.SUMMARY_TITLE,
                "Checkout: Overview"
            )
        )

    def finish_purchase(self):
        self.click(self.FINISH_BUTTON)

    def get_summary_title(self):
        return self.get_text(self.SUMMARY_TITLE)

    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
