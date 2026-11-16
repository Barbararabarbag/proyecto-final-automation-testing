
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Representa la página de inicio de sesión de SauceDemo."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        """Abre la página de login."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Completa las credenciales e intenta iniciar sesión."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Obtiene el mensaje de error del login."""
        return self.get_text(self.ERROR_MESSAGE)

    def wait_for_inventory(self):
        """Espera la redirección al catálogo."""
        return self.wait.until(
            EC.url_contains("/inventory.html")
        )
