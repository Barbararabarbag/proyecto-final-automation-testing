
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_agregar_producto_al_carrito(driver):
    """Verifica que un producto se agregue correctamente al carrito."""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    inventory_page = InventoryPage(driver)

    product_name, product_price = inventory_page.get_first_product()

    inventory_page.add_first_product_to_cart()

    assert inventory_page.get_cart_count() == 1

    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.is_product_in_cart(product_name)


def test_carrito_vacio(driver):
    """Verifica que el carrito esté vacío antes de agregar productos."""

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    inventory_page = InventoryPage(driver)
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert len(cart_page.get_products()) == 0
