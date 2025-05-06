FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . /app/

# Set environment variable with a default value that will be overridden by .env
ENV OPENAI_API_KEY=""

CMD ["uvicorn", "app.main:mcp_app", "--host", "0.0.0.0", "--port", "8000"]
