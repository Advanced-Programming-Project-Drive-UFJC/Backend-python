"""
This module contains the User class that represents a user in the system.
Author: Juan Nicolás Diaz Salamanca <jndiaz@udistrital.edu.co>
"""

class User: 
    """
    This class represents a user in the system data
    """

    def __init__(self, user_name: str, password: str):
        
        self.user_name = user_name
        self.__password = password

