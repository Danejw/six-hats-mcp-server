from fastapi import APIRouter, FastAPI
from fastmcp import FastMCP
from agents import Runner
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

# FastAPI app - this is the app that Uvicorn will run
app = FastAPI(title="Six Hats MCP API")

router = APIRouter()

# Include the MCP router in the FastAPI app
app.include_router(router, prefix="/6hats", tags=["6hats"])


@mcp.tool(name="white", description="Objective facts & data")
@app.post("/white")
async def white(query: str) -> str:
    response = await Runner.run(white_hat_agent, query)
    return response.final_output


@mcp.tool(name="red", description="Emotions & intuitions")
@app.post("/red")
async def red(query: str) -> str:
    response = await Runner.run(red_hat_agent, query)
    return response.final_output

@mcp.tool(name="black", description="Risks & critiques")
@app.post("/black")
async def black(query: str) -> str:
    response = await Runner.run(black_hat_agent, query)
    return response.final_output

@mcp.tool(name="yellow", description="Benefits & optimism")
@app.post("/yellow")
async def yellow(query: str) -> str:
    response = await Runner.run(yellow_hat_agent, query)
    return response.final_output

@mcp.tool(name="green", description="Creativity & ideas")
@app.post("/green")
async def green(query: str) -> str:
    response = await Runner.run(green_hat_agent, query)
    return response.final_output

@mcp.tool(name="blue", description="Manager & orchestration")
@app.post("/blue")
async def blue(prompt: str) -> str:
    response = await Runner.run(blue_hat_agent, prompt)
    return response.final_output


@app.get("/health")
async def health():
    return {"status": "ok"}

