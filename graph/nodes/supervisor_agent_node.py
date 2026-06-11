from agents.supervisor_agent import supervisor_agent
from graph.state import OrchestratorState

def supervisor_agent_node(state: OrchestratorState):
    result = supervisor_agent.invoke(state)
import json
from agents.supervisor_agent import supervisor_agent
from graph.state import OrchestratorState

async def supervisor_agent_node(state: OrchestratorState):
    result = await supervisor_agent.ainvoke(state)
    content = result["messages"][-1].content

    content = content.replace("```json", "").replace("```", "").strip()

    route = json.loads(content)["route"]
    print(result,"result")

    return {"goto": route}
