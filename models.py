from pydantic import BaseModel, Field


class Terrorists(BaseModel):
    name: str 
    location: str
    danger_rate: float = Field(ge=1, le=10)