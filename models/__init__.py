#!/usr/bin/python3
"""Initialize the directory as module """
from models.engine.filestorage import FileStorage
storage = FileStorage("file.json")
storage.reload()
