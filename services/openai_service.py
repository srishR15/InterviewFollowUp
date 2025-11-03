import os
from openai import AsyncOpenAI
from schemas import InterviewRequest
from services.memory_manager import add_message, get_conversation

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are an expert interviewer who asks concise, relevant follow-up questions. "
    "Always base your next question on the previous conversation. "
    "Avoid yes/no, repetitive, or leading questions."
)

async def generate_followup_question(payload: InterviewRequest, session_id: str) -> str:
    """Generate a follow-up question while keeping prior context."""
    
    conversation = get_conversation(session_id)
    
    # If this is a new session, start fresh
    if not conversation:
        add_message(session_id, "system", SYSTEM_PROMPT)
        add_message(session_id, "user", f"Original Question: {payload.question}")
        add_message(session_id, "assistant", "(First follow-up question placeholder)")
    
    # Add candidate's latest answer
    add_message(session_id, "user", f"Candidate Answer: {payload.answer}")
    
    # Send the full conversation context to OpenAI
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=get_conversation(session_id),
        max_tokens=100,
        temperature=0.7,
    )

    followup = response.choices[0].message.content.strip()
    add_message(session_id, "assistant", followup)

    return followup