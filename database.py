import uuid
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings


async_engine = create_async_engine(settings.DATABASE_URL, echo=False, future=True)
async_session_maker = async_sessionmaker(bind=async_engine,autoflush=True,autocommit=False,expire_on_commit=False)
Base = declarative_base(metadata=MetaData())


def generate_uuid():
    return str(uuid.uuid4())