# Tic-Fast-Toe

Tic Tac Toe game built using FastAPI.

This is a simple API implementation of the classic Tic Tac Toe game, allowing users to start a new game and interact with it through HTTP requests.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10**: You can download it from [python.org](https://www.python.org/).
- **pip**: Python package installer, which typically comes with Python.

## Installation (locally)

Follow these steps to get the project running locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/elbeto87/tic-fast-toe.git
    cd tic-fast-toe
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

1. **Start the FastAPI server**:
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    Open your browser and go to:
    ```bash
    http://127.0.0.1:8000/docs
    ```
    This will open the interactive Swagger UI where you can test the API endpoints.

  
## Installation (Docker)

1. **Build the Docker image**:
    ```bash
    docker build -t tic-fast-toe .
    ```
2. **Run the Docker container**:
    ```bash
    docker run -d -p 8000:8000 tic-fast-toe
    ```
3. **Stop the Docker container**:
    ```bash
    docker stop <container_id>
    ```

## Usage

Here's how you can use the API:

1. **Start a new game**:
    - Send a `POST` request to `/` to start a new game.
    - **Response**:
        ```json
        {
            "message": "Welcome to Tic Fast Toe",
            "board": [
                "_ | _ | _",
                "_ | _ | _",
                "_ | _ | _"
            ]
        }
        ```

2. **Make a move**:
    - Send a `POST` request to `/make_move_request` with the following JSON payload:
    ```json
    {
        "row": 0,
        "col": 0
    }
    ```
    - Replace the values of `row` and `col` with the desired move.
    - **Response**:
        - If the player wins:
        ```json
        {
            "message": "Player X wins!",
            "board": [
                "X | X | X",
                "_ | O | _",
                "O | O | _"
            ]
        }
        ```
        - If the computer wins:
        ```json
        {
            "message": "Player O wins!",
            "board": [
                "X | X | _",
                "O | O | O",
                "X | _ | _"
            ]
        }
        ```
        - If no one wins yet:
        ```json
        {
            "message": "Move made successfully",
            "board": [
                "X | _ | _",
                "_ | _ | _",
                "_ | _ | _"
            ]
        }
        ```

3. **Get Game History**:
    - Send a `GET` request to `/game_history`.
    - **Response**:
    ```json
    {
        "game_history": [
            {
                "timestamp": "2024-08-22 10:00:00",
                "winner": "X"
            },
            {
                "timestamp": "2024-08-22 11:00:00",
                "winner": "O"
            }
        ]
    }
    ```

4. **Count of Wins**:
    - Send a `GET` request to `/count_of_wins`.
    - **Response**:
    ```json
    {
        "player_wins": 3,
        "computer_wins": 2
    }
    ```
  
## Testing

To run the tests, use the following command:

```bash 
python -m pytest
```

## License

This project is licensed under the GNU General Public License v3.0.
