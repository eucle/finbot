# Используем базовый образ Python
FROM python:3.11.6-slim

# Устанавливаем зависимости
RUN pip install poetry

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости проекта
RUN poetry install --no-dev

# Запускаем приложение
CMD ["poetry", "run", "python", "./finbot/bot.py"]
