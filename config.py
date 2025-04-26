import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set. Please set it in your .env file.") 