from langchain_mcp_adapters.client import MultiServerMCPClient
from Mcp.email_mcp_config import EMAIL_MCP_CONFIG
from Mcp.calender_mcp_config import CALENDER_MCP_CONFIG

async def get_mcp_tools():
    email_client = MultiServerMCPClient(EMAIL_MCP_CONFIG)
    calender_client = MultiServerMCPClient(CALENDER_MCP_CONFIG)
    email_tools = await email_client.get_tools()
    calender_tools = await calender_client.get_tools()
    return {
        "email_tools":email_tools,
        "calender_tools":calender_tools
    }