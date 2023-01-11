# powerplant-coding-challenge

I solved this challenge using :
- Python 3.10
- FastAPI to create the API
- Pydantic to validate the payload
- A greedy algorithm to solve the unit-commitment problem

## How to run the API

### Using Docker

```bash
docker build -t powerplant-coding-challenge .
docker run -p 8888:8888 powerplant-coding-challenge
```

### Using Python

```bash
poetry install
python main.py
```

## How to use the API

A GET request to http://localhost:8888/docs will open the Swagger UI describing the endpoints.