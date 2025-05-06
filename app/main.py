from fastapi import FastAPI
from fastmcp import FastMCP
import os
from dotenv import load_dotenv
from .hats import (
    white_hat_agent,
    red_hat_agent,
    black_hat_agent,
    yellow_hat_agent,
    green_hat_agent,
    blue_hat_agent
)

# Load environment variables
load_dotenv()

# Ensure OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY environment variable not set")

# Create FastMCP instance
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

# FastAPI app - this is the app that Uvicorn will run
mcp_app = FastAPI(title="Six Hats MCP API")

# Include the MCP router in the FastAPI app
mcp_app.include_router(prefix="/6hats", tags=["6hats"])

@mcp_app.get("/health")
async def health():
    return {"status": "ok"}

