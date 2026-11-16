
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_catalogo_muestra_productos(driver):
    """Verifica que el catálogo muestre productos."""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"
    assert len(inventory_page.get_products()) > 0


def test_catalogo_muestra_nombre_y_precio(driver):
    """Verifica que el primer producto tenga nombre y precio."""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    inventory_page = InventoryPage(driver)
    product_name, product_price = inventory_page.get_first_product()

    assert product_name != ""
    assert product_price.startswith("$")


def test_catalogo_muestra_filtro(driver):
    """Verifica que el filtro de ordenamiento esté visible."""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_sort_filter_visible()
