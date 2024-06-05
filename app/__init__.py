# this file makes the holding directory of this file a 'package'

from app.routes import home, dashboard # imports home module (/app/routes/home.py), renamed inside routes init py
# import the Flask() function
from flask import Flask

# use the def keyword to define a create_app() function
def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/') # declared new app variable -- app should serve any static resources from the root directory and not from the default /static directory
  app.url_map.strict_slashes = False # configuring that trailing slashes are optional (/dash and /dash/ load same route)
  app.config.from_mapping( 
    SECRET_KEY='super_secret_key' # app will use key 'super_secret_key' when creating server-side sessions
  )

  @app.route('/hello') # the decorator '@app.route('hello')' turns the hello() func into a route
  def hello():
    return 'hello world' # the return becomes the route's response
  
  # register routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)

  return app