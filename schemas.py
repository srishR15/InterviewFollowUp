from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class InterviewRequest(BaseModel):
    question: str = Field(..., description="Original interview question")
    answer: str = Field(..., description="Candidate’s answer text")
    role: Optional[str] = Field(None, description="Target role/title")
    interview_type: Optional[List[str]] = Field(None, description="Interview type(s)")

class InterviewResponse(BaseModel):
    result: str
    message: str
    data: Dict[str, str]