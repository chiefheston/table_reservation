# FastAPI + PostgreSQL + SQLAlchemy + Alembic + Docker

API-сервис бронирования столиков в ресторане с помощью **FastAPI** с использованием **SQLAlchemy** для работы с **PostgreSQL**, миграциями через **Alembic** и контейнеризацией через **Docker**.

Сервис предоставляет REST API для бронирования столиков в ресторане. Он позволяет создавать, просматривать и удалять брони, а также управлять столиками и временными слотами.

---

### Стек

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

2. Создание .env файла:

   Для корректной работы сервиса, нужно создать `.env` файл в главной директории сервиса `app/` с такими переменными:

   ```env
   DB_URL=postgresql+asyncpg://dev:dev@localhost:5433/tablereservation
   ```

3. Сборка и запуск контейнеров:

   ```bash
   docker-compose up --build
   ```

4. Создание первой миграции:

   ```bash
   docker-compose exec web alembic revision --autogenerate -m "Название миграции"
   ```

5. Примените миграции:

   ```bash
   docker-compose exec web alembic upgrade head
   ```

6. Пользуйтесь API

   Сервис доступен по адресу [http://localhost:8000/docs](http://localhost:8000/docs).

---
