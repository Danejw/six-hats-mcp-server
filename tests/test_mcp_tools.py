import pytest
from fastapi.testclient import TestClient
import app.hats as hats
from app.main import mcp_app

client = TestClient(mcp_app)

@pytest.fixture(autouse=True)
def stub_agent_runs(monkeypatch):
    # Stub each agent's run method to avoid real OpenAI calls
    for agent in [
        hats.white_hat_agent,
        hats.red_hat_agent,
        hats.black_hat_agent,
        hats.yellow_hat_agent,
        hats.green_hat_agent,
        hats.blue_hat_agent
    ]:
        monkeypatch.setattr(
            agent,
            "run",
            lambda query, *args, agent=agent, **kwargs: f"{agent.name} processed: {query}"
        )

@pytest.mark.parametrize("tool,query", [
    ("white", "List known facts about Knolia."),
    ("red", "How do you feel about this feature?"),
    ("black", "What could go wrong?"),
    ("yellow", "What are the benefits?"),
    ("green", "Suggest creative improvements."),
    ("blue", "Coordinate a Six Hats session on Knolia feature.")
])
def test_tool_endpoints(tool, query):
    response = client.post(f"/tools/{tool}", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    # Verify stubbed output matches expected format
    agent = getattr(hats, f"{tool}_hat_agent" if tool != "blue" else "blue_hat_agent")
    expected = f"{agent.name} processed: {query}"
    assert data.get("response") == expected


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
