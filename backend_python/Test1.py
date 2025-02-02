"""
This module contains a test to verify:
    1. file and a folder can be created
    2. folder can have files 
    3. folder with files can be converted to a json 
    4. folder can have folders and be converted to a json
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""

from src.repositories.File import File
from src.repositories.Folder import Folder

file1 = File("file1", "2021-01-01", "1MB", "txt", "0x0001")
file2 = File("file2", "2021-01-02", "2MB", "txt", "0x0002")
file3 = File("file3", "2021-01-03", "3MB", "txt", "0x0003")

folder1 = Folder("folder1", "2021-01-01")
folder2 = Folder("folder2", "2021-01-02")
folder3 = Folder("folder3", "2021-01-03")

folder1.add_file(file1)
folder1.add_file(file2)
folder1.add_file(file3)
folder2.add_folder(folder1)
folder3.add_folder(folder2)



