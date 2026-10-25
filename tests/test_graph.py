from src.agent.graph import graph
from unittest.mock import patch
from src.agent.graph import graph, llm_graph


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

def test_llm_node_stores_model_response():
    expected_response = "An AI agent can use tools."

    with patch(
        "src.agent.graph.generate_response",
        return_value=expected_response,
    ) as mock_llm:
        result = llm_graph.invoke({
            "task": "Explain an AI agent",
            "result": "",
            "priority": "normal",
            "llm_response": "",
        })

    assert result["llm_response"] == expected_response
    mock_llm.assert_called_once_with("Explain an AI agent")