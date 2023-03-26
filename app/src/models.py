from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    password: str
    is_active: str
    created_at: Optional[str] = datetime.utcnow()
    timestamp: datetime = datetime.timestamp(datetime.utcnow())
    last_login: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "Email": "test@foondamate.com",
                "password": "fakehashedsecret",
                "is_active": "false",
                "created_at": "datetime",
                "timestamp": "datetime",
                "last_login": "datetime",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str
