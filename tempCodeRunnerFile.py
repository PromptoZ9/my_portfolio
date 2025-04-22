from app import app
from dotenv import load_dotenv
import os

load_dotenv()
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
EMAIL =  os.getenv ("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")
print(FLASK_SECRET_KEY, EMAIL, EMAIL_PASS)
exit()