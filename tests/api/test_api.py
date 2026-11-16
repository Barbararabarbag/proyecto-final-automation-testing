
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_obtener_publicaciones():
    """Verifica que la API devuelva publicaciones correctamente."""

    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    publicaciones = response.json()

    assert isinstance(publicaciones, list)
    assert len(publicaciones) > 0
    assert "title" in publicaciones[0]
    assert "body" in publicaciones[0]

def test_crear_publicacion():
    """Verifica que la API permita crear una publicación."""

    nueva_publicacion = {
        "title": "Prueba de automatizacion QA",
        "body": "Publicacion creada mediante una prueba POST",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=nueva_publicacion
    )

    assert response.status_code == 201

    datos = response.json()

    assert datos["title"] == nueva_publicacion["title"]
    assert datos["body"] == nueva_publicacion["body"]
    assert datos["userId"] == nueva_publicacion["userId"]
    assert "id" in datos

def test_eliminar_publicacion():
    """Verifica que la API permita eliminar una publicación."""

    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.json() == {}
