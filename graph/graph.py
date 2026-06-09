from langgraph.graph import StateGraph
from graph.state import OrchestratorState
from graph.nodes.email_agent_node import email_agent_node
from graph.nodes.db_agent_node import db_agent_node
from graph.nodes.calender_agent_node import calender_agent_node
from graph.nodes.supervisor_agent_node import supervisor_agent_node

graph = StateGraph(OrchestratorState)
graph.add_node("supervisor", supervisor_agent_node)
graph.add_node("email_agent", email_agent_node)
graph.add_node("db_agent", db_agent_node)
graph.add_node("calender_agent", calender_agent_node)

graph.set_entry_point("supervisor")
graph.add_edge("supervisor", "email_agent")
graph.add_edge("supervisor", "db_agent")
graph.add_edge("supervisor", "calender_agent")
graph.add_edge("email_agent", "supervisor")
graph.add_edge("db_agent", "supervisor")
graph.add_edge("calender_agent", "supervisor")
graph.set_finish_point("supervisor")

graph_builder = graph.compile()

