# Six Hats MCP

A full implementation of Edward de Bono's Six Thinking Hats using FastMCP and the OpenAI Agents SDK.

## Setup

### Environment Variables

This project requires an OpenAI API key. You can set it up with:

```bash
# Run the setup script
python setup_env.py

# Or manually create a .env file with:
# OPENAI_API_KEY=your_openai_api_key_here
```

## Run Locally

```bash
docker-compose up --build
```

Visit http://localhost:8000 to access the MCP endpoints.

## Tools

- **white**: Objective facts & data
- **red**: Emotions & intuitions
- **black**: Risks & critiques
- **yellow**: Benefits & optimism
- **green**: Creativity & ideas
- **blue**: Manager & orchestration

## Testing

```bash
poetry run pytest --cov=app
```
