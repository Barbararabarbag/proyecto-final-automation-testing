# Proyecto Final - QA Automation | Barbara Barbagalo

## Descripción

Proyecto de automatización de pruebas funcionales y de API, desarrollado como proyecto final de la formación en Automatización QA de Talento Tech.

Se automatizan distintos escenarios sobre la aplicación web **[SauceDemo](https://www.saucedemo.com/)** y se realizan pruebas de servicios REST sobre **JSONPlaceholder**.

El proyecto utiliza Python, Selenium WebDriver y Pytest, aplicando el patrón de diseño Page Object Model (POM) para organizar y mantener el código de automatización.

## Tecnologías y herramientas

- Python 3.14.3
- Pytest 9.1.1
- Selenium WebDriver 4.49.0
- pytest-html 4.2.0
- Requests
- Google Chrome
- Visual Studio Code
- Git y GitHub

## Arquitectura y estructura del proyecto

```text
proyecto-final-automation-testing-barbara-barbagalo/
│
├── data/
│   └── login_data.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── api/
│   │   └── test_api.py
│   │
│   └── ui/
│       ├── test_login.py
│       ├── test_inventory.py
│       ├── test_cart.py
│       └── test_checkout.py
│
├── logs/
├── screenshots/
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Patrón de diseño: Page Object Model (POM)

Para las pruebas de interfaz se implementó el patrón Page Object Model.

Cada página de la aplicación tiene una clase propia que centraliza sus localizadores y acciones:

- `BasePage`: contiene métodos reutilizables para interactuar con los elementos y gestionar esperas.
- `LoginPage`: gestiona el inicio de sesión.
- `InventoryPage`: gestiona el catálogo y la selección de productos.
- `CartPage`: gestiona las operaciones del carrito.
- `CheckoutPage`: gestiona el proceso de compra.

Esta organización permite separar la lógica de interacción con la aplicación de los casos de prueba.

## Pruebas automatizadas

El proyecto cuenta con **13 pruebas automatizadas: 10 de interfaz (UI) y 3 de API**.

### 1. Pruebas de interfaz (UI)

Se utiliza Selenium WebDriver para automatizar los flujos de SauceDemo.

**Login – 4 escenarios parametrizados**

Los datos de prueba se encuentran externalizados en `data/login_data.json`.

- Inicio de sesión exitoso.
- Usuario bloqueado.
- Credenciales incorrectas.
- Campos vacíos.

**Inventario – 3 escenarios**

- Verificación de visualización del catálogo.
- Verificación del nombre y precio de un producto.
- Verificación del filtro de ordenamiento.

**Carrito – 2 escenarios**

- Agregar un producto y verificar su presencia en el carrito.
- Verificar que el carrito esté vacío inicialmente.

**Checkout – 1 escenario**

- Completar el proceso de compra.
- Verificar la información del resumen.
- Validar el mensaje de confirmación de compra.

### 2. Pruebas de API

Se utiliza la biblioteca Requests para realizar solicitudes HTTP a JSONPlaceholder.

- **GET:** obtener publicaciones y validar el código de respuesta y la estructura del contenido.
- **POST:** crear una publicación y validar la respuesta y los datos enviados.
- **DELETE:** eliminar una publicación y validar el código de respuesta.

## Sincronización y esperas

Se implementaron esperas explícitas mediante `WebDriverWait` y `Expected Conditions` para sincronizar las interacciones con los elementos de la aplicación y reducir problemas de sincronización.

## Manejo de errores, capturas y logs

El proyecto utiliza fixtures y hooks de Pytest configurados en `conftest.py`.

- Se inicializa y cierra el navegador mediante una fixture.
- Se registran eventos de ejecución mediante el módulo `logging`.
- Se genera una captura de pantalla automáticamente cuando falla una prueba de interfaz.
- Las capturas incluyen el nombre del test y una marca de fecha y hora.

Los archivos se almacenan en:

- `logs/automation.log`
- `screenshots/`

## Reportes HTML

Se utiliza el plugin `pytest-html` para generar reportes de ejecución autocontenidos.

Para generar el reporte:

```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

El archivo se genera en `reports/reporte.html`.

## Instalación y ejecución

### Requisitos previos

- Python instalado.
- Google Chrome instalado.
- Conexión a Internet para acceder a los sitios de prueba y a la API.

### 1. Instalar dependencias

Desde la raíz del proyecto:

```bash
python -m pip install -r requirements.txt
```

### 2. Ejecutar todas las pruebas

```bash
python -m pytest -v
```

### 3. Ejecutar únicamente las pruebas de interfaz

```bash
python -m pytest tests/ui -v
```

### 4. Ejecutar únicamente las pruebas de API

```bash
python -m pytest tests/api -v
```

### 5. Generar el reporte HTML

```bash
python -m pytest -v --html=reports/reporte.html --self-contained-html
```

## Resultado de ejecución

Última ejecución completa:

- **13 pruebas ejecutadas**
- **13 pruebas aprobadas**
- **0 pruebas fallidas**

## Autora

**Bárbara Barbagalo**

QA Manual | Analista Funcional

Formación en Automatización QA – Talento Tech