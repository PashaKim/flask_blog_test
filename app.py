from flask import Flask
from config import Configuration

app = Flask(__name__)  # filename
app.config.from_object(Configuration)
