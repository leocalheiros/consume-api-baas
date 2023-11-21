import awsgi
from flask import Flask
from src.main.routes import account_blueprint
from src.main.routes import payments_blueprint
from src.main.routes import balance_blueprint
from src.main.routes import type_blueprint

app = Flask(__name__)
app.register_blueprint(account_blueprint)
app.register_blueprint(payments_blueprint)
app.register_blueprint(balance_blueprint)
app.register_blueprint(type_blueprint)


def lambda_handler(event, context):
    return awsgi.response(app, event, context)
