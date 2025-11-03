from fastapi import FastAPI, HTTPException
from schemas import InterviewRequest, InterviewResponse
from services.openai_service import generate_followup_question
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Interview Follow-up Generator", version="1.0.0")

@app.post("/interview/generate-followups", response_model=InterviewResponse)
async def generate_followups(payload: InterviewRequest):
    try:
        followup = await generate_followup_question(payload)
        return InterviewResponse(
            result="success",
            message="Follow-up question generated.",
            data={"followup_question": followup}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))