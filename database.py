import uuid
from sqlalchemy.schema import MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(metadata=MetaData())


def generate_uuid():
    return str(uuid.uuid4())