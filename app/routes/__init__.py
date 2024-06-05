# this file makes the holding directory of this file a 'package'

from .home import bp as home # .home syntax directs the program to find the module named 'home' in the current directory -- Next we're importing the bp object, but we're renaming it home for practicality's sake
from .dashboard import bp as dashboard