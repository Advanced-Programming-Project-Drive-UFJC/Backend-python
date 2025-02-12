"""
This file contains services offerd by Folder class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

"""
import os
from fastapi import APIRouter
from repositories.Folder import Folder

router = APIRouter()
folder_root = None
ROOT_ADDRESS = os.getcwd() + '/data/'
os.chdir(ROOT_ADDRESS)

def is_loaded():
    """
    This method check if the folder is loaded
    Returns:
        bool: True if the folder is loaded, False otherwise
        """
    if folder_root is not None:
        return True
    else:
        return False

@router.get("/{folder_name}")
def upload_data(folder_name : str) :
    """
    This method upload a folder to the database
    Args:
        folder_nae: str
    Returns:
        Folder : Folder object
    """
    global folder_root
    folder_root = Folder(folder_name)
    if not os.path.exists(ROOT_ADDRESS + '/' + folder_name + '/'):
        os.mkdir(ROOT_ADDRESS + '/' + folder_name + '/')
    return folder_root.upload(folder_name)

@router.get("/search_file/{file_name}")
def search_file(file_name : str):
    """
    This method search files which match with the name given 
    Args:
        file_name: str
    Returns:
        Files: File object list
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        result_list = folder_root.search_file_by_name(file_name)
        for folder in folder_root.get_folders_folders(None):
            result_list.extend(folder.search_file_by_name(file_name))    
        return list(set(result_list)) 

@router.get("/search_folder/{folder_name}")       
def search_folder(folder_name):
    """
    This method search a folder  which match with the name given 
    Args:
        folder_name: str
    Returns:
        Folder: Folder object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        result_list = folder_root.search_folder_by_name(folder_name)
        for folder in folder_root.get_folders_folders(None):
            result_list.extend(folder.search_folder_by_name(folder_name))
        return list(set(result_list)) 

@router.get("/show_elements/")
def show_elements():
    """
    This method show the elements in the folder root
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root

@router.get("/show_folder_elements/{folder_name}")
def show_folder_elements(folder_name):
    """
    This method show the elements in a folder
    Args:
        folder_name: str
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.get_folder_by_name(folder_name).show_elements()

@router.post("/create_folder/{folder_name}")
def create_folder(folder_name):
    """
    This method create a folder
    Args:
        folder_name: str
    Returns:
        new_folder: Folder object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.create_folder(folder_name)
    
@router.delete("/delete_folder/{folder_name}")
def delete_folder(folder_name):
    """
    This method delete a folder
    Args:
        folder_name: str
    Returns:
        Folder_root : Folder object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.delete_folder(folder_name)

@router.post("/rename_folder/{new_folder_name}")
def rename_folder(folder_name, new_folder_name):
    """
    This method rename a folder
    Args:
        folder_name: str
        new_folder_name: str
    Returns:
        Folder_root : Folder object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.rename_folder(folder_name, new_folder_name)

@router.post("/rename_file/{new_file_name}")
def rename_file(file_name, new_file_name) :
    """
    This method rename a file
    Args:
        file_name: str
        new_file_name: str
    Returns:
        File : File object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.rename_file(file_name, new_file_name)

@router.post("/copy_file/{file}")
def copy_file(file, base_dir=os.path.expanduser("~")):
    """
    This method copy the file of the adress given
    As the argument is the file name and it's extension, the method
    automatically search the file in user root directory, to change this 
    it's required to change base_dir parameter
    Args:
        file_name: str
        <optional> base_dir: str
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.copy_file(file, base_dir)

@router.delete("/delete_file/{file}")
def delete_file(file) -> dict:
    """
    This method delete a file inner the folder root
    Args:
        file_name: str
    Returns:
        folder_root: Folder object
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.delete_file(file)

@router.post("/move_file/{file}")
def move_file(file_name: str, folder_name : str) : 
    """
    This method move a file to a folder
    Args:
        file_name: str
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.move_file(file_name, folder_name)
    
@router.post("/move_folder/{folder_name}")
def move_folder(folder_to_move_name: str, folder_to_reach_name: str) :
    """
    This method move a folder to a folder
    Args:
        folder_name: str
        new_folder_name: str
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.move_folder(folder_to_move_name , folder_to_reach_name )

@router.post("/save/")
def save():
    """
    This method save the folder root modifications
    Args:
        None
    Returns:
        str: message
    """
    if not is_loaded():
        return "ERROR Folder is not loaded"
    else:
        return folder_root.save(ROOT_ADDRESS)
