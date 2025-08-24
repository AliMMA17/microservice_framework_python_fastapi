Minimal FastAPI + PostgreSQL + Alembic template for microservices.

- **FastAPI** app with routes in `main.py`
- **Postgres** via SQLAlchemy (async runtime)
- **Alembic** for migrations (no auto-create; migrations only)

## Requirements
- Docker + Docker Compose (recommended), or
- Python 3.12 + `pip` (for local dev)


Alembic commands :

alembic revision -m "manual migration"

apply migration : alembic upgrade head


setup: 
apply the alembic migration when the postgres is up