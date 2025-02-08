import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.engine import Connection as ConnectionSqlalchemy
from sqlalchemy.ext.asyncio import AsyncEngine

from app.infrastructure.database.models.base import BaseModel
from app.settings.database.database_settings import DatabaseSettings

ALEMBIC_MIGRATION_FILENAME_TEMPLATE: str = (
    "%%(year)d_" "%%(month).2d_" "%%(day).2d_" "%%(hour).2d_" "%%(minute).2d_" "%%(second).2d_" "%%(slug)s"
)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

db_settings = DatabaseSettings()

config.set_main_option("file_template", ALEMBIC_MIGRATION_FILENAME_TEMPLATE)
config.set_main_option("timezone", "UTC")
config.set_main_option("sqlalchemy.url", db_settings.dsn())

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = BaseModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: ConnectionSqlalchemy) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = AsyncEngine(
        engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        ),
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
