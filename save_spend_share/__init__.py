from flask import Flask

app = Flask(__name__)
from save_spend_share import routes
