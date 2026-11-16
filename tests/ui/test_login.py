
import json
import pytest

from pathlib import Path

from pages.login_page import LoginPage


# Cargar los datos externos desde JSON
DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "login_data.json"
)

with open(DATA_FILE, encoding="utf-8") as file:
    login_data = json.load(file)


@pytest.mark.parametrize(
    "test_data",
    login_data,
    ids=[data["description"] for data in login_data]
)
def test_login_parametrizado(driver, test_data):
    """Verifica distintos escenarios de inicio de sesión."""

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    if test_data["expected"] == "success":
        assert login_page.wait_for_inventory()
        assert "/inventory.html" in driver.current_url

    else:
        error_message = login_page.get_error_message()
        assert error_message != ""
