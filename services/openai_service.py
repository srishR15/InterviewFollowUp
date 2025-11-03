import os
from openai import AsyncOpenAI
from schemas import InterviewRequest


api_key = os.getenv("OPENAI_API_KEY")
client = AsyncOpenAI(api_key=api_key)

async def generate_followup_question(payload: InterviewRequest) -> str:
    """Calls OpenAI to generate a follow-up question with rationale."""
    
    system_prompt = (
        "You are an expert technical interviewer. "
        "Given an interview question and the candidate’s answer, "
        "generate one concise, contextually relevant follow-up question. "
        "Do not repeat the original question or restate the answer. "
        "Avoid asking yes/no questions. Keep it professional and insightful."
    )

    user_prompt = f"""
Original Question: {payload.question}
Candidate Answer: {payload.answer}
Role: {payload.role or "Not specified"}
Interview Type: {', '.join(payload.interview_type) if payload.interview_type else "General"}

Now generate one short follow-up question the interviewer can ask next.
"""

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=100,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()