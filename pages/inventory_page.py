
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Representa el catálogo de productos de SauceDemo."""

    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_FILTER = (By.CLASS_NAME, "product_sort_container")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_products(self):
        return self.wait.until(
            lambda driver: driver.find_elements(*self.PRODUCTS)
        )

    def get_first_product(self):
        product = self.get_products()[0]

        name = product.find_element(
            *self.PRODUCT_NAMES
        ).text

        price = product.find_element(
            *self.PRODUCT_PRICES
        ).text

        return name, price

    def add_first_product_to_cart(self):
        product = self.get_products()[0]

        add_button = product.find_element(
            By.TAG_NAME, "button"
        )

        add_button.click()

    def get_cart_count(self):
        badge = self.wait_for_element(self.CART_BADGE)
        return int(badge.text)

    def open_cart(self):
        self.click(self.CART_LINK)
        self.wait.until(
            lambda driver: "/cart.html" in driver.current_url
        )

    def is_sort_filter_visible(self):
        return self.wait_for_element(
            self.SORT_FILTER
        ).is_displayed()
