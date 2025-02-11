"""
This module contains a test to verify:
    1. file can be renamed via FolderService
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""

from src.repositories.File import File
from src.repositories.Folder import Folder
from src.Services.Folder import FolderService

file1 = File("file1", "2021-01-01", "1MB", "txt", "0x0001")
file2 = File("file2", "2021-01-02", "2MB", "txt", "0x0002")
file3 = File("file3", "2021-01-03", "3MB", "txt", "0x0003")
file4 = File("file4", "2021-01-04", "4MB", "txt", "0x0004")
file5 = File("file5", "2021-01-05", "5MB", "txt", "0x0005")

folder1 = Folder("folder1", "2021-01-01")
folder1.add_file(file1)
folder1.add_file(file2)
folder1.add_file(file3)

folder2 = Folder("folder2", "2021-01-02")
folder2.add_file(file4)
folder2.add_file(file5)
folder2.add_folder(folder1)

folder3 = Folder("folder3", "2021-01-03")
folder3.add_folder(folder2)

folder4 = Folder("folder4", "2021-01-04")
folder4.add_folder(folder3)

folder_service = FolderService(folder3)

print(folder4.get_file_by_name("file5").get_size())
folder_service.rename_file("file5", "file5(1)")
print(folder4.get_file_by_name("file5(1)").get_size())



