"""
This file contains services offerd by Folder class
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>

"""
from abc import ABC, abstractmethod
import re, subprocess
from ..repositories.Folder import Folder
from ..repositories.User import User
from ..repositories.File import File
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
        #TODO: Test the subprocces run
        """
        This method delete a folder in the current folder
        Args:
            folderName (str): Name of the folder to be deleted
        Returns:
            None
        """
        try:
            self.folder.folders.remove(self.folder.get_folder_by_name(folder_name))
            subprocess.run(["rm", "-r", self.folder.get_address() + "/" + folder_name], check=True)
            print("Folder deleted " + folder_name)
        except Exception as e:
            print("Folder not found", e)
    
    def create_folder(self, folder_name: str) -> None:
        #TODO: Test it
        """
        This method create a folder in the current folder
        Args:
            folderName (str): Name of the folder to be created
        Returns:
            None
        """
        new_folder = Folder(folder_name)
        self.folder.folders.append(new_folder)
        subprocess.run(["mkdir", self.folder.get_address() + "/" + folder_name], check=True)
        print("Folder created " + folder_name)
    
    def delete_file(self, file_name: str) -> None:
        #TODO: Test the subprocces run
        """
        This method delete a file in the current folder
        Args:
            fileName (str): Name of the file to be deleted
        Returns:
            None
        """
        try:
            self.folder.files.remove(self.folder.get_file_by_name(file_name))
            subprocess.run(["rm", self.folder.get_address() + "/" + file_name], check=True)
            print("File deleted " + file_name)
        except Exception as e:
            print("File not found", e)
    
    def copy_folder(self, folder_name: str, address: str) -> None:
        #TODO: test it and don't forget size attribute
        """
        This method copy a folder from the current folder to another the given 
        memory address
        
        Args:
            folderName (str): Name of the folder to be copied
            address (str): Memory address where the folder will be copied

        Returns:
            None
        """
        new_folder = Folder(folder_name)
        self.folder.folders.append(new_folder)
        subprocess.run(['cp', '-r', address, self.folder.get_address()], check=True)
        file_names = subprocess.run(['cd', self.folder.get_address(), '&&', 'ls'],capture_output=True, text=True ,check=True)
        regex= r'\.[a-zA-Z0-9]+$'
        for element_name in file_names.stdout.split("\n"):
            if bool(re.search(regex, element_name)):
                new_folder.files.append(File(element_name, self.folder.get_time(), "0", "txt", self.folder.get_address() + "/" + element_name))
            else:
                new_folder.folders.append(Folder(element_name))
                self.copy_folder(element_name, self.folder.get_address() + "/" + element_name)


    def copy_file(self, file_name: str, file_extension: str, file_size: str, address: str) -> None:
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
        
        new_file_address = self.folder.get_address() + "/" + file_name + "." + file_extension
        new_file = File(file_name, self.folder.get_time(), file_size, file_extension, new_file_address )
        self.folder.files.append(new_file)
        subprocess.run(["cp ",address,self.folder.get_address()], check=True)

    def move_folder(self, folder_name: str, address: str) -> None:
        #TODO: test it and dont' forget about size attribute
        """
        This method move a folder from the current folder to another the given 
        memory address

        Args: 
            folderName (str): Name of the folder to be moved
            address (str): Memory address where the folder will be moved

        Returns:
            None
        """
        new_folder = Folder(folder_name)
        self.folder.folders.append(new_folder)
        subprocess.run(['mv', '-r', address, self.folder.get_address()], check=True)
        file_names = subprocess.run(['cd', self.folder.get_address(), '&&', 'ls'],capture_output=True, text=True ,check=True)
        regex= r'\.[a-zA-Z0-9]+$'
        for element_name in file_names.stdout.split("\n"):
            if bool(re.search(regex, element_name)):
                new_folder.files.append(File(element_name, self.folder.get_time(), "0", "txt", self.folder.get_address() + "/" + element_name))
            else:
                new_folder.folders.append(Folder(element_name))
                self.move_folder(element_name, self.folder.get_address() + "/" + element_name)

    def move_file(self, file_name: str, file_extension: str, file_size: str, address: str):
        #TODO: test it
        """
        This method move a file from the current folder to another the given
        """
        new_file_address = self.folder.get_address() + "/" + file_name + "." + file_extension
        new_file = File(file_name, self.folder.get_time(), file_size, file_extension, new_file_address)
        self.folder.files.append(new_file)
        subprocess.run(["mv",address,self.folder.get_address()], check=True)

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
        for folder in self.folder.get_folders_folders(None):
            if not isinstance(folder, list) \
                and pattern.match(folder.get_name()):
                name_list.append(folder.get_name())
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
        for file in self.folder.files:
            if pattern.match(file.get_name()):
                name_list.append(file.get_name())
        for file in self.folder.get_folders_files(None):
            if not isinstance(file, list) \
                and pattern.match(file.get_name()):
                name_list.append(file.get_name())
        return name_list

    def rename_file(self, file_name: str, new_name: str) -> None:
    #TODO: test it with the os feature
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
            file_address = self.folder.get_file_by_name(file_name).get_address()
            self.folder.get_file_by_name(file_name).set_name(new_name)
            file_new_address = self.folder.get_file_by_name(new_name).get_address()
            subprocess.run(['mv', file_address, file_new_address], check=True)
    
    def rename_folder(self, folder_name: str, new_name: str) -> None:
        #TODO: test it with the os feature
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
            folder_address = self.folder.get_folder_by_name(folder_name).get_address()
            self.folder.get_folder_by_name(folder_name).set_name(new_name)
            folder_new_address = self.folder.get_folder_by_name(new_name).get_address()
            subprocess.run(['mv', '-r', folder_address, folder_new_address], check=True)


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