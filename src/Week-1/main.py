
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(override=True)

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send prompt
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Hello! Introduce yourself."
)

# Print response
print(response.text)
