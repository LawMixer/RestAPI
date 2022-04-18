from flask import flask 
from firebase_admin import creditials, initlize_app

# grab stuff from service accounts 
cred = creditials.Certification(".json") #file for permissions
default_app = initlize_app(cred)

def create_app():
    app = flask(__name__)
    app.config["SECRET_KEY"] = "ss"

    from .userAPI import userAPI

    app.register_blueprint(userAPI, url_prefix="/user")