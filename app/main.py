from fastapi import FastAPI
from fastmcp import FastMCP
from .hats import (
    white_hat_agent,
    red_hat_agent,
    black_hat_agent,
    yellow_hat_agent,
    green_hat_agent,
    blue_hat_agent
)

mcp = FastMCP(name="SixHatsMCP")

@mcp.tool(name="white", description="Objective facts & data")
async def white(query: str) -> str:
    return white_hat_agent.run(query)

@mcp.tool(name="red", description="Emotions & intuitions")
async def red(query: str) -> str:
    return red_hat_agent.run(query)

@mcp.tool(name="black", description="Risks & critiques")
async def black(query: str) -> str:
    return black_hat_agent.run(query)

@mcp.tool(name="yellow", description="Benefits & optimism")
async def yellow(query: str) -> str:
    return yellow_hat_agent.run(query)

@mcp.tool(name="green", description="Creativity & ideas")
async def green(query: str) -> str:
    return green_hat_agent.run(query)

@mcp.tool(name="blue", description="Manager & orchestration")
async def blue(prompt: str) -> str:
    return blue_hat_agent.run(
        prompt,
        tools=["white", "red", "black", "yellow", "green"]
    )

# FastAPI app
mcp_app = FastAPI()

mcp_app.include_router(mcp.router)

@mcp_app.get("/health")
async def health():
    return {"status": "ok"} 