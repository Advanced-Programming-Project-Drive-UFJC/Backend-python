"""
This module contains the Folder class represent in the database.
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""
import json, os, datetime
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
        self.users = {}
        self.address = os.getcwd() +'/src/data/' + self.name 
    #TODO: Don´t forget about self.users
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

    #TODO: implement getters as paramaters of a super function calle get_files_data

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
    
    def get_folders_files(self, list_result) -> list:
        """
        This methods returns a list of file list from the folders
        inners it. Each file list owner to a folder
        Args:
            None
        Returns:
            File lists
        """
        #TODO implement a better solution here and repetar logic at the others
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
        #TODO implement a better solution here and repetar logic at the others
        if list_result is None:
            list_result = []
        for folder in self.get_folders():
            list_result.append(folder)    
            if len(folder.get_folders()) != 0:
                list_result.append(folder.get_folders_folders(list_result))          
        return list_result        
    
    def add_file(self, file: File) -> None:
        """
        This method adds a file to the folder
        Args:
            file (File): The file to add
        Returns:
            None
        """
        self.files.append(file)

    
    def add_folder(self, folder ) -> None:
        """
        This method adds a folder to the folder
        Args:
            folder (Folder): The folder to add
        Returns:
            None
        """
        self.folders.append(folder)
    
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
            "users": self.users,
            "address": self.address
        }
    
    def load(self, name: str) -> None:
        """
        This method loads the folder from a json
        Args:
            name (str): The name of the folder
        Returns:
            None
        """
        self.address = 'src/data/' + name + '.json'
        try:
            with open(self.address, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.name = data['name']
                self.modification_date = data['modification_date']
                for file in data['files']:
                    objetct_file = File(file['name'], file['modification_date'], file['size'],\
                                  file['extension'], file['address'])
                    self.files.append(objetct_file)
                for index_folder in range(0, len(data['folders'])):
                    object_folder = Folder(data['folders'][index_folder]['name'])
                    for index_file in range(0, len(data['folders'][index_folder]['files'])):
                        object_file = File(data['folders'][index_folder]['files'][index_file]['name'], \
                                           data['folders'][index_folder]['files'][index_file]['modification_date'],\
                                           data['folders'][index_folder]['files'][index_file]['size'],\
                                           data['folders'][index_folder]['files'][index_file]['extension'],\
                                           data['folders'][index_folder]['files'][index_file]['address'])
                        object_folder.add_file(object_file)
                    self.folders.append(object_folder)
                self.users = data['users']
                self.address = data['address']
        except Exception as e:
            print('File cannot be loaded', e)

    def save(self):
        """
        This method creates the folder in a json
        Args:
            None
        Returns:
            None
        """
        self.set_address(os.getcwd() +'/src/data/' + self.name + '.json')
        try:
            with open(self.address, 'w', encoding='utf-8') as file:
                json.dump(self.convert_dict(), file, indent=4)
        except Exception as e:
            print('File cannot be created', e)
    
    
        