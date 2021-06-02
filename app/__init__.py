from flask import Flask,render_template
from flask import json
from flask import request
from app.webhook.routes import webhook

def create_app(test_config=None):
    app = Flask(__name__)

    #registering the blueprints
    app.register_blueprint(webhook ,url_prefix="/webhook")


    # hello route
    @app.route('/')
    def hello():
        return "check output on localhost:port/webhook/"

    return app

