import random
import time

def print_divider():
    print("-" * 31)

def display_ui(player_hp, computer_hp):
    """Displays the current status of the game in a clean UI box."""
    print_divider()
    print(f"| {'PLAYER':<12} | {'COMPUTER':<12} |")
    print(f"| HP: {player_hp:<4}/100 | HP: {computer_hp:<4}/100 |")
    print_divider()

def main():
    player_hp = 100
    computer_hp = 100
    
    # Track defense status for the upcoming turn
    
    player_defending = False
    computer_defending = False

    print("  === WELCOME TO THE ARENA ===  ")
    
    while player_hp > 0 and computer_hp > 0:
        display_ui(player_hp, computer_hp)
        
        # --- PLAYER'S TURN INTERACTION ---
        valid_input = False
        player_action = ""
        
        while not valid_input:
            print("\nAvailable Actions:")
            print("[H] Show Health (Free Action)")
            print("[A] Attack")
            print("[D] Defend")
            print("[Q] Quit")
            
            choice = input("Choose your action: ").strip().lower()
            
            if choice == 'h':
                # Free action: Display UI again and don't consume the turn
                display_ui(player_hp, computer_hp)
            elif choice in ['a', 'd', 'q']:
                player_action = choice
                valid_input = True
            else:
                print("Invalid choice! Please choose A, D, H, or Q.")
        
        # Process Quit
        if player_action == 'q':
            print("\nYou fled from battle! Game Over.")
            break

        # --- COMPUTER'S DECISION ---
        # Computer randomly chooses to attack (70% chance) or defend (30% chance)
        computer_action = 'a' if random.random() < 0.7 else 'd'

        print("\n--- TURN RESOLUTION ---")
        time.sleep(0.5)

        # 1. Roll raw values for this turn
        player_roll = random.randint(1, 25)
        computer_roll = random.randint(1, 25)

        # 2. Process Defenses from the PREVIOUS turn
        # If player defended last turn, reduce computer's attack
        if player_defending:
            player_defense_pool = random.randint(1, 25)
            print(f"🛡️  Your active defense blocks up to {player_defense_pool} damage!")
            computer_roll = max(0, computer_roll - player_defense_pool)
            player_defending = False # Reset defense

        # If computer defended last turn, reduce player's attack
        if computer_defending:
            computer_defense_pool = random.randint(1, 25)
            print(f"🛡️  Computer's active defense blocks up to {computer_defense_pool} damage!")
            player_roll = max(0, player_roll - computer_defense_pool)
            computer_defending = False # Reset defense

        # 3. Execute Actions for Current Turn
        # Player Action Execution
        if player_action == 'a':
            print(f"⚔️  You strike the computer for {player_roll} damage!")
            computer_hp -= player_roll
        elif player_action == 'd':
            print("🛡️  You take a defensive stance for the next turn.")
            player_defending = True

        # Computer Action Execution
        if computer_action == 'a':
            print(f"💥 Computer strikes you for {computer_roll} damage!")
            player_hp -= computer_roll
        elif computer_action == 'd':
            print("🤖 Computer takes a defensive stance for the next turn.")
            computer_defending = True

        # Small pause for readability before the next round
        time.sleep(1.5)

    # --- GAME OVER WIN/LOSS CHECK ---
    print("\n=========================")
    print("       GAME OVER         ")
    print("=========================")
    display_ui(player_hp, computer_hp)

    if player_hp <= 0 and computer_hp <= 0:
        print("It's a draw! Both fell in the heat of battle.")
    elif player_hp <= 0:
        print("You lose! The computer defeated you.")
    elif computer_hp <= 0:
        print("Congratulations! You won the battle!")

if __name__ == "__main__":
    main()