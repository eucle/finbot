FROM python:3.11.6-slim

RUN pip install poetry

WORKDIR /app

COPY . /app

RUN poetry install --no-dev

CMD ["poetry", "run", "python", "./finbot/bot.py"]
