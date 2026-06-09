from agents.supervisor_agent import supervisor_agent
from graph.state import OrchestratorState

def supervisor_agent_node(state: OrchestratorState):
    result = supervisor_agent.invoke(state)
    print(result,"result")
    return {"messages": result["messages"]}
