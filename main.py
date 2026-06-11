from dotenv import load_dotenv
load_dotenv()

from graph.graph import graph_builder
from langchain_core.messages import HumanMessage
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"status": "ok"}

@app.post("/process")
async def process_message(message: str):
    result = await graph_builder.ainvoke( {
        "messages": [
            HumanMessage(
                content=message
            )
        ],
        "goto": "",
        "email": {
            "to": "",
            "subject": "",
            "body": ""
        },
    })
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



