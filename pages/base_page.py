
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Clase base con métodos comunes para todas las páginas."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, locator):
        """Espera hasta que un elemento sea visible."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        """Espera hasta que un elemento sea clickeable."""
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator):
        """Espera y hace clic en un elemento."""
        self.wait_for_clickable(locator).click()

    def type_text(self, locator, text):
        """Espera, limpia y completa un campo."""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto de un elemento."""
        return self.wait_for_element(locator).text
