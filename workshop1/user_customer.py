"""
This module defines the AbstractUser class (abstract base class) and 
the Customer class for managing user details and customer-specific information 
for an arcade machine purchase.

Author: Juan Bedoya <jebedoyal@udistrital.edu.co>

ArcadeMachine - bl is free software: you can redistribute it and/or modify it under the terms 
of the GNU General Public License as published by the Free Software Foundation, either version 3 
of the License, or (at your option) any later version.

ArcadeMachine - bl is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ArcadeMachine - bl. 
If not, see <https://www.gnu.org/licenses/>.

==================================================
LICENSE - GPL-3.0
"""

from abc import ABC, abstractmethod
from typing import List

class AbstractUser(ABC):
    """
    This abstract class represents a user with a username.
    """

    def __init__(self, username: str):
        """Initialize an AbstractUser with a username.

        Args:
            username (str): The username of the user.
        """
        self.username = username

    @abstractmethod
    def get_user_info(self) -> List[str]:
        """Abstract method to get user information.

        Returns:
            List[str]: User information as a list of strings.
        """


class Customer(AbstractUser):
    """
    This class represents a customer with additional information such as address.
    """

    def __init__(self, username: str, address: str):
        """Initialize a Customer with a username and address.

        Args:
            username (str): The username of the customer.
            address (str): The address of the customer.
        """
        super().__init__(username)
        self.__address = address

    def get_user_info(self) -> List[str]:
        """Return customer information including username and address.

        Returns:
            List[str]: A list containing the username and address of the customer.
        """
        return [self.username, self.__address]
