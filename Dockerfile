FROM python:3.12-slim

RUN pip install --upgrade pip \
    && pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --without dev

COPY ./src /app

CMD ["python", "main.py"]
