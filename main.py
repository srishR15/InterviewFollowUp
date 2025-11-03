from fastapi import FastAPI, HTTPException, Query
from schemas import InterviewRequest, InterviewResponse
from services.openai_service import generate_followup_question
from services.memory_manager import get_conversation, clear_conversation
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Interview Follow-up Generator", version="2.0.0")

@app.post("/interview/generate-followups", response_model=InterviewResponse)
async def generate_followups(payload: InterviewRequest, session_id: str = Query(..., description="Unique ID for this interview session")):
    try:
        followup = await generate_followup_question(payload, session_id)
        return InterviewResponse(
            result="success",
            message="Follow-up question generated.",
            data={"followup_question": followup}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/interview/session")
async def get_session(session_id: str):
    convo = get_conversation(session_id)
    return {"session_id": session_id, "turns": len(convo), "messages": convo}

@app.delete("/interview/session")
async def delete_session(session_id: str):
    clear_conversation(session_id)
    return {"session_id": session_id, "message": "Session cleared successfully"}