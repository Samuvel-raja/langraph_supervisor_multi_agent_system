from agents.db_agent import db_agent
from graph.state import OrchestratorState

async def db_agent_node(state: OrchestratorState):
    result = await db_agent.ainvoke(state)
    return {"messages": result["messages"]}
