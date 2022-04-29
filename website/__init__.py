from flask import Flask

from os import path

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "S"

    # Import Blueprint files
    from .views import views
    from .auth import auth

    #Register Blueprint file with flask application. url_prefix = all of the urls stored in the blueprint file how do I access them? 
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app 