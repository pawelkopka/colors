import pytest
from colors import colors



@pytest.fixture
def client():
    colors.app.config["ENVIRONMENT"] = "Testing"
    colors.colors_cache = colors.load_colors("tests/test_colors.json")
    with colors.app.test_client() as client:
        yield client


def test_list_colors(client):
    response = client.get("/")
    assert response.status_code == 200
    assert ["red", "green"] == response.json


def test_get_color(client):
    response = client.get("/red")
    assert response.status_code == 200
    assert {"color": "red", "value": "#f00"} == response.json


def test_not_found_color(client):
    response = client.get("/blue")
    assert response.status_code == 404
    assert "Color not found" in str(response.data)


def test_add_color(client):
    response = client.post("/blue", data="#00f")
    assert response.status_code == 200
    assert {"color": "blue", "value": "#00f"} == response.json
    response = client.get("/")
    assert response.status_code == 200
    assert ["red", "green", "blue"] == response.json
