import awsgi
from flask import Flask
from src.main.routes import account_blueprint

app = Flask(__name__)
app.register_blueprint(account_blueprint)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
