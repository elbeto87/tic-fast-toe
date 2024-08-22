from fastapi.testclient import TestClient
from http import HTTPStatus
from main import app

client = TestClient(app)


def test_start_game_endpoint():
    response = client.get("/start_game")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "message": "Welcome to Tic Fast Toe",
        "board": ["_ | _ | _", "_ | _ | _", "_ | _ | _"]
    }
