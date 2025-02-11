"""
This file contains services offerd by Folder class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

"""
from abc import ABC, abstractmethod
from fastapi import APIRouter
from typing import Optional
import os
from repositories.Folder import Folder
from repositories.User import User
from repositories.File import File

class IFolder_Services(ABC) :
    """
    This class is an interface that contains the methods that Folder class should implement
    """

    @abstractmethod
    def  upload_data(self, folder : Folder) -> str:
        """
        This method upload a folder to the database
        Args:
            folder: Folder object
        Returns:
            str: message
        """

    @abstractmethod
    def download_data(self, folder_name : str) -> Folder:
        """
        This method download a folder from the database
        Args:
            folder: Folder object
        Returns:
            Folder: Folder object
        """
    @abstractmethod
    def is_loaded(self) -> bool:
        """
        This method check if the folder is loaded
        Returns:
            bool: True if the folder is loaded, False otherwise
        """

    @abstractmethod
    def search_file(self, file_name : str) -> File:
        """
        This method search a file in the folder root
        Args:
            file_name: str
        Returns:
            File: File object
        """

    @abstractmethod
    def search_folder(self, folder_name : str) -> Folder:
        """
        This method search a folder in the folder root
        Args:
            folder_name: str
        Returns:
            Folder: Folder object
        """

    @abstractmethod
    def show_elements(self) -> str:
        """
        This method show the elements in the folder root
        Returns:
            str: message
        """
    
    @abstractmethod
    def show_folder_elements(self, folder_name : str) -> str:
        """
        This method show the elements in a folder
        Args:
            folder_name: str
        Returns:
            str: message
        """
    
    @abstractmethod
    def copy_folder(self, folder_address : str) -> str:
        """
        This method copy a folder
        Args:
            folder_address: str
        Returns:
            str: message
        """

    @abstractmethod
    def copy_file(self, file_address : str) -> str:
        """
        This method copy a file
        Args:
            file_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def move_folder(self, folder_address : str) -> str:
        """
        This method move a folder
        Args:
            folder_address: str
        Returns:
            str: message
        """
    @abstractmethod
    def move_file(self, file_address : str) -> str:
        """
        This method move a file
        Args:
            file_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def create_folder(self, folder_name : str) -> str:
        """
        This method create a folder
        Args:
            folder_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def delete_folder(self, folder_name : str) -> str:
        """
        This method delete a folder
        Args:
            folder_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def delete_file(self, file_name : str) -> str:
        """
        This method delete a file
        Args:
            file_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def rename_folder(self, folder_name : str, new_folder_name : str) -> str:
        """
        This method rename a folder
        Args:
            folder_name: str
            new_folder_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def rename_file(self, file_name : str, new_file_name : str) -> str:
        """
        This method rename a file
        Args:
            file_name: str
            new_file_name: str
        Returns:
            str: message
        """
    @abstractmethod
    def add_user(self, user : User) -> str:
        """
        This method add a user to the folder
        Args:
            user: User object
        Returns:
            str: message
        """
    @abstractmethod
    def delete_user(self, user : User) -> str:
        """
        This method delete a user to the folder
        Args:
            user: User object
        Returns:
            str: message
        """



