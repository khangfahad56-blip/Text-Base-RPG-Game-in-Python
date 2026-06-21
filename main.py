#make this better

import random
import time

def menu():
    print("*******************************************")
    print("       Welcome to Text Base RPG Game       ")
    print("*******************************************")
    print("1:Check Your Health")
    print("2:Attack on Your Enemies")
    print("3:Defend For Enemies Attack")
    print("4:Quit the Game")
    print("*******************************************")

def print_health(health):
    print(f"Your Current is {health} Points.")

def cal_attack(defend):
    attack = random.randint(1,25)
    if defend > attack:
        attack = 0
    elif defend > 0:
        attack = attack - defend
    elif defend == 0:
        attack = attack
    return attack

def cal_defend():
    defend = random.randint(1,25)
    return defend

def main():
    player_hp = 100
    computer_hp = 100
    player_defend = 0
    computer_defend = 0
    AI = ["attack","defend"]

    menu()

    while True:

        try:

            #This is for User Attack and Defend Calculation and Printing for Player

            option = int(input("Please Select Your Option (1-4): "))
            time.sleep(1)

            if option == 1:
                print_health(player_hp)
                time.sleep(1)
                continue
            elif option == 2:
                player_attack = cal_attack(computer_defend)
                computer_hp -= player_attack
                print(f"You Performed {player_attack} Point on Computer")
                print(f"Computer Current Health is Now {computer_hp}")
                time.sleep(1)
            elif option == 3:
                player_defend = cal_defend()
                print(f"You Got {player_defend} Point Defend")
                time.sleep(1)
            elif option == 4:
                print("Thank for Using our Game")
                break
            else:
                print("Please Select Number Blw (1-4)!")
                print("And You have lose Your Turn")
                print("Have Fun!")
                time.sleep(1)

            #This is for Computer Attack and Defend Calculation PrintFor Computer

            choice = random.choice(AI)
            if choice == "attack":
                computer_attack = cal_attack(player_defend)
                player_hp -= computer_attack
                print(f"Computer Performed {computer_attack} Point on You")
                print(f"Your Current Health is Now {player_hp}")
                time.sleep(1)
            elif choice == "defend":
                computer_defend = cal_defend()
                print(f"Computer Got {computer_defend} Point Defend")
                time.sleep(1)

            #This is Winning and Losing Condition

            if player_hp <= 0:
                print("Your Health is 0, You Lose the Game")
                break
            elif computer_hp <= 0:
                print("Your Enemies Health is 0, You Win the Game")
                break
        
        # This is for Handling the Error if User Write String or Float Instead of Integer

        except ValueError:
            print("Only Write Numbers!")
            continue

if __name__ == "__main__":
    main()

