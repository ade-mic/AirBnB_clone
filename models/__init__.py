#!/usr/bin/python3
"""Initialize the directory as module """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
