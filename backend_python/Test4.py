"""
This module contains tests for os functions
"""
from src.repositories.Folder import Folder
from src.repositories.File import File
from src.services.Folder import FolderService 
import os 


# importing datetime module for now()
import datetime

# using now() to get current time

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Printing value of now.
print(current_time)

