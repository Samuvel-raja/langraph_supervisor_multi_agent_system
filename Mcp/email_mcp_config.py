
from config import settings
EMAIL_MCP_CONFIG = {
    "gmail": {
        "transport": "streamable_http",
        "url": "https://gmailmcp.googleapis.com/mcp/v1",
        "auth": {
            "client_id": settings.google_client_id,
            "client_secret": settings.google_client_secret,
            "scopes": [
                "https://www.googleapis.com/auth/gmail.readonly",
                "https://www.googleapis.com/auth/gmail.compose"
            ]
        }
    }
}