"""
This module contains the File class that represents a file in the database.
A file is a dict so its requires: 
    - name (str): The name of the file
    - modification_date (str): The date of the last modification of the file
    - size (str): The size of the file
    - extension (str): The extension of the file
    - address (str): The memory address of the file
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""

class File:
    """
    This class represents a file in the database
    A file is a dict 
        Args:
            name (str): The name of the file
            modification_date (str): The date of the last modification of the file
            size (str): The size of the file
            extension (str): The extension of the file
            address (str): The memory address of the file
        Returns:
            None
    """

    def __init__(self, name: str, modification_date: str, size: str, extension: str, address: str) -> None:
        
        self.name = name
        self.modification_date = modification_date
        self.size = size
        self.extension = extension
        self.address = address
    
    def __str__(self):
        return f"{self.size} {self.modification_date} {self.name}.{self.extension}"

    def get_name(self) -> str:
        """
        This method returns the name of the file
        Args:
            None
        Returns:
            str: The name of the file
        """
        return self.name
    
    def get_modification_date(self) -> str:
        """
        This method returns the modification date of the file
        Args:
            None
        Returns:
            str: The modification date of the file
        """
        return self.modification_date

    def get_size(self) -> str:
        """
        This method returns the size of the file
        Args:
            None
        Returns:
            str: The size of the file
        """
        return self.size
    
    def get_extension(self) -> str:
        """
        This method returns the extension of the file
        Args:
            None
        Returns:
            str: The extension of the file
        """
        return self.extension
    
    def get_address(self) -> str:
        """
        This method returns the memory address of the file
        Args:
            None
        Returns:
            str: The memory address of the file
        """
        return self.address
    
    def set_name(self, new_name: str) -> None:
        """
        This method sets the name of the file
        Args:
            newName (str): The new name of the file
        Returns:
            None
        """
        self.name = new_name
    
    def set_modification_date(self, new_modification_date: str) -> None:
        """
        This method sets the modification date of the file
        Args:
            newModificationDate (str): The new modification date of the file
        Returns:
            None
        """
        self.modification_date = new_modification_date
    
    def convert_dict(self) -> dict:
        """
        This method converts the file to a dict
        Args:
            None
        Returns:
            dict: The file as a dict
        """
        return {
            "name": self.name,
            "modification_date": self.modification_date,
            "size": self.size,
            "extension": self.extension,
            "address": self.address
        }
        
    
    def move(self, new_address: str) -> None:
        """
        TODO: implement logic low level to move a file. impelemented in services module
        This method move the file to another memory address
        Args:
            newAddress (str): New memory address of the file
        Returns:
            None
        """
  
    
