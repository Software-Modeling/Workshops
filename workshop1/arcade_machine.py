"""
This module defines the ArcadeMachine class for managing arcade machine properties 
and functionalities such as selecting materials and managing the list of games.

Author: Juan Bedoya <jebedoyal@udistrital.edu.co>

This file is part of ArcadeMachine - bl.

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

class AbstractMachine(ABC):
    """
    This abstract class represents an arcade machine with a material type.
    """

    def __init__(self, material: str):
        """Initialize an AbstractMachine with a material.

        Args:
            material (str): The material of the arcade machine (wood, aluminum, carbon fiber).
        """
        self._material = material

    @abstractmethod
    def select_material(self, material: str):
        """Select the material of the arcade machine.

        Args:
            material (str): The material type (wood, aluminum, carbon fiber).
        """

    def get_material(self):
        """Return the current material of the arcade machine.

        Returns:
            str: The material of the arcade machine.

        Raises:
            ValueError: If the material is not one of the allowed values.
        """
        if self._material not in ['wood', 'aluminum', 'carbon fiber']:
            raise ValueError("Invalid material. Allowed values are: wood, aluminum, carbon fiber.")
        return self._material


# =============== Concrete Version of a Machine =============== #

class ArcadeMachine(AbstractMachine):
    """
    This class represents a concrete arcade machine with properties such as material type
    and a list of games.
    """

    def __init__(self, material: str):
        """Initialize an ArcadeMachine with a material and an empty game list.

        Args:
            material (str): The material of the arcade machine (wood, aluminum, carbon fiber).
        """
        super().__init__(material)

    def select_material(self, material: str):
        """Set the material type of the arcade machine.

        Args:
            material (str): The new material type (wood, aluminum, carbon fiber).
        """
        self._material = material
