from config import settings

CALENDER_MCP_CONFIG = {
    "calendar": {
        "transport": "streamable_http",
        "url": "https://calendarmcp.googleapis.com/mcp/v1",
        "auth": {
            "client_id": settings.google_client_id,      
            "client_secret": settings.google_client_secret,  
            "scopes": [
                "https://www.googleapis.com/auth/calendar.readonly",
                "https://www.googleapis.com/auth/calendar.events"
            ]
        }
    }
}