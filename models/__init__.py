#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""

from os import getenv
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()