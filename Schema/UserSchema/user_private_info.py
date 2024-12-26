from uuid import UUID
from pydantic import BaseModel


class UserPrivateInfo(BaseModel):
    id: UUID
    is_active: bool
    is_staff: bool