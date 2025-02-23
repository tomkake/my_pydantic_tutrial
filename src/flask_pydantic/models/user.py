
from pydantic import BaseModel, field_validator

class User(BaseModel):
    id: int
    name: str = "John"

    @field_validator("name")
    def validate_name(cls,name: str) -> str:
        if len(name) > 10:
            raise ValueError("ame is too long, it must be 255 characters or less")
        return name