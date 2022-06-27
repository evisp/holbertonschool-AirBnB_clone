"""
module for init FileStorage
To create a unique FileStorage instance for the application improting
FileStorage, creating the variable storage (as instance of FileStorage)
and callign reaload() method on this variable
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
