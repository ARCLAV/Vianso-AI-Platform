from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / "myproject" / ".env"

print("ENV =", env_path)

load_dotenv(env_path)

print("KEY =", os.getenv("GROQ_API_KEY_3"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY_3")
)

models = client.models.list()

for model in models.data:
    print(model.id)