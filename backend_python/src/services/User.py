"""
This module contains services related to user management
Juan Nicolás Diaz Salamanca <jndiazs@udistrital.edu.co>
"""
#TODO Implements these services in java backend
from abc import ABC, abstractmethod

class IUser(ABC):
    """
    This class is an interface that contains
    the methods (services) to implemented to
    user
    """

    @abstractmethod
    @property
    def create_user(self, user_name: str, password: str) -> None:
        """
        This method creates a new user in the system
        Args:
            user_name (str): Name of the user
            password (str): Password of the user
        Returns:
            None
        """

    @abstractmethod
    @property
    def delete_user(self, user_name: str) -> None:
        """
        This method delete a user in the system
        Args:
            user_name (str): Name of the user to be deleted
        Returns:
            None
        """

    @abstractmethod
    @property
    def update_user(self, user_name: str, password: str) -> None:
        """
        This method update the password of a user
        Args:
            user_name (str): Name of the user
            password (str): New password
        Returns:
            None
        """

    @abstractmethod
    @property
    def show_users(self) -> list:
        """
        This method return a list of users in the system
        Args:
            None
        Returns:
            list: List of users
        """

    @abstractmethod
    @property
    def show_user(self, user_name: str) -> dict:
        """
        This method return the information of a user
        Args:
            user_name (str): Name of the user
        Returns:
            dict: Information of the user
        """

    @abstractmethod
    @property
    def login(self, user_name: str, password: str) -> bool:
        """
        This method validate the credentials of a user
        Args:
            user_name (str): Name of the user
            password (str): Password of the user
        Returns:
            bool: True if the credentials are correct, False otherwise
        """

    @abstractmethod
    @property
    def logout(self, user_name: str) -> None:
        """
        This method close the session of a user
        Args:
            user_name (str): Name of the user
        Returns:
            None
        """
        