from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    name: str = Field(min_length=2)
    purpose: str = Field(min_length=3)