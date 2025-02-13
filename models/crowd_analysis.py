from typing import Optional
from pydantic import BaseModel, Field

class CrowdAnalysisResult(BaseModel):
    estimated_count: int = Field(..., description = "The estimated number of people")
    threshold: int = Field(..., description = "The threshold used")
    warning: str = Field(..., description = "A warning message, or None")
    message: str = Field(..., description = "The full response message")