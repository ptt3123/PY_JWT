from sqlalchemy.sql import func, expression
from sqlalchemy.schema import Column
from sqlalchemy.types import String, DateTime, Boolean

from database import Base, generate_uuid

class User(Base):
    __tablename__ = "user"
    id = Column("id", String(36), primary_key=True, default=generate_uuid, index=True)
    username = Column("username", String(30), nullable=False, unique= True)
    password = Column("password", String(100), nullable= False)

    first_name = Column("first_name", String(30), nullable= False)
    last_name = Column("last_name", String(30), nullable= False)
    email = Column("email", String(30), nullable= False, unique= True)
    phone_number = Column("phone_number", String(10), nullable= False, unique= True)
    create_at = Column("create_at", DateTime, nullable= False, server_default=func.now())
    update_at = Column("update_at", DateTime, nullable= False, onupdate=func.now())
    is_active = Column("is_active", Boolean, nullable= False, server_default=expression.false())
    is_staff = Column("is_staff", Boolean, nullable= False, server_default=expression.false())