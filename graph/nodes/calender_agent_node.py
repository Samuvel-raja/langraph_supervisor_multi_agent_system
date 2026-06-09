from agents.calender_agent import calender_agent
from graph.state import OrchestratorState

def calender_agent_node(state: OrchestratorState):
    result = calender_agent.invoke(state)
    return {"messages": result["messages"]}