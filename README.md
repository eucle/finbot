## Описание
ExpenditureBot — телеграм-бот для учета личных расходов. 

Позволяет в удобной форме фиксировать ежедневные расходы по 30+ категориям и средствам платежа. Категории и средства платежа можно легко кастомизировать — добавление новых и редактирование существующих производим тут: finbot/lexicon/lexicon.py

Результаты за любой период можно наглядно отобразить на графиках на дашборде и в админпанели в браузере.

В разработке использованы:
* основная часть: aiogram, PostgreSQL, SQLAlchemy, Redis;
* [дашборд, админпанель](https://github.com/eucle/finbot_django): Django, Bootstrap;
* графики: Chart.js.

В этом репозитории находится основная часть, дашборд и админпанель можно найти [тут](https://github.com/eucle/finbot_django).

## Технологии основной части
* Python 3.11;
* aiogram 3.x (фреймворк для создания ТГ-ботов)
* PostgreSQL (база данных);
* SQLAlchemy (обеспечивает связь бота с базой данных)
* Redis (NoSQL база данных для реализации конечного автомата - FSM)
* psycopg3 (драйвер базы данных для SQLAlchemy)
* loguru (библиотека для логирования)

Для установки зависимостей используйте `poetry`.

Перед запуском бота нужно переименовать файл .env.example в .env, и указать в .env:
* токен вашего ТГ-бота, 
* данные для подключения к вашей БД PostgreSQL,
* хост вашей БД Redis,
* ID вашего ТГ-аккаунта (с которого вы будете посылать боту команды).

<img src="https://github.com/eucle/bot_files/blob/main/scr001.jpeg" width="300">

---
<img src="https://github.com/eucle/bot_files/blob/main/scr002.jpeg" width="300">

---
<img src="https://github.com/eucle/bot_files/blob/main/scr003.png" width="600">

---
<img src="https://github.com/eucle/bot_files/blob/main/scr004.png" width="600">