class Folder_Services:

    
    def __init__(self, folder_name):
        self.folder = self.upload_data(folder_name)


    def upload_data(self, folder_name : str):
        folder = Folder(folder_name)
        return folder.upload(folder_name)

    def is_loaded(self):
        if self.folder is not None:
            return True
        else:
            return False
    
    def search_file(self, file_name):
        if self.is_loaded():
            result_list = self.folder.search_file_by_name(file_name)
            for folder in self.folder.get_folders_folders(None):
                result_list.append(folder.search_file_by_name(file_name))
            return result_list
        else:
            return "ERROR Folder is not loaded"
    
    def search_folder(self, folder_name):
        if self.is_loaded():
            result_list = self.folder.search_folder_by_name(folder_name)
            for folder in self.folder.get_folders_folders(None):
                result_list.append(folder.search_folder_by_name(folder_name))
        else:
            return "ERROR Folder is not loaded"
    
    def show_elements(self):
        if self.is_loaded():
            return self.folder.show_elements()
        else:
            return "ERROR Folder is not loaded"
    
    def show_folder_elements(self, folder_name):
        if self.is_loaded():
            return self.folder.folders[folder_name].show_elements()
        else:
            return "ERROR Folder is not loaded"
    
    def copy_folder(self, folder_address):
        if self.is_loaded():
            self.folder.copy_folder(folder_address)
        else:
            return "ERROR Folder is not loaded"
    
    def copy_file(self, file_address):
        if self.is_loaded():
            self.folder.copy_file(file_address)
        else:
            return "ERROR Folder is not loaded"
    
    def create_folder(self, folder_name):
        if self.is_loaded():
            self.folder.create_folder(folder_name)
        else:
            return "ERROR Folder is not loaded"

    def delete_folder(self, folder_name):
        if self.is_loaded():
            self.folder.delete_folder(folder_name)
        else:
            return "ERROR Folder is not loaded"
    
    def delete_file(self, file_name):
        if self.is_loaded():
            self.folder.delete_file(file_name)
        else:
            return "ERROR Folder is not loaded"
    
    def rename_folder(self, folder_name, new_folder_name):
        if self.is_loaded():
            self.folder.rename_folder(folder_name, new_folder_name)
        else:
            return "ERROR Folder is not loaded"
    
    def rename_file(self, file_name, new_file_name):
        if self.is_loaded():
            self.folder.rename_file(file_name, new_file_name)
        else:
            return "ERROR Folder is not loaded"
    
    def add_user(self, user):
        if self.is_loaded():
            self.folder.add_user(user)
        else:
            return "ERROR Folder is not loaded"
    
    def delete_user(self, user):
        if self.is_loaded():
            self.folder.delete_user(user)
        else:
            return "ERROR Folder is not loaded"

router = APIRouter()

folder_root = None
ROOT_ADDRESS = os.getcwd() + '/data/'
os.chdir(ROOT_ADDRESS)
#TODO: Eliminar al terminar 
folder_root = Folder("folder4")
folder_root.upload("folder4")
if not os.path.exists(ROOT_ADDRESS + "/folder4/"):
    os.mkdir(ROOT_ADDRESS + "/folder4")

def is_loaded():
    if folder_root is not None:
        return True
    else:
        return False

@router.get("/{folder_name}")
def upload_data(folder_name : str):
    global folder_root
    folder_root = Folder(folder_name)
    if not os.path.exists(ROOT_ADDRESS + '/' + folder_name + '/'):
        os.mkdir(ROOT_ADDRESS + '/' + folder_name + '/')
    return folder_root.upload(folder_name)

@router.get("/search_file/{file_name}")
def search_file(file_name : str):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        result_list = folder_root.search_file_by_name(file_name)
        for folder in folder_root.get_folders_folders(None):
            result_list.extend(folder.search_file_by_name(file_name))    
        return list(set(result_list)) 

@router.get("/search_folder/{folder_name}")       
def search_folder(folder_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        result_list = folder_root.search_folder_by_name(folder_name)
        for folder in folder_root.get_folders_folders(None):
            result_list.extend(folder.search_folder_by_name(folder_name))
        return list(set(result_list)) 

@router.get("/show_elements/")
def show_elements():
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root

@router.get("/show_folder_elements/{folder_name}")
def show_folder_elements(folder_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.get_folder_by_name(folder_name).show_elements()

@router.post("/create_folder/{folder_name}")
def create_folder(folder_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.create_folder(folder_name)
    
@router.delete("/delete_folder/{folder_name}")
def delete_folder(folder_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.delete_folder(folder_name)

@router.post("/rename_folder/{new_folder_name}")
def rename_folder(folder_name, new_folder_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.rename_folder(folder_name, new_folder_name)

@router.post("/rename_file/{new_file_name}")
def rename_file(file_name, new_file_name):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.rename_file(file_name, new_file_name)

@router.post("/copy_file/{file}")
def copy_file(file):
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.copy_file(file)
