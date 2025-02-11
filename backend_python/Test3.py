"""
This module contains a test to verify all services in the FolderService class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

Folder1 contains 3 files
Folder2 contains 2 files and Folder1
Folder3 contains Folder2
Folder4 is empty
"""

from src.repositories.File import File
from src.repositories.Folder import Folder
from src.Services.Folder import FolderService

file1 = File("file1", "2021-01-01", "1MB", "txt", "0x0001")
file2 = File("file2", "2021-01-02", "2MB", "txt", "0x0002")
file3 = File("file3", "2021-01-03", "3MB", "txt", "0x0003")
file4 = File("file4", "2021-01-04", "4MB", "txt", "0x0004")
file5 = File("file5", "2021-01-05", "5MB", "txt", "0x0005")

folder1 = Folder("folder1")
folder1.add_file(file1)
folder1.add_file(file2)
folder1.add_file(file3)

folder2 = Folder("folder2")
folder2.add_file(file4)
folder2.add_file(file5)
folder2.add_folder(folder1)

folder3 = Folder("folder3")
folder3.add_folder(folder2)

folder4 = Folder("folder4")

folder_service1 = FolderService(folder1)
folder_service2 = FolderService(folder2)
folder_service3 = FolderService(folder3)
folder_service4 = FolderService(folder4)

# Test 1: show elements
# Test passed on 2 feb
print("Test 1: show elements")
for i in folder_service1.show_elements():
    print(i)
for i in folder_service2.show_elements():
    print(i)
for i in folder_service3.show_elements():
    print(i)
for i in folder_service4.show_elements():
    print(i)

# Test 2: sort elements
# Test passed on 2 feb
print("Test 2: sort elements")
print(folder_service1.sort_elements())
print(folder_service2.sort_elements())
print(folder_service3.sort_elements()) 
print(folder_service4.sort_elements())

#TODO Test 5: copy folder
#TODO Test 6: copy file
#TODO Test 7: move folder
#TODO Test 8: move file

# Test 9: search folder by name
# Test passed on 2 feb
print("Test 9: search folder by name")
print(folder_service1.search_folder_by_name("folder"))
print(folder_service2.search_folder_by_name("folder"))
print(folder_service3.search_folder_by_name("folder"))
print(folder_service4.search_folder_by_name("folder"))

# Test 10: search file by name
# Test passed on 2 feb
print("Test 10: search folder by name")
print(folder_service1.search_file_by_name("file"))
print(folder_service2.search_file_by_name("file"))
print(folder_service3.search_file_by_name("file"))
print(folder_service4.search_file_by_name("file"))

# Test 11: rename folder
# Test passed on 2 feb
print("Test 11: rename folder")
print(folder_service3.search_folder_by_name("folder"))
folder_service3.rename_folder("folder1", "folder1(1)")
print(folder_service3.search_folder_by_name("folder"))

# Test 3: delete folder
# Test passed on 2 feb
print("Test 3: delete folder")
folder_service1.delete_folder("folder")
folder_service2.delete_folder("folder1")
folder_service3.delete_folder("folder2")
folder_service4.delete_folder("folder3")

# Test 4: delete file
# Test passed on 2 feb
print("Test 4: delete file")
folder_service1.delete_file("file1")
folder_service2.delete_file("file4")
folder_service3.delete_file("file3")
folder_service4.delete_file("file4")

