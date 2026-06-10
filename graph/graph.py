from langgraph.graph import StateGraph, END
from graph.state import OrchestratorState
from graph.nodes.email_agent_node import email_agent_node
from graph.nodes.db_agent_node import db_agent_node
from graph.nodes.calender_agent_node import calender_agent_node
from graph.nodes.supervisor_agent_node import supervisor_agent_node
from graph.nodes.route_node import route_node

graph = StateGraph(OrchestratorState)
graph.add_node("supervisor", supervisor_agent_node)
graph.add_node("email_agent", email_agent_node)
graph.add_node("db_agent", db_agent_node)
graph.add_node("calender_agent", calender_agent_node)
graph.add_node("route", route_node)

graph.set_entry_point("supervisor")
graph.add_conditional_edges("supervisor", route_node,    {
        "email_agent": "email_agent",
        "db_agent": "db_agent",
        "calender_agent": "calender_agent",
        "END": END
    })

graph.add_edge("email_agent", "supervisor")
graph.add_edge("db_agent", "supervisor")
graph.add_edge("calender_agent", "supervisor")
graph.add_edge("supervisor", END)

graph_builder = graph.compile()

