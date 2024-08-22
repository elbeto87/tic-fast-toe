# Tic-Fast-Toe

Tic Tac Toe game built using FastAPI.

This is a simple API implementation of the classic Tic Tac Toe game, allowing users to start a new game and interact with it through HTTP requests.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: You can download it from [python.org](https://www.python.org/).
- **pip**: Python package installer, which typically comes with Python.

## Installation

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

3. **Start a new Tic Tac Toe game**:
    Open your browser and go to:
    ```bash
    http://127.0.0.1:8000/start_game
    ```

    This will return a JSON response with the initial state of the game board.

## Usage

Here's how you can use the API:

- **Start Game**: 
    - `GET /start_game`
    - This endpoint initializes a new Tic Tac Toe game and returns the initial game board.

- **API Example**:
    - After starting the server, you can use tools like Postman or cURL to interact with the API.
    - Example cURL request:
    ```bash
    curl http://127.0.0.1:8000/start_game
    ```

    Example response:
    ```json
    {
        "message": "Welcome to Tic Tac Toe!",
        "board": [
            "_ | _ | _",
            "_ | _ | _",
            "_ | _ | _"
        ]
    }
    ```
  
## Usage using Docker

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
  
## Testing

To run the tests, use the following command:

```bash 
python -m pytest
```

## License

This project is licensed under the GNU General Public License v3.0.
