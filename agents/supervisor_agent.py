from langchain.agents import create_agent
from utils.llm import get_openai_llm
from prompts.supervisor_agent_prompt import SUPERVISOR_AGENT_PROMPT

supervisor_agent = create_agent(
    model=get_openai_llm(),
    tools=[],
    system_prompt=SUPERVISOR_AGENT_PROMPT,
)