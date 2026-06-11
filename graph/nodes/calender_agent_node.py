from agents.calender_agent import calender_agent
from graph.state import OrchestratorState

async def calender_agent_node(state: OrchestratorState):
    result = await calender_agent.ainvoke(state)
    return {"messages": result["messages"]}