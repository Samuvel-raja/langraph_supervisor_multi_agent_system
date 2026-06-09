from langchain.agents import create_agent
from utils.llm import get_openai_llm
from tools.calender_agent_tools import create_event,get_events,delete_event,update_event
from prompts.calender_agent_prompt import CALENDER_AGENT_PROMPT

calender_agent = create_agent(
    model=get_openai_llm(),
    tools=[create_event,get_events,delete_event,update_event],
    system_prompt=CALENDER_AGENT_PROMPT,
)