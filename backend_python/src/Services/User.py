"""
This module contains services related to user management
Juan Nicolás Diaz Salamanca <jndiazs@udistrital.edu.co>
"""
#TODO: test it
from pydantic import BaseModel
import os
from .Folder import router
from repositories.Folder import Folder as FolderRepository


@router.post("/receive-user_root")
async def receive_json(username: str):
    folder_name = username + "_root"
    new_folder = FolderRepository(folder_name)
    new_folder.save(os.getcwd() + '/data/')
    return f"Folder {folder_name} created at {os.getcwd() + '/data/'}"

@router.delete("/delete-user_root")
async def delete_json(username: str):
    os.rmdir(os.getcwd() + '/data/' + username + '_root')
    os.remove(os.getcwd() + '/data/' + username + '_root.json')
    return f"Folder {username}_root deleted"

