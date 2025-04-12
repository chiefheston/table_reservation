# FastAPI + PostgreSQL + SQLAlchemy + Alembic + Docker

API-сервис бронирования столиков в ресторане с помощью **FastAPI** с использованием **SQLAlchemy** для работы с **PostgreSQL**, миграциями через **Alembic** и контейнеризацией через **Docker**.

Сервис предоставляет REST API для бронирования столиков в ресторане. Он позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами.

---

## Стек

- **FastAPI** — Основоной фреймворк.
- **PostgreSQL** — БД.
- **SQLAlchemy** — ORM для работы с БД.
- **Alembic** — Иструмент для миграций базы данных.
- **Docker** — Для контейнеризации сервиса.

---

## Быстрый старт

> Для того чтобы запустить сервис на своем компьютере, убедитесь, что у вас установлен [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/).

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/chiefheston/table_reservation.git
   cd table_reservation
   ```

2. Соберите и запустите контейнеры:

   ```bash
   docker-compose up --build -d
   ```

3. Примените `Alembic` миграции:

   ```bash
   docker-compose exec web alembic upgrade head
   ```

4. Пользуйтесь API

   Сервис доступен по адресу [http://localhost:8000/docs](http://localhost:8000/docs)

---
