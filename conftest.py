
import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver


# Configuración de logs
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/automation.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    """Inicia y cierra Chrome para cada prueba de interfaz."""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)

    logger.info("Navegador iniciado")

    yield browser

    browser.quit()
    logger.info("Navegador cerrado")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda una captura cuando falla una prueba de interfaz."""

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")

        if browser:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("/", "_")

            screenshot_path = os.path.abspath(
                f"screenshots/{test_name}_{timestamp}.png"
            )

            browser.save_screenshot(screenshot_path)

            logger.error(
                "Prueba fallida: %s. Captura: %s",
                item.name,
                screenshot_path
            )

            report.screenshot_path = screenshot_path
