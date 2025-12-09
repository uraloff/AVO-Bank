from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from App.Core.Settings import settings


DB_URL = settings.DB_URL


engine = create_async_engine(DB_URL)
async_session = async_sessionmaker(engine)


Base = declarative_base() 
