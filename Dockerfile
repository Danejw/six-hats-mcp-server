FROM python:3.10-slim
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . /app/


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
