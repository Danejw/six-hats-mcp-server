#!/bin/bash
# Six Hats MCP Server Starter Script

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "No .env file found. Creating one now..."
    
    # Prompt for OpenAI API key
    echo -n "Enter your OpenAI API key: "
    read apikey
    
    # Create .env file
    echo "OPENAI_API_KEY=$apikey" > .env
    
    echo ".env file created successfully."
else
    echo ".env file already exists."
fi

# Start the application
echo "Starting Six Hats MCP server..."
docker-compose up --build 