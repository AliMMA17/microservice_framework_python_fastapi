# migrations/env.py
import os
import sys
from pathlib import Path
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# --- (optional) load .env when running locally ---
# pip install python-dotenv  (only if you want .env auto-loaded outside Docker)
try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
except Exception:
    pass

# Make sure project root is importable (so "lib" and "src" imports work)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Alembic config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Import your Base + models so metadata is populated ---
from lib.db.postgres import Base      # DeclarativeBase defined in your template
import src.models  # noqa: F401       # IMPORTANT: import models to register tables

target_metadata = Base.metadata

def _build_sync_dsn() -> str:
    """
    Use ALEMBIC_DATABASE_URL if set, otherwise build from POSTGRES_* env vars.
    This lets you keep everything in .env.
    """
    dsn = os.getenv("ALEMBIC_DATABASE_URL", "").strip()
    if dsn:
        return dsn
    user = os.getenv("POSTGRES_USER", "postgres")
    pwd  = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "db")
    port = "5432"
    db   = os.getenv("POSTGRES_DB", "postgres")
    return f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"

# Force the URL here (alembic.ini is just a fallback)
config.set_main_option("sqlalchemy.url", _build_sync_dsn())

def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
