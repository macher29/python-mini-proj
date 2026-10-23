import random

print("Type 0 to exit\n")

while True:
    user_choice = input("Rock / Paper / Scissor: ")
    computer_choice = random.randint(1 , 3)

    Dict = {
        "Rock" : 1,
        "Paper" : 2,
        "Scissor" : 3
    }

    reverse_Dict = {
        1 : "Rock",
        2 : "Paper",
        3 : "Scissor"
    }

    if Dict[user_choice] == computer_choice:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , It's a tie")

    elif Dict[user_choice] == 1 and  computer_choice == 2:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , Computer wins")

    elif Dict[user_choice] == 1 and  computer_choice == 3:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , you wins")

    elif Dict[user_choice] == 2 and  computer_choice == 1:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , you wins")

    elif Dict[user_choice] == 2 and  computer_choice == 3:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , Computer wins")

    elif Dict[user_choice] == 3 and  computer_choice == 1:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , Computer wins")

    elif Dict[user_choice] == 3 and  computer_choice == 2:
        print(f"Your choice: {user_choice} computer choice: {reverse_Dict[computer_choice]} , you wins")

    else:
        print("Oop's something went wrong")