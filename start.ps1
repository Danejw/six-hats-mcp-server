# Six Hats MCP Server Starter Script

# Check if .env file exists
if (-not (Test-Path -Path ".env")) {
    Write-Host "No .env file found. Creating one now..."
    
    # Prompt for OpenAI API key
    $apiKey = Read-Host -Prompt "Enter your OpenAI API key"
    
    # Create .env file
    "OPENAI_API_KEY=$apiKey" | Out-File -FilePath ".env"
    
    Write-Host ".env file created successfully."
} else {
    Write-Host ".env file already exists."
}

# Start the application
Write-Host "Starting Six Hats MCP server..."
docker-compose up --build 