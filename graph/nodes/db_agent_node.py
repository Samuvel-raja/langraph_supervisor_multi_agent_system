from agents.db_agent import db_agent
from graph.state import OrchestratorState

def db_agent_node(state: OrchestratorState):
    result = db_agent.invoke(state)
    return {"messages": result["messages"]}
