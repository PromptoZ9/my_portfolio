from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from flask_mail import Mail

load_dotenv()
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL =  os.getenv ("EMAIL")
PASSWORD = os.getenv("PASSWORD")
app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = EMAIL
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = EMAIL

mail = Mail(app)

def render(template: str,**kwargs):
    kwargs["path"] = request.path
    return render_template(template, **kwargs)

from . import routes

