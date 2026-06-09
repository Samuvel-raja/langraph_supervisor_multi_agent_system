from langchain.agents import create_agent
from utils.llm import get_openai_llm
from tools.email_agent_tools import send_email, create_email, create_draft, delete_email
from prompts.email_agent_prompt import EMAIL_AGENT_PROMPT

email_agent = create_agent(
    model=get_openai_llm(),
    tools=[send_email, create_email, create_draft, delete_email],
    system_prompt=EMAIL_AGENT_PROMPT,
)
