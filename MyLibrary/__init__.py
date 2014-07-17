#    Test __init__.py
#

import os
from _keywords import keywords

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(THIS_DIR, 'version.py'))
#execfile(join(dirname(__file__), 'version.py'))

__version__ = VERSION


class MyLibrary(keywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
