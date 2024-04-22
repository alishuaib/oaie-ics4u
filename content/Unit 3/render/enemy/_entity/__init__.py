"""
Dynamically import all classes from files in this directory
Allows usage in the form of:
    from render.enemy import entity
    obj = entity.Boss()

Instead of:
    from render.enemy import entity
    obj = entity.boss.Boss()
Or manually importing each class to __init__.py
"""

import os
import importlib
import inspect

__globals = globals()

for file in os.listdir(os.path.dirname(__file__)):
    mod_name = file[:-3]   # strip .py at the end
    if (mod_name.startswith("__")): continue
    module = importlib.import_module('.' + mod_name, package=__name__)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            globals()[name] = obj