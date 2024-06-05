# this is a standalone file called a 'module' -- this one specifically is a module that belongs to the routes package

from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')
# Blueprint() lets us consolidate routes into a single `bp` object that the parent app can register later -- This coresponds to using the `Router` middleware of Express.js

@bp.route('/') # @bp.route() decorator added before the function to turn it into a route (remember that the function return = the response)
def index():
  return render_template('homepage.html') # render_template function used to respond with a template instead of a string

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>') # this route is using a parameter '<id>', to capture the value, its included as a function parameter as well (single(id))
def single(id):
  return render_template('single-post.html')

# you can import any variables or functions defined by Python modules into other modules -- the @bp.route() decoratior makes all other functions already attatched to the bp object, so we only care about bp, which has the bp object and all 3 route functions all available for importing
