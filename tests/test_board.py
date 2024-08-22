import pytest
from fastapi.testclient import TestClient
from http import HTTPStatus
from main import app

client = TestClient(app)


@pytest.fixture(scope="function")
def new_game():
    client.post("/")


def test_start_game_endpoint(new_game):
    response = client.post("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "message": "Welcome to Tic Fast Toe",
        "board": ["_ | _ | _", "_ | _ | _", "_ | _ | _"]
    }


def test_make_move_request_endpoint(new_game):
    response = client.post("/make_move_request", json={"row": 1, "col": 1})

    assert response.status_code == HTTPStatus.OK
    assert response.json()["message"] == "Move made successfully"
    assert response.json()["board"][0][0] == "X"
