#!/usr/bin/env python3
"""
Environment setup helper for Six Hats MCP.
Creates a .env file with necessary environment variables.
"""
import os

def setup_env():
    """Create a .env file with necessary environment variables."""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    
    # Check if .env already exists
    if os.path.exists(env_path):
        overwrite = input(".env file already exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("Setup cancelled.")
            return
    
    # Get OpenAI API key
    openai_key = input("Enter your OpenAI API key: ").strip()
    
    # Write to .env file
    with open(env_path, 'w') as f:
        f.write(f"OPENAI_API_KEY={openai_key}\n")
    
    print(f".env file created at {env_path}")
    print("Environment setup complete!")

if __name__ == "__main__":
    setup_env() 