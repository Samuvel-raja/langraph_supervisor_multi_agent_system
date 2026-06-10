from dotenv import load_dotenv
load_dotenv()

from graph.graph import graph_builder
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    result = graph_builder.invoke( {
        "messages": [
            HumanMessage(
                content="i want to send a email to john@example.com"
            )
        ],
        "goto": "",
        "email": {
            "to": "",
            "subject": "",
            "body": ""
        },
    })
    print(result)


