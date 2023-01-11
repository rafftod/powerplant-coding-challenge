FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY src /app
COPY pyproject.toml /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

CMD ["python3", "main.py"]