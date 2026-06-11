from langchain.agents import create_agent
from utils.llm import get_openai_llm
from tools.email_agent_tools import send_email, create_email, create_draft, delete_email
from prompts.email_agent_prompt import EMAIL_AGENT_PROMPT
from Mcp.mcp_client import get_mcp_tools


async def get_email_tools():
    tools = await get_mcp_tools()
    return tools

async def email_agent_funct():
    tools = await get_email_tools()
    print("Email tools:", tools)
    email_agent = create_agent(
        model=get_openai_llm(),
        tools=tools,
        system_prompt=EMAIL_AGENT_PROMPT,
    )
    return email_agent
