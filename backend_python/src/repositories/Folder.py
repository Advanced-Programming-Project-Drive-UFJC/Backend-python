"""
This module contains the Folder class represent in the database.
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""
import json, os, datetime
import re
from .File import File

class Folder:
    """
    This class represents a folder in the database
    A folder is a dict of dicts
    """
    #TODO : Verify that always exist a data folder in src
    #TODO: for the root folder, must be os.chdir(os.getcwd() + '/data/')
    def __init__(self, name: str) -> None:
        self.name = name
        self.modification_date = self.get_time()
        self.folders = []
        self.files = []
        self.users = {}
        self.address = os.getcwd() +'/' + self.name
        if not os.path.exists(self.address):
            os.mkdir(self.address)
        
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
                list_result.extend(folder.get_folders_folders(list_result))          
        return list_result        
    
    #TODO: On this point, the folder services methods
    
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
        #TODO: Test it
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """
        try:
            folder = self.get_folder_by_name(folder_name)
            self.folders.remove(folder)
            if os.path.exists(folder.get_address()):
                for item in os.listdir(folder.get_address()):
                    item_path = os.path.join(folder.get_address(), item)
                    if os.path.isdir(item_path):
                        sub_folder = folder.get_folder_by_address(item_path)
                        item_path.delete_folder(sub_folder.get_name())
                        os.rmdir(item_path)
                    else:
                        os.remove(item_path)
                os.rmdir(folder.get_address())
                return f"Carpeta {folder.get_address()} y su contenido borrados exitosamente."
            else:
                return "Error: La carpeta no existe en la dirección especificada."
    
        except Exception as e:
            return f"Error: {e}"
    
    def create_folder(self, folder_name: str) -> None:
        #TODO: Test it 
        """
        This method create a folder in the current folder
        Args:
            folderName (str): Name of the folder to be created
        Returns:
            None
        """
        os.chdir(self.get_address())
        new_folder = Folder(folder_name)
        self.folders.append(new_folder)
        
        
        
    
    def delete_file(self, file_name: str) -> None:
        #TODO: Test it
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted
        Returns:
            None
        """

        #self.files.remove(self.get_file_by_name(file_name))
        try:
            file = self.get_file_by_name(file_name)
            if os.path.exists(file.get_address()):
                os.remove(file.get_address())
                return f"Archivo {file.get_address()} borrado exitosamente."
            else:
                return "Error: El archivo no existe en la dirección especificada."
    
        except Exception as e:
            return f"Error: {e}"
    
    def copy_folder(self, address: str) -> None:
        #TODO: test it 
        """
        This method copy a folder from the current folder to another the given 
        memory address
        
        Args:
            folderName (str): Name of the folder to be copied
            address (str): Memory address where the folder will be copied

        Returns:
            None
        """
        try:
            if not os.path.exists(address):
                return "Error: Address given does not exist"
            folder_name = os.path.basename(address)
            new_folder = Folder(folder_name)
            self.folders.append(new_folder)
            for element in os.listdir(address):
                origen_element = os.path.join(address, element)
                destiny_element = os.path.join(new_folder.get_address(), element)
                element.set_address(destiny_element)
                if os.path.isdir(origen_element):
                    self.copy_folder(origen_element)
                else:
                    self.copy_file(origen_element) 
            return f"Carpeta {address} copiada exitosamente a {self.get_address()}"
    
        except Exception as e:
            return f"Error: {e}"

    def copy_file(self, address: str) -> None:
        #TODO: test it 
        """
        This method copy a file from the current folder to another the given
        memory address

        Args:
            fileName (str): Name of the file to be copied
            address (str): Memory address where the file will be copied
        
        Returns:
            None
        """
        try:
            if not os.path.exists(address):
                return "Error: Address given does not exist"
            
            file_name = os.path.basename(address)
            file_name, file_extension = os.path.splitext(file_name)
            file_size = os.path.getsize(address)
            new_file_address = self.get_address() + "/" + file_name + "." + file_extension
            new_file = File(file_name, self.get_time(), file_size, file_extension, new_file_address )
            self.files.append(new_file)

            with open(address, 'rb') as file:
                file = file.read()

            with open(new_file_address, 'wb') as new_file:
                new_file.write(file)

            return f"Archivo copiado exitosamente a {new_file_address}"
        except Exception as e:
            return f"Error: {e}"
    
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
    #TODO: test it 
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
            file_address = self.get_file_by_name(file_name).get_address()
            file_new_address = self.get_file_by_name(new_name).get_address()
            os.rename(file_address, file_new_address)
            self.get_file_by_name(file_name).set_name(new_name)
            
    
    def rename_folder(self, folder_name: str, new_name: str) -> None:
        #TODO: test it 
        """
        This method rename a folder in the current folder
        Args:
            folderName (str): Name of the file to be renamed
            newName (str): New name of the file
        Returns:
            None
        """
        if (self.get_folder_by_name(folder_name) is None):
            print("File not found")
        else:

            folder = self.get_folder_by_name(folder_name)
            folder.set_name(new_name)
            folder_new_address = self.get_folder_by_name(new_name).get_address()
            for file in folder.get_files():
                file.set_address(folder_new_address + file.get_name() + '.' + file.get_extension())
            for sub_folder in folder.get_folders():
                sub_folder.set_address(folder_new_address + sub_folder.get_name())
                sub_folder.rename_folder(sub_folder.get_name(), sub_folder.get_name())

    def add_user(self, user) -> None:
        """
        This method add a user to users list who has access to the folder
        Args:
            user (User): User to be added
        Returns:
            None
        """
        self.users.append(user)

    def delete_user(self, user) -> None:
        """
        This method delete a user from users list who has access to the folder
        Args:
            user (User): User to be deleted
        Returns:
            None
        """
        self.users.remove(user)
    
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
    
    def upload(self, name: str) -> dict:
        """
        This method loads the folder from a json
        Args:
            name (str): The name of the folder
        Returns:
            None
        """
        self.address = os.getcwd() + '/' + name + '.json'
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
                self.users = data['users']
                self.address = data['address']
                return self
        except Exception as e:
            print('File cannot be loaded', e)

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
        self.users = data['users']
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
            print('File cannot be created', e)    