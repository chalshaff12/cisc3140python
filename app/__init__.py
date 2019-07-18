from flask import Flask 
from config import Config

#create app object in Flask class
app = Flask(__name__)
#apply configurations 
app.config.from_object(Config)

from app import routes