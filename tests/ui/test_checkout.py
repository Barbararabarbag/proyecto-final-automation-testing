
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_compra_completa_exitosa(driver):
    """Verifica el flujo completo de compra en SauceDemo."""

    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.wait_for_inventory()

    # Agregar producto
    inventory_page = InventoryPage(driver)
    inventory_page.add_first_product_to_cart()

    assert inventory_page.get_cart_count() == 1

    # Ir al carrito
    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert len(cart_page.get_products()) == 1

    # Iniciar checkout
    cart_page.go_to_checkout()

    checkout_page = CheckoutPage(driver)

    # Completar datos del comprador
    checkout_page.complete_customer_information(
        "Barbara",
        "Barbagalo",
        "1900"
    )

    # Validar resumen de compra
    assert checkout_page.get_summary_title() == "Checkout: Overview"

    # Finalizar compra
    checkout_page.finish_purchase()

    # Validar confirmación
    assert checkout_page.get_confirmation_message() == (
        "Thank you for your order!"
    )
