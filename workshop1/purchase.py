"""
This module defines the Purchase class for managing the checkout process and 
generating receipts in an arcade machine purchase system.

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
import json
from datetime import datetime
from typing import List

class Purchase:
    """
    This class represents a purchase transaction for an arcade machine.
    """

    def __init__(self, purchase_date: datetime, total_amount: float):
        """Initialize a Purchase with a date and total amount.

        Args:
            purchase_date (datetime): The date of the purchase.
            total_amount (float): The total amount of the purchase.
        """
        self._purchase_date = purchase_date
        self._total_amount = total_amount

    def finalize_purchase(self):
        """Finalize the purchase process.

        This method is a placeholder for any actions needed to complete the purchase.
        """
        print("Purchase finalized.")

    def generate_receipt(self) -> str:
        """Generate a receipt for the purchase.

        Returns:
            str: A receipt string with the purchase date and total amount.
        """
        receipt = (
            f"Receipt:\n"
            f"Purchase Date: {self._purchase_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Total Amount: ${self._total_amount:.2f}\n"
        )
        return receipt

    def calculate_total_amount(self, arcade_machine_cost: float, game_codes: List[str]) -> float:
        """Calculate the total amount for the purchase.

        Args:
            arcade_machine_cost (float): The cost of the arcade machine.
            game_codes (List[str]): The list of selected game codes.

        Returns:
            float: The total amount of the purchase.
        """
        with open("data.json", "r", encoding='utf-8') as file:
            data = json.load(file)
        game_prices = {game['code']: game['price'] for game in data.get('games', [])}
        total_amount = arcade_machine_cost + sum(game_prices.get(code, 0) for code in game_codes)
        return total_amount
