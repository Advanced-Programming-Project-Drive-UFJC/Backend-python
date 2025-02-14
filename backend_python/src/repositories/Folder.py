"""
This module contains the Folder class represent in the database.
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""
import json
import os
import datetime
import re
import shutil
from .File import File

class Folder:
    """
    This class represents a folder in the database
    A folder is a dict of dicts
    """
    #TODO : Verify that always exist a data folder in src

    def __init__(self, name: str) -> None:
        self.name = name
        self.modification_date = self.get_time()
        self.folders = []
        self.files = []
        self.address = os.getcwd() +'/' + self.name
        
    def __str__(self):
        
        return f"{self.modification_date} {self.name} "
    
    def get_time(self) -> str:
        """
        This method returns the year/month/day/hour/minute/seconds
         exactly of the momment is called 
        Args:
            None
        Returns:
            str: The time on a string format
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_name(self) -> str:
        """
        This method returns the name of the folder
        Args:
            None
        Returns:
            str: The name of the folder
        """
        return self.name
    
    def set_name(self, name: str) -> None:
        """
        This method sets the name of the folder
        Args:
            name (str): The name of the folder
        Returns:
            None
        """
        self.name = name
        self.modification_date = self.get_time()
        self.address = os.getcwd() +'/' + self.name + '/'

    def get_modification_date(self) -> str:
        """
        This method returns the modification date of the folder
        Args:
            None
        Returns:
            str: The modification date of the folder
        """
        return self.modification_date
    
    def set_modification_date(self, modification_date: str) -> None:
        """
        This method sets the modification date of the folder
        Args:
            modification_date (str): The modification date of the folder
        Returns:
            None
        """
        self.modification_date = modification_date
    
    def get_address(self) -> str:
        """
        This method returns the address of the folder
        Args:
            None
        Returns:
            str: The address of the folder
        """
        return self.address
    
    def set_address(self, address: str) -> None:
        """
        This method sets the address of the folder
        Args:
            address (str): The address of the folder
        Returns:
            None
        """
        self.address = address
    
    def get_files(self) -> list:
        """
        This method returns the files of the folder
        Args:
            None
        Returns:
            list: The files of the folder
        """
        return self.files

    def get_folders(self) -> list:
        """
        This method returns the folders of the folder
        Args:
            None
        Returns:
            list: The folders of the folder
        """
        return self.folders

    def get_files_names(self) -> list:
        """
        This method returns the names of the files of the folder
        Args:
            None
        Returns:
            list: The names of the files of the folder
        """
        return [file.get_name() for file in self.files]
    
    def get_files_modification_date(self) -> list:
        """
        This method returns the modification date of the files of the folder
        Args:
            None
        Returns:
            list: The modification dates of the files of the folder
        """
        return [file.get_modification_date() for file in self.files]
    
    def set_files_modification_date(self) -> None:
        """
        This method sets the modification date of the files of the folder
        Args:
            None
        Returns:
            None
        """
        for file in self.files:
            file.set_modification_date(self.get_time())
    
    def set_files_addresses(self) -> None:
        """
        This method sets the addresses of the files of the folder
        Args:
            None
        Returns:
            None
        """
        for file in self.files:
            file.set_address(self.address + file.get_name() + '.' + file.get_extension())
    
    def get_file_by_name(self, name: str) -> File:
        """
        This method returns a file by its name
        Args:
            name (str): The name of the file
        Returns:
            File: The file
        """
        result = None
        for file in self.files:
            if file.get_name() == name:
                return file
            
        for file in self.get_folders_files(None):
            if not isinstance(file, list) \
                and file.get_name() == name:
                return file
       
        return result
    
    def get_folder_by_name(self, name: str) :
        """
        This method returns a folder by its name
        Args:
            name (str): The name of the folder
        Returns:
            Folder: The folder
        """
        result = None
        for folder in self.folders:
            if folder.get_name() == name:
                return folder
    
        for folder in self.get_folders_folders(None):
            if not isinstance(folder, list) \
                and folder.get_name() == name:
                return folder
        return result

    def get_folder_by_address(self, address: str) :
        """
        This method returns a folder by its address
        Args:
            address (str): The address of the folder
        Returns:
            Folder: The folder
        """
        result = None
        for folder in self.folders:
            if folder.get_address() == address:
                return folder
        for folder in self.get_folders_folders(None):
            if not isinstance(folder, list) \
                and folder.get_address() == address:
                return folder
        return result
    
    def get_folders_files(self, list_result) -> list:
        """
        This methods returns a list of file list from the folders
        inners it. Each file list owner to a folder
        Args:
            None
        Returns:
            File lists
        """
        if list_result is None:
            list_result = []
        for folder in self.get_folders():
            for file in folder.get_files():
                list_result.append(file)
            if len(folder.get_folders()) != 0:
                list_result.append(folder.get_folders_files(list_result))
        return list_result
    
    def get_folders_folders(self, list_result) -> list:
        """
        This methods returns a list of folders list from the folders
        inners it. Each folder list owner to a folder
        Args:
            None
        Returns:
            Folders lists
        """
        if list_result is None:
            list_result = []
        for folder in self.get_folders():
            list_result.append(folder)    
            if len(folder.get_folders()) != 0:
                list_result.extend(folder.get_folders_folders(list_result))          
        return list_result        
    
    def show_elements(self) -> list:
        """
        This method return a list of files and folders in the current folder

        Args:
            None
        
        Returns:
            list: List of files and folders in the current folder
        
        """
        return self.get_files() + self.get_folders()

    def delete_folder(self, folder_name: str) -> None :
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """
 
        folder_to_delete = self.get_folder_by_name(folder_name)
        for folder in self.folders:
            if folder == folder_to_delete:
                self.folders.remove(folder)
                break
            if folder.get_folders() != []:
                folder.delete_folder(folder_name)
        return self
    
    def create_folder(self, folder_name: str) -> None:
        """
        This method create a folder in the current folder
        Args:
            folderName (str): Name of the folder to be created
        Returns:
            None
        """
        new_folder = Folder(folder_name)
        address = os.path.splitext(self.get_address())[0]
        new_folder.set_address(address + '/' + folder_name + '/')
        self.folders.append(new_folder)
        return new_folder
        
    def delete_file(self, file_name: str): 
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted
        Returns:
            None
        """
        try:
            file = self.get_file_by_name(file_name)
            if os.path.exists(file.get_address()):
                os.remove(file.get_address())
            for file in self.files:
                if file.get_name() == file_name:
                    self.files.remove(file)
                    break
            for folder in self.folders:
                if folder.get_files() != [] or folder.get_folders() != []:
                    folder.delete_file(file_name)
            return self
    
        except Exception as e:
            return f"Error: {e}"

    def copy_file(self, file, root) -> None:
        """
        This method copy a file from the current folder to another the given
        memory address

        Args:
            file : File object

        Returns:
            None
        """
        new_file_address = f"{root}/{self.name}/{file.filename}" 
        with open(new_file_address, "wb") as new_file:
            shutil.copyfileobj(file.file, new_file)
        file_name = os.path.basename(new_file_address)
        file_name, file_extension = os.path.splitext(new_file_address)
        file_size = os.path.getsize(new_file_address)
        new_address =  os.path.splitext(new_file_address)[0]
        new_element = File(file_name, self.get_time(), file_size, file_extension, new_address)
        self.files.append(new_element)
        return self
    
    def move_file(self, file_name: str, folder_name: str) :
        """
        This method move a file from the current folder to another the given
        memory address
        Args:
            file_name (str): Name of the file to be moved
            address (str): Memory address where the file will be moved
        Returns:
            Folder_root : Folder object
        """
        file = self.get_file_by_name(file_name)
        folder_to_move = self.get_folder_by_name(folder_name)
        if file is None or folder_to_move is None:
            return "File not found"
        else:
            self.delete_file(file_name)
            folder_to_move.get_files().append(file)
            return self
    
    def move_folder(self, folder_name: str, folder_destination: str) :
        """
        This method move a folder from the current folder to another the given
        memory address
        Args:
            folder_name (str): Name of the folder to be moved
            address (str): Memory address where the folder will be moved
        Returns:
            Folder_root : Folder object
        """
        folder_to_move = self.get_folder_by_name(folder_name)
        folder_to_reach = self.get_folder_by_name(folder_destination)
        if folder_to_move  is None or folder_to_reach is None:
            return "Folder not found"
        else:
            self.delete_folder(folder_name)
            folder_to_reach.get_folders().append(folder_to_move)
            return self

    def search_folder_by_name(self, folder_name: str) -> list:
        """
        This method search folders names in the current folder
        that coincides with the given name, using a regular expression
        which allow coincidences in any part of the string given
        Args:
            folderName (str): Name of the folder to be searched
        Returns:
            list: List of folders that are related to the given name
        """
        name_list = []
        pattern = ".*" + folder_name + ".*"
        pattern = re.compile(pattern, re.IGNORECASE)
        for folder in self.get_folders_folders(None):
            if not isinstance(folder, list) \
                and pattern.match(folder.get_name()):
                name_list.append(folder)
        return name_list
    
    def search_file_by_name(self, file_name: str) -> list:
        """
        This method search by name a file in the current folder
        Args:
            fileName (str): Name of the file to be searched
        Returns:
            list: List of files with the given name
        """
        name_list = []
        pattern = ".*" + file_name + ".*"
        pattern = re.compile(pattern, re.IGNORECASE)
        for file in self.files:
            if pattern.match(file.get_name()):
                name_list.append(file)
        for file in self.get_folders_files(None):
            if not isinstance(file, list) \
                and pattern.match(file.get_name()):
                name_list.append(file)
        return name_list

    def rename_file(self, file_name: str, new_name: str) -> None:
        """
        This method rename a file in the current folder
        Args:
            fileName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """
        if (self.get_file_by_name(file_name) is None):
            return "File not found"
        else:
            file = self.get_file_by_name(file_name)
            file.set_name(new_name)
            file.set_modification_date(self.get_time())
            
    
    def rename_folder(self, folder_name: str, new_name: str) -> None:
        """
        This method rename a folder in the current folder
        Args:
            folderName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """
        if (self.get_folder_by_name(folder_name) is None):
            return"Folder not found"
        else:

            folder = self.get_folder_by_name(folder_name)
            folder.set_name(new_name)
            folder_new_address = self.get_folder_by_name(new_name).get_address()
            for file in folder.get_files():
                file.set_address(folder_new_address + file.get_name() + '.' + file.get_extension())
            for sub_folder in folder.get_folders():
                sub_folder.set_address(folder_new_address + sub_folder.get_name())
                sub_folder.rename_folder(sub_folder.get_name(), sub_folder.get_name())  
    
    def convert_dict(self) -> dict:
        """
        This method returns the folder as a dict
        Args:
            None
        Returns:
            dict: The folder as a dict
        """
        return {
            "name": self.name,
            "modification_date": self.modification_date,
            "folders": [folder.convert_dict() for folder in self.folders],
            "files": [file.convert_dict() for file in self.files],
            "address": self.address
        }
    
    def upload(self, name: str) -> dict:
        """
        This method loads the folder from a json
        Args:
            name (str): The name of the folder
        Returns:
            None
        """
        self.address = os.getcwd() + '/' + name + '.json'
        self.address = os.path.abspath(self.address)
        try:
            with open(self.address, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.name = data['name']
                self.modification_date = data['modification_date']
                for file in data['files']:
                    objetct_file = File(file['name'], file['modification_date'], file['size'],\
                                  file['extension'], file['address'])
                    self.files.append(objetct_file)
                for folder in data['folders']:
                    object_folder = Folder(folder['name'])
                    object_folder.dict_to_folder(folder)
                    self.folders.append(object_folder)
                self.address = self.address
                return self
        except Exception as e:
            return f"File cannot be loaded', {e}"

    def dict_to_folder(self, data: dict) -> None:
        """
        This method converts a dict to a folder
        Args:
            data (dict): The dict to be converted
        Returns:
            None
        """
        self.name = data['name']
        self.modification_date = data['modification_date']
        for folder in data['folders']:
            object_folder = Folder(folder['name'])
            object_folder.dict_to_folder(folder)
            self.folders.append(object_folder)
        for file in data['files']:
            object_file = File(file['name'], file['modification_date'], file['size'],\
                                  file['extension'], file['address'])
            self.files.append(object_file)
        self.address = data['address']

    def save(self, address: str) -> None:
        """
        This method creates the folder in a json
        Args:
            None
        Returns:
            None
        """
        self.set_address(address + self.name + '.json')
        try:
            with open(self.address, 'w', encoding='utf-8') as file:
                json.dump(self.convert_dict(), file, indent=4)
        except Exception as e:
            return f"File cannot be created', {e}"   