from bson import ObjectId
from enum import Enum
from pydantic import BaseModel, Field


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


class ReportType(str, Enum):
    quarterly = "quarterly"
    yearly = "yearly"


class Report(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    stock_code: str = Field(...)
    date: int = Field(...)
    income_statement: dict = Field(...)
    balance_sheet: dict = Field(...)
    cash_flow: dict = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": "string",
                "stock_code": "string",
                "date": 0,
                "income_statement": {},
                "balance_sheet": {},
                "cash_flow": {},
            }
        }
