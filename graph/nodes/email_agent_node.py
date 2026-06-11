from langgraph.types import interrupt
from agents.email_agent import email_agent_funct
from graph.state import OrchestratorState

async def email_agent_node(state: OrchestratorState):
    email_agent = await email_agent_funct()
    result = await email_agent.invoke(state)
    email_data = result.get("email", {})
    to = email_data.get("to", "")
    subject = email_data.get("subject", "")
    body = email_data.get("body", "")
    if not to or not subject or not body:
        answer = interrupt(result["messages"][-1])
        return {"messages": result["messages"], "email_data": email_data, "answer": answer}
    return {"messages": result["messages"], "email_data": email_data}
