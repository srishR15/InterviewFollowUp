# services/memory_manager.py
from typing import Dict, List

# Simple in-memory store for now; can later swap with Redis or DB
_conversations: Dict[str, List[dict]] = {}

def get_conversation(session_id: str) -> List[dict]:
    """Retrieve the stored conversation for a session."""
    return _conversations.get(session_id, [])

def add_message(session_id: str, role: str, content: str):
    """Add a message to the conversation."""
    if session_id not in _conversations:
        _conversations[session_id] = []
    _conversations[session_id].append({"role": role, "content": content})

def clear_conversation(session_id: str):
    """Clear a session (optional endpoint)."""
    if session_id in _conversations:
        del _conversations[session_id]