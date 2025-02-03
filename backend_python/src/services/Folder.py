"""
This file contains services offerd by Folder class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

"""
from abc import ABC, abstractmethod
import re
from ..repositories.Folder import Folder
from ..repositories.User import User

class IFolder(ABC) :
    """
    This class is an interface that contains the methods that Folder class must implement
    """

    @abstractmethod
    def show_elements(self) -> list:
        """
        This method return a list of files and folders in the current folder

        Args:
            None
        
        Returns:
            list: List of files and folders in the current folder
        
        """

    @abstractmethod
    def sort_elements(self) -> list:
        """
        This method sort the folders and files in the current folder
        
        Args:
            None

        Returns:
            list: List of files and folders sorted
        """

    @abstractmethod
    def delete_folder(self, folder_name: str) -> None :
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """

    @abstractmethod
    
    def delete_file(self, file_name: str) -> None:
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted

        Returns:
            None
        """
        
    @abstractmethod
    
    def copy_folder(self, folder_name: str, address: str) -> None:
        """
        This method copy a folder from the current folder to another the given 
        memory address
        
        Args:
            folderName (str): Name of the folder to be copied
            address (str): Memory address where the folder will be copied

        Returns:
            None
        """

    @abstractmethod
    
    def copy_file(self, file_name: str, address: str) -> None:
        """
        This method copy a file from the current folder to another the given
        memory address

        Args:
            fileName (str): Name of the file to be copied
            address (str): Memory address where the file will be copied
        
        Returns:
            None
        """
       
    @abstractmethod
    
    def search_folder_by_name(self, folder_name: str) -> list:
        """
        This method search by name a folder in the current folder 
        Args:
            folderName (str): Name of the folder to be searched
        Returns:
            list: List of folders with the given name
        """

    @abstractmethod
    
    def search_file_by_name(self, file_name: str) -> list:
        """
        This method search by name a file in the current folder
        Args:
            fileName (str): Name of the file to be searched
        Returns:
            list: List of files with the given name
        """

    @abstractmethod
    
    def move_folder(self, folder_name: str, address: str) -> None:
        """
        This method move a folder from the current folder to another the given 
        memory address

        Args: 
            folderName (str): Name of the folder to be moved
            address (str): Memory address where the folder will be moved

        Returns:
            None
        """

    @abstractmethod
    
    def move_file(self, file_name: str, address: str):
        """
        This method move a file from the current folder to another the given
        """
    @abstractmethod
    
    def rename_file(self, file_name: str, new_name: str) -> None:
        """
        This method rename a file in the current folder
        Args:
            fileName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """
    @abstractmethod
    def rename_folder(self, folder_name: str, new_name: str) -> None:
        """
        This method rename a folder in the current folder
        Args:
            folderName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """

    @abstractmethod
    
    def add_user(self, user: User) -> None:
        """
        This method add a user to users list who has access to the folder
        Args:
            user (User): User to be added
        Returns:
            None
        """
    @abstractmethod
    def delete_user(self, user: User) -> None:
        """
        This method delete a user from users list who has access to the folder
        Args:
            user (User): User to be deleted
        Returns:
            None
        """
class FolderService(IFolder):
    """
    This class contains the methods that Folder class must implement
    """
    
    def __init__(self, folder: Folder) -> None:

        self.folder = folder
        super().__init__()

    
    def show_elements(self) -> list:
        """
        This method return a list of files and folders in the current folder

        Args:
            None
        
        Returns:
            list: List of files and folders in the current folder
        
        """
        return self.folder.get_files() + self.folder.get_folders()
    
    def sort_elements(self) -> list:

        """
        This method sort the folders and files in the current folder
        
        Args:
            None

        Returns:
            list: List of files and folders sorted
        """
        result =  self.folder.get_files_names()
        if len(self.folder.get_folders()) != 0:
            for folder in self.folder.get_folders():
                result.append(folder.get_name())
        result.sort(reverse=True)
        return result
    
    def delete_folder(self, folder_name: str) -> None :
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """
        try:
            self.folder.folders.remove(self.folder.get_folder_by_name(folder_name))
            print("Folder deleted " + folder_name)
        except Exception as e:
            print("Folder not found", e)
    
    def delete_file(self, file_name: str) -> None:
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted
        Returns:
            None
        """
        try:
            self.folder.files.remove(self.folder.get_file_by_name(file_name))
            print("File deleted " + file_name)
        except Exception as e:
            print("File not found", e)
    
    def copy_folder(self, folder_name: str, address: str) -> None:
        #TODO: implements with os library
        """
        This method copy a folder from the current folder to another the given 
        memory address
        
        Args:
            folderName (str): Name of the folder to be copied
            address (str): Memory address where the folder will be copied

        Returns:
            None
        """
        pass

    def copy_file(self, file_name: str, address: str) -> None:
        #TODO: implements with os library
        """
        This method copy a file from the current folder to another the given
        memory address

        Args:
            fileName (str): Name of the file to be copied
            address (str): Memory address where the file will be copied
        
        Returns:
            None
        """
        pass

    def move_folder(self, folder_name: str, address: str) -> None:
        #TODO: implements with os library
        """
        This method move a folder from the current folder to another the given 
        memory address

        Args: 
            folderName (str): Name of the folder to be moved
            address (str): Memory address where the folder will be moved

        Returns:
            None
        """

    def move_file(self, file_name: str, address: str):
        #TODO: implements with os library
        """
        This method move a file from the current folder to another the given
        """

    def search_folder_by_name(self, folder_name: str) -> list:
        #TODO: tests it
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
        for folder in self.folder.get_folders_folders(None):
            if not isinstance(folder, list) \
                and pattern.match(folder.get_name()):
                name_list.append(folder.get_name())
        return name_list
    
    def search_file_by_name(self, file_name: str) -> list:
        #TODO: tests it
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
        for file in self.folder.files:
            if pattern.match(file.get_name()):
                name_list.append(file.get_name())
        for file in self.folder.get_folders_files(None):
            if not isinstance(file, list) \
                and pattern.match(file.get_name()):
                name_list.append(file.get_name())
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
        if (self.folder.get_file_by_name(file_name) is None):
            print("File not found")
        else:
            self.folder.get_file_by_name(file_name).set_name(new_name)
    
    def rename_folder(self, folder_name: str, new_name: str) -> None:
        """
        This method rename a folder in the current folder
        Args:
            folderName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """
        if (self.folder.get_folder_by_name(folder_name) is None):
            print("File not found")
        else:
            self.folder.get_folder_by_name(folder_name).set_name(new_name)


    def add_user(self, user: User) -> None:
        """
        This method add a user to users list who has access to the folder
        Args:
            user (User): User to be added
        Returns:
            None
        """
        self.folder.users.append(user)

    def delete_user(self, user: User) -> None:
        """
        This method delete a user from users list who has access to the folder
        Args:
            user (User): User to be deleted
        Returns:
            None
        """
        self.folder.users.remove(user)

        
        
        
    
    