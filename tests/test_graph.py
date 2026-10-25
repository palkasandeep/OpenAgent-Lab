from src.agent.graph import graph


def test_graph_routes_normal_task():
    result = graph.invoke({
        "task": "Learn LangGraph",
        "result": "Pending",
        "priority": "normal",
    })

    assert result["priority"] == "normal"
    assert result["result"] == "Normal task handled"


def test_graph_routes_urgent_task():
    result = graph.invoke({
        "task": "URGENT: Fix login",
        "result": "Pending",
        "priority": "normal",
    })

    assert result["priority"] == "urgent"
    assert result["result"] == "Urgent task handled"