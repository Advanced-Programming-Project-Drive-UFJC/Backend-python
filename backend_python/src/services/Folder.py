"""
This file contains services offerd by Folder class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

"""
from abc import ABC, abstractmethod
from ..repositories.Folder import Folder

class IFolder(ABC) :
    """
    This class is an interface that contains the methods that Folder class must implement
    """

    @abstractmethod
    @property
    def show_elements(self) -> list:
        """
        This method return a list of files and folders in the current folder

        Args:
            None
        
        Returns:
            list: List of files and folders in the current folder
        
        """

    @abstractmethod
    @property
    def sort_elements(self) -> list:
        """
        This method sort the folders and files in the current folder
        
        Args:
            None

        Returns:
            list: List of files and folders sorted
        """

    @abstractmethod
    @property
    def delete_folder(self, folder_name: str) -> None :
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """

    @abstractmethod
    @property
    def delete_file(self, file_name: str) -> None:
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted

        Returns:
            None
        """
        
    @abstractmethod
    @property
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
    @property
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
    @property
    def search_folder_by_name(self, folder_name: str) -> list:
        """
        This method search by name a folder in the current folder 
        Args:
            folderName (str): Name of the folder to be searched
        Returns:
            list: List of folders with the given name
        """

    @abstractmethod
    @property
    def search_file(self, file_name: str) -> list:
        """
        This method search by name a file in the current folder
        Args:
            fileName (str): Name of the file to be searched
        Returns:
            list: List of files with the given name
        """

    @abstractmethod
    @property
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
    @property
    def move_file(self, file_name: str, address: str):
        """
        This method move a file from the current folder to another the given
        """
    @abstractmethod
    @property
    def add_user(self, user: User) -> None:
        """
        This method add a user to users list who has access to the folder
        Args:
            user (User): User to be added
        Returns:
            None
        """
    @abstractmethod
    @property
    def delete_user(self, user: User) -> None:
        """
        This method delete a user from users list who has access to the folder
        Args:
            user (User): User to be deleted
        Returns:
            None
        """

class Folder(IFolder):
    """
    This class contains the methods that Folder class must implement
    """
    
    def __init__(self, folder_name: str, creation_date: str, address: str) -> None:

        self.folder_name = folder_name
        self.creation_date = creation_date
        self.address = address
        self.users_list = []
        self.folder_elements = {}
        self.file_elements = {}
        super().__init__()
    
    @property
    def show_elements(self) -> list:
        """
        This method return a list of files and folders in the current folder

        Args:
            None
        
        Returns:
            list: List of files and folders in the current folder
        
        """
        for file in self.file_elements:
            print(file)
        
        
    
    