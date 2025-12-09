# import os, sys
# from pathlib import Path
# from logging.config import fileConfig

# from sqlalchemy import pool, engine_from_config

# from alembic import context


# config = context.config


# current_path = Path(__file__).resolve()
# project_root = current_path.parents[4] 

# sys.path.append(str(project_root))

# # 2. Импортируем ваш базовый класс Base и все файлы с моделями
# # Убедитесь, что эти импорты соответствуют вашей структуре папок:

# from App.Core.Database.Requests.session import Base
# from App.Core.Database.Models.user import User
# from App.Core.Database.Models.operators import Operator
# from App.Core.Database.Models.admin import Admin


# db_url = os.getenv("DB_URL")
# if db_url:
#     config.set_main_option("sqlalchemy.url", db_url + "?async_fallback=True")
# else:
#     raise RuntimeError("❌ DB_URL не найдена в окружении!")


# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# # target_metadata = mymodel.Base.metadata
# print(f"DEBUG: sys.path is: {sys.path}")
# print(f"DEBUG: Base metadata tables: {Base.metadata.tables.keys()}")

# target_metadata = Base.metadata

# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.


# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode.

#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.

#     Calls to context.execute() here emit the given string to the
#     script output.

#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()


# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.

#     """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()


import asyncio
import os
import sys
from logging.config import fileConfig
from pathlib import Path

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# --- 1. Настройка путей (чтобы видеть папку App) ---
# Поднимаемся из App/Core/Database/Migrations в корень проекта
current_path = Path(__file__).resolve()
project_root = current_path.parents[4]
sys.path.append(str(project_root))

# --- 2. Импорты моделей ---
# Импортируем Base и ВСЕ модели, чтобы они зарегистрировались в metadata
from App.Core.Database.Requests.session import Base
from App.Core.Database.Models.user import User
from App.Core.Database.Models.operators import Operator
from App.Core.Database.Models.admin import Admin

# --- 3. Конфигурация Alembic ---
config = context.config

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаданные для автогенерации
target_metadata = Base.metadata

# --- 4. Получение URL базы данных ---
# Читаем из переменной окружения (как у тебя было)
db_url = os.getenv("DB_URL")
if not db_url:
    raise RuntimeError("❌ DB_URL не найдена в переменных окружения!")

# Подменяем URL в конфиге Alembic, чтобы использовать asyncpg, но для Alembic он нужен в виде строки
# Важно: Alembic в асинхронном режиме использует NullPool
config.set_main_option("sqlalchemy.url", db_url)


def run_migrations_offline() -> None:
    """Запуск миграций в 'offline' режиме (без подключения к БД)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Запуск миграций в 'online' режиме с использованием asyncpg."""
    
    # Создаем асинхронный движок
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Точка входа для online-миграций."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()