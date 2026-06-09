from langchain.tools import tool

@tool
def create_event(event: str) -> str:
    """Create an event."""
    return f"Event {event} created"


@tool
def delete_event(event_id: str) -> str:
    """Delete an event."""
    return f"Event {event_id} deleted"


@tool
def update_event(event_id: str, event: str) -> str:
    """Update an event."""
    return f"Event {event_id} updated with event: {event}"


@tool
def get_events() -> str:
    """Get events."""
    return "Events"
