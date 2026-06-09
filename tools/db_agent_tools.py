from langchain.tools import tool

@tool
def create_note(content: str) -> str:
    """Create a note."""
    return f"Note created with content: {content}"

@tool
def get_notes() -> str:
    """Get notes."""
    return "Notes"


@tool
def delete_note(note_id: str) -> str:
    """Delete a note."""
    return f"Note {note_id} deleted"


@tool
def update_note(note_id: str, content: str) -> str:
    """Update a note."""
    return f"Note {note_id} updated with content: {content}"

