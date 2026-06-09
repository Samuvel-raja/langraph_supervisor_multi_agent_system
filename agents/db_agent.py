from langchain.agents import create_agent
from utils.llm import get_openai_llm
from tools.db_agent_tools import create_note,get_notes,delete_note,update_note
from prompts.db_agent_prompt import DB_AGENT_PROMPT

db_agent = create_agent(
    model=get_openai_llm(),
    tools=[create_note,get_notes,delete_note,update_note],
    system_prompt=DB_AGENT_PROMPT,
)