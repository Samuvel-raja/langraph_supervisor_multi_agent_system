from typing import Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from pydantic import BaseModel


class Email(BaseModel):
    to: str
    subject: str
    body: str
    

class OrchestratorState(BaseModel):
    messages: Annotated[list[AnyMessage], add_messages]
    goto: str=""
    email: Email=None