from agents.email_agent import email_agent
from graph.state import OrchestratorState

def email_agent_node(state: OrchestratorState):
    result = email_agent.invoke(state)
    return {"messages": result["messages"]}
