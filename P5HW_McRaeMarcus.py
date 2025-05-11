#Marcus McRae
#04/29/25
#P5HW
#Simple character creation game 

import random

def create_character():
    name = input("Enter your character's name: ")
    life = int(input(f"Enter {name}'s starting life: "))
    attack = int(input(f"Enter {name}'s attack points: "))
    defense = int(input(f"Enter {name}'s defense points: "))

    return {
        "Name": name,
        "Life": life,
        "Attack": attack,
        "Defense": defense,
        "Inventory": []
    }

def adventure(character):
    events = ["find potion", "battle monster", "find treasure"]
    event = random.choice(events)
    print(f"\nAdventure event: {event.upper()}!")

    if event == "find potion":
        heal = random.randint(10, 30)
        character["Life"] += heal
        print(f"You found a life potion! Life increased by {heal}.")
    elif event == "battle monster":
        damage = random.randint(5, 20)
        character["Life"] -= damage
        print(f"A monster attacked you! You lost {damage} life.")
    elif event == "find treasure":
        treasure = random.choice(["Magic Sword", "Shield", "Life Potion"])
        character["Inventory"].append(treasure)
        print(f"You found a {treasure}!")

def battle(character):
    enemy_life = random.randint(30, 70)
    enemy_attack = random.randint(5, 15)
    print("\nYou encounter a rogue enemy!")
    print(f"Enemy Life: {enemy_life}, Enemy Attack: {enemy_attack}")

    action = input("Do you want to 'attack' or 'run'? ").lower()
    if action == "attack":
        damage = character["Attack"] + random.randint(-2, 5)
        enemy_life -= damage
        print(f"You hit the enemy for {damage} damage!")

        if enemy_life > 0:
            taken = max(enemy_attack - character["Defense"], 0)
            character["Life"] -= taken
            print(f"The enemy attacks! You lose {taken} life.")
        else:
            print("You defeated the enemy!")

    elif action == "run":
        print("You ran away.")
    else:
        print("Invalid action.")

def main():
    print("Welcome to Fillory! Create your Character:")
    character = create_character()

    continue_game = "yes"
    while continue_game.lower() == "yes":
        print("\nWhat would you like to do?")
        print("1. Display Character")
        print("2. Go on an Adventure")
        print("3. Battle an Enemy")
        print("4. Exit Game")
        choice = input("Enter choice: ")

        if choice == "1":
            print("\nCharacter Info:")
            for key, value in character.items():
                print(f"{key}: {value}")
        elif choice == "2":
            adventure(character)
        elif choice == "3":
            battle(character)
        elif choice == "4":
            print("Thanks for playing!")
            return
        else:
            print("Invalid choice.")

        continue_game = input("\nDo you want to continue? (yes/no): ")

if __name__ == "__main__":
    main()
