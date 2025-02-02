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
        
        self.data = {'name': name, 'modification_date': modification_date, 'size': size ,\
                      'extension': extension, 'address': address}
    
    def __str__(self):
        return f"{self.data.get('size')} {self.data.get('modification_date')} {self.data.get('name')}.{self.data.get('extension')}"

    def get_data(self, key) -> str:
        """
        This method returns the value of the attribute given of the file
        The file has the following attributes:
        - name: The name of the file -> str
        - modification_date: The date of the last modification of the file -> str
        - size: The size of the file -> str
        - extension: The extension of the file -> str
        - address: The memory address of the file -> str
        Args:
            key (str): The attribute of the file
        Returns:
            str: The value of the attribute
        """
        return self.data.get(key)
    
    def change_data(self, key: str, value: str) -> None:
        """
        This method change one of the attributes of the file
        The file has the following attributes:
        - name: The name of the file -> str
        - modification_date: The date of the last modification of the file -> str
        - size: The size of the file -> str
        - extension: The extension of the file -> str
        - address: The memory address of the file -> str
        Args:
            key (str): New name of the file
            value (str): New value of the attribute
        Returns:
            None
        """
        self.data[key] = value
        
    
    def move(self, new_address: str) -> None:
        """
        TODO: implement logic low level to move a file. impelemented in services module
        This method move the file to another memory address
        Args:
            newAddress (str): New memory address of the file
        Returns:
            None
        """
  
    
