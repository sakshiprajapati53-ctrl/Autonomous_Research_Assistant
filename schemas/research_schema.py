from pydantic import BaseModel,ConfigDict
from datetime import datetime

# Create Research Session
class ResearchCreate(BaseModel):
    query: str


# Research Response
class ResearchResponse(BaseModel):
    id: int
    query: str
    timestamp: datetime
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )