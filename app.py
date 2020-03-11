from flask import Flask
from config import Configuration

from posts.blueprint import posts

app = Flask(__name__)  # filename
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')
