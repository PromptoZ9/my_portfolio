from dotenv import load_dotenv
import os

load_dotenv()

print("EMAIL:", os.getenv("EMAIL"))
print("PASSWORD:", os.getenv("PASSWORD"))
print("SECRET_KEY:", os.getenv("SECRET_KEY"))