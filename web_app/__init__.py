
# this is the "web_app/__init__.py" file...
## this is a python convention that is an entry point to a given folder that has some python code in it
## in order to stay organized and when we build on top of some basic fucntionality it will help us to set it up this way
## flask is telling us about a way of keeping organized
## implementing an organized modular structure for our web app


from flask import Flask

from web_app.routes.home_routes import home_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)