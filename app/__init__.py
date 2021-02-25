from flask import Flask
from .config import Config
USERNAME = 'admin'
PASSWORD = 'password123'
SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config.from_object(__name__)
from app import views
