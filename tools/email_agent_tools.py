from langchain.tools import tool

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email."""
    return f"Email sent to {to} with subject {subject} and body {body}"

@tool
def get_emails() -> str:
    """Get emails."""
    return "Emails"

@tool
def delete_email(email_id: str) -> str:
    """Delete an email."""
    return f"Email {email_id} deleted"

@tool
def create_email(email_id: str) -> str:
    """Create an email."""
    return f"Email {email_id} created"

@tool
def create_draft(email_id: str) -> str:
    """Create a draft email."""
    return f"Draft {email_id} created"
