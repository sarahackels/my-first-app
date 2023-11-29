
# this is the "web_app/__init__.py" file...
## this is a python convention that is an entry point to a given folder that has some python code in it
## in order to stay organized and when we build on top of some basic fucntionality it will help us to set it up this way
## flask is telling us about a way of keeping organized
## implementing an organized modular structure for our web app


# this is the "web_app/__init__.py" file...
import os

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.unemployment_routes import unemployment_routes
from web_app.routes.stock_routes import stocks_routes
#from web_app.routes.stocks_routes import stocks_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    app.register_blueprint(unemployment_routes)
    app.register_blueprint(stocks_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)