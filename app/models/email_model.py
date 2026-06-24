from pydantic import BaseModel, Field

class EmailRequest(BaseModel):
    purpose: str = Field(
        min_length=5,
        max_length=500
    )