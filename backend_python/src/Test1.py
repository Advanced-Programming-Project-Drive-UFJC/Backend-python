from repositories.Folder import Folder
import os
root_address = os.getcwd() + '/data/'
folder1 = Folder("Folder1")
folder1.create_folder("Folder2")
folder1.get_folder_by_name("Folder2").create_folder("Folder3")
folder1.save(root_address)
folder1.rename_folder("Folder2", "Folder_lol")
folder1.save(root_address)
