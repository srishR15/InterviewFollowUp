# Interview Follow-up Question Generator
An AI-powered backend built with FastAPI and OpenAI GPT models that automatically generates intelligent, context-aware follow-up questions for interviewers.
It supports multi-turn conversations, session memory, and REST endpoints to start, continue, and reset interviews.

## 🚀 Features
* Generate high-quality follow-up questions based on interviewer prompts and candidate answers
* Support for multiple interview types (Behavioral, Technical, System Design, etc.)
* Maintain session memory across multiple rounds using a session_id
* Simple REST API with POST, GET, and DELETE endpoints
* Ready to integrate with front-end clients

## 💻 Tech Stack
* Backend: FastAPI
* AI Engine: OpenAI GPT-4o-mini (via AsyncOpenAI SDK)
* Environment Management: python-dotenv
* Testing Tooling: Postman or Swagger UI

## 📡 API Endpoints
| Goal | Method | Route |
| :------------------------------- | :------: | -----------------------------------------------: |
| Generate new follow-up question | **POST** | `/interview/generate-followups?session_id=<id>` |
| Retrieve current session memory | **GET**  | `/interview/session?session_id=<id>`             |
| Clear or reset an interview session | **DELETE** | `/interview/session?session_id=<id>`             |

## 💾 Folder Structure
<img width="306" height="253" alt="image" src="https://github.com/user-attachments/assets/a1f15768-5920-413b-94cb-7c92618da621" />

## 🔧 Installation
### 1️⃣ Clone repository
```bash
git clone https://github.com/<your-username>/InterviewFollowUp.git
cd InterviewFollowUp
```

### 2️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```
### 3️⃣ Add your `.env` file
```bash
OPENAI_API_KEY=sk-your-api-key-here
```
## 🧠 Running the App
```bash
uvicorn main:app --reload
```
Then open in a browser:
### 👉 Swagger UI: http://127.0.0.1:8000/docs

## Test in Postman
### 1. Generate Follow-up Question
POST ` http://127.0.0.1:8000/interview/generate-followups?session_id=<id> `

Request Body:
```json
{
  "question": "Tell me about a time you handled conflicting priorities.",
  "answer": "In my last role, we had two urgent client requests. I triaged by impact and aligned stakeholders.",
  "role": "Senior Backend Engineer",
  "interview_type": ["Behavioral interview"]
}
```

Successful Response:
```json
{
  "result": "success",
  "message": "Follow-up question generated.",
  "data": {
    "followup_question": "How did you determine the impact of each client request when prioritizing your tasks?"
  }
}
```
Notes:
* The session_id query parameter links all turns of the same interview.
* Use the same session_id for all subsequent POSTs to continue the conversation.

### 2. Get Current Session Conversation
GET `http://127.0.0.1:8000/interview/session?session_id=<id>`

Example Response:
```json
{
  "session_id": "1234",
  "turns": 7,
  "messages": [
    {"role": "system", "content": "You are an expert interviewer..."},
    {"role": "user", "content": "Original Question: Tell me about a time you handled conflicting priorities."},
    {"role": "assistant", "content": "How did you determine the impact of each client request when prioritizing your tasks?"},
    {"role": "user", "content": "Candidate Answer: I compared impact and deadlines..."},
    {"role": "assistant", "content": "Can you describe a specific instance where your prioritization led to a positive outcome?"}
  ]
}
```
### 3. Clear Session Memory
DELETE `http://127.0.0.1:8000/interview/session?session_id=<id>`

Example Response:
```json
{
  "session_id": "1234",
  "message": "Session cleared successfully"
}
```
