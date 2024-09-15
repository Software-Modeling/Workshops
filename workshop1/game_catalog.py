"""
This module defines the Game and Catalog classes for managing video game details 
and filtering games by category in an arcade machine.

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

from typing import List

class Game:
    """
    This class represents a video game with its details such as name, code, and genre.
    """

    def __init__(self, code: str, name: str, genre: str, price: float):
        """Initialize a Game with code, name, genre, and price.

        Args:
            code (str): The code of the game.
            name (str): The name of the game.
            genre (str): The genre of the game.
            price (float): The price of the game.
        """
        self.code = code
        self.name = name
        self.genre = genre
        self.price = price

    def get_game_details(self) -> List[str]:
        """Return the details of the game as a list of strings.

        Returns:
            List[str]: A list containing the name, code, and genre of the game.
        """
        return [self.code, self.name, self.genre, f"${self.price:.2f}"]


class Catalog:
    """
    This class represents a catalog of games available for arcade machines.
    """

    def __init__(self):
        """Initialize a Catalog with an empty list of games."""
        self.games = []
    def add_game(self, game: Game):
        """Add a game to the catalog.

        Args:
            game (Game): The game to add.
        """
        self.games.append(game)

    def get_games(self) -> List[Game]:
        """Get the list of games in the catalog.

        Returns:
            List[Game]: The list of games.
        """
        return self.games

    def filter_games_by_category(self, category: str) -> List[Game]:
        """Filter games by category.

        Args:
            category (str): The category to filter by.

        Returns:
            List[Game]: A list of games that match the category.
        """
        return [game for game in self.games if game.genre.lower() == category.lower()]
