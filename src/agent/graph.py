from typing_extensions import TypedDict
from langgraph.graph import END, START, StateGraph
from src.llm_client import generate_response


class TaskState(TypedDict):
    task: str
    result: str
    priority: str
    llm_response: str


def process_task(state: TaskState) -> dict:
    task = state["task"]

    return {
        "result": f"Processed task: {task}",
        "priority": (
            "urgent" if "urgent" in task.lower() else "normal"
        ),
    }
def llm_node(state: TaskState) -> dict:
    response = generate_response(state["task"])

    return {
        "llm_response": response
    }


def route_by_priority(state: TaskState) -> str:
    if state["priority"] == "urgent":
        return "urgent_handler"

    return "normal_handler"


def urgent_handler(state: TaskState) -> dict:
    return {"result": "Urgent task handled"}


def normal_handler(state: TaskState) -> dict:
    return {"result": "Normal task handled"}

llm_builder = StateGraph(TaskState)

llm_builder.add_node("llm_node", llm_node)

llm_builder.add_edge(START, "llm_node")
llm_builder.add_edge("llm_node", END)

llm_graph = llm_builder.compile()


builder = StateGraph(TaskState)

builder.add_node("process_task", process_task)
builder.add_node("urgent_handler", urgent_handler)
builder.add_node("normal_handler", normal_handler)

builder.add_edge(START, "process_task")

builder.add_conditional_edges(
    "process_task",
    route_by_priority,
    {
        "urgent_handler": "urgent_handler",
        "normal_handler": "normal_handler",
    },
)

builder.add_edge("urgent_handler", END)
builder.add_edge("normal_handler", END)

graph = builder.compile()


if __name__ == "__main__":
    output = llm_graph.invoke({
        "task": "Explain an AI agent in two sentences.",
        "result": "",
        "priority": "normal",
        "llm_response": "",
    })

    print(output["llm_response"])