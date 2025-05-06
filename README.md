# Six Hats MCP

A full implementation of Edward de Bono's Six Thinking Hats using FastMCP and the OpenAI Agents SDK.

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
