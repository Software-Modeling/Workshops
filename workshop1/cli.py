"""
This module provides a command-line interface for the arcade machine purchase system,
allowing users to interact with arcade machines, games, and the purchase process.

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
from arcade_machine import ArcadeMachine
from game_catalog import Catalog
from user_customer import Customer
from purchase import Purchase
from game_catalog import Game

def load_data():
    """Load the initial data from a JSON file."""
    try:
        with open("data.json", "r", encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Data file not found. Please ensure 'data.json' is present.")
        return None, None
    return data.get("arcade_machine_cost", 0), data.get("games", [])

def main():
    machine_cost, initial_games = load_data()
    if machine_cost is None:
        return

    catalog = Catalog()
    for game_data in initial_games:
        game = Game(code=game_data["code"], name=game_data["name"], genre=game_data["genre"], price=game_data["price"])
        catalog.add_game(game)

    print("Welcome to the Arcade Machine Store!")

    username = input("Enter your username: ")
    address = input("Enter your address: ")
    customer = Customer(username=username, address=address)

    print("\nAvailable machine materials:")
    print("1. Wood")
    print("2. Aluminum")
    print("3. Carbon Fiber")
    
    material_choice = input("Select the material for your arcade machine (1, 2, 3): ")
    material_mapping = {"1": "wood", "2": "aluminum", "3": "carbon fiber"}
    if material_choice not in material_mapping:
        print("Invalid choice. Please select a valid option.")
        return

    selected_material = material_mapping[material_choice]
    machine = ArcadeMachine(material=selected_material)

    print("\nAvailable games:")
    for idx, game in enumerate(catalog.get_games(), start=1):
        print(f"{idx}. Code: {game.code}, Name: {game.name}, Genre: {game.genre}")

    print("\n4. Add a new game")
    print("5. Continue with purchase")

    selected_games = []
    while True:
        game_choice = input("Select a game by number (or choose 4 to add a new game, 5 to continue): ")
        if game_choice == "5":
            break
        elif game_choice == "4":
            new_game_code = input("Enter the code for the new game: ")
            new_game_name = input("Enter the name for the new game: ")
            new_game_genre = input("Enter the genre for the new game: ")
            new_game_price = float(input("Enter the price for the new game: "))
            new_game = Game(code=new_game_code, name=new_game_name, genre=new_game_genre, price=new_game_price)
            catalog.add_game(new_game)
            print(f"Added new game: {new_game.name}")
        elif game_choice.isdigit() and 1 <= int(game_choice) <= len(catalog.get_games()):
            game = catalog.get_games()[int(game_choice) - 1]
            selected_games.append(game.code)
            print(f"Selected game: {game.name}")
        else:
            print("Invalid choice. Please select a valid option.")

    total_amount = machine_cost + sum(game.price for game in catalog.get_games() if game.code in selected_games)
    purchase_date = datetime.now()
    purchase = Purchase(purchase_date=purchase_date, total_amount=total_amount)
    purchase.finalize_purchase()

    receipt_text = purchase.generate_receipt()
    with open("receipt.txt", "w", encoding='utf-8') as file:
        file.write(receipt_text)

    print("\nPurchase completed. Receipt has been saved to 'receipt.txt'.")

if __name__ == "__main__":
    main()
