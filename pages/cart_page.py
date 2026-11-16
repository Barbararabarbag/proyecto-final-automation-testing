
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    """Representa el carrito de compras."""

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def get_products(self):
        return self.driver.find_elements(*self.CART_ITEMS)

    def get_product_names(self):
        items = self.wait.until(
        EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )
        return [
        item.find_element(*self.PRODUCT_NAMES).text
        for item in items
        ]
    
    def is_product_in_cart(self, product_name):
        return product_name in self.get_product_names()

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
