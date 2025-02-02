"""
This module contains a test to verify:
    1. file and a folder can be created
    2. file and folder can be added to a folder
    3. file inner a folder can show its data
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""

from src.repositories.File import File
from src.repositories.Folder import Folder

file1 = File('file1', '2021-08-09', '1MB', 'txt', '0x123')
file2 = File('file2', '2021-08-09', '1MB', 'txt', '0x123')
file3 = File('file3', '2021-08-09', '1MB', 'txt', '0x123')
file4 = File('file4', '2021-08-09', '1MB', 'txt', '0x123')
folder1 = Folder('folder1', '2021-08-09')
folder2 = Folder('folder2', '2025-01-01')
folder3 = Folder('folder3', '2024-01-01')
folder4 = Folder('folder4', '2024-01-01')
folder5 = Folder('folder5', '2024-01-01')

folder1.add_file(file1)
folder2.add_file(file2)
folder3.add_file(file3)
folder4.add_file(file4)

folder2.add_folder(folder1)
folder3.add_folder(folder2)
folder4.add_folder(folder3)
folder5.add_folder(folder4)

folder5.get_folders_data('name')
folder1.create()
"""
print(folder1.get_files_data('name'))
print(folder1.get_files_data('size'))
print(folder1.get_files_data('modification_date'))
print(folder1.get_files_data('extension'))
print(folder1.get_files_data('address'))
folder2.add_folder(folder1)
print(folder2.data)
print(folder2.get_folders_data('name'))
print(folder2.get_data('name'))
"""
