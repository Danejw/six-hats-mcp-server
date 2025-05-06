FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock* /app/
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copy source
COPY . /app/

CMD ["uvicorn", "app.main:mcp_app", "--host", "0.0.0.0", "--port", "8000"]
