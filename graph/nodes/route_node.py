from graph.state import OrchestratorState

async def route_node(state: OrchestratorState) -> str:
    route = state.goto
    if route == "email_agent":
        return "email_agent"
    elif route == "db_agent":
        return "db_agent"
    elif route == "calender_agent":
        return "calender_agent"
    elif route == "END":
        return "END"
    return "supervisor"
