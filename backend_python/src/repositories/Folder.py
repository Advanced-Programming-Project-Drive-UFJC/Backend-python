"""
This module contains the Folder class represent in the database.
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""
from .File import File
import json

class Folder:
    """
    This class represents a folder in the database
    A folder is a dict of dicts
    """

    def __init__(self, name: str, modification_date: str) -> None:
        
        self.folders = {}
        self.files = {}
        self.users = {}
        self.address = None
        self.data = {'name': name, 'modification_date': modification_date,\
                     'folders': self.folders, 'files': self.files, 'users': self.users}
    
    def __str__(self):
        #TODO : find a way to do not mark error here
        self.data

    def get_data(self, key: str) -> str:
        """
        This method returns the value of the attribute given of the folder
        The folder has the following attributes:
        - name: The name of the folder -> str
        - modification_date: The date of the last modification of the folder -> str
        - address: The memory address of the folder -> str
        Args:
            key (str): The attribute of the folder
        Returns:
            str: The value of the attribute
        """
        return self.data.get(key)

    def get_files_data(self, key: str) -> list:
        """
        This method returns the specific attribute put on the parrameter of the all files
        that the folder has.
        This method do not return the attributes of the files inner the folders.
        Args:
            key (str): The attribute of the files

        Returns:
            dict: The attribute of the files in the folder
        """
        result = {}
        for file in self.data['files']:
            result[self.get_data('name')] = self.data['files'][file].get_data(key)
        return result
    
    def get_folders_data(self, key: str) -> dict:
        """
        This method returns the specific attribute put on the parrameter of the all folders
        that the folder has.
        Args:
            key (str): The attribute of the folders
        Returns:
            dict: The attribute of the folders in the folder
        """
        #TODO: implements a better solution here
        result = {}
        for folder_name in self.data['folders']:
            result[folder_name] = {}
            result[folder_name] = self.data['folders'][folder_name].get_files_data(key)

            print(result[folder_name])
            
            folder = self.data['folders'][folder_name]
            result[folder.get_data('name')] = folder.get_folders_data(key)
            break    
        return result
            
        
            
    
    def add_file(self, file: File) -> None:
        """
        This method adds a file to the folder
        Args:
            file (File): The file to add
        Returns:
            None
        """
        self.data['files'][file.get_data('name')] = file
    
    def add_folder(self, folder ) -> None:
        """
        This method adds a folder to the folder
        Args:
            folder (Folder): The folder to add
        Returns:
            None
        """
        self.data['folders'][folder.get_data('name')] = folder
    
    def create(self):
        """
        This method creates the folder in a json
        Args:
            None
        Returns:
            None
        """
        self.address = 'src/data/' + self.get_data('name') + '.json'
        try:
            with open(self.address, 'w', encoding='utf-8') as file:
                json.dump(self.data, file)
        except Exception as e:
            print('File cannot be created', e)
    
        