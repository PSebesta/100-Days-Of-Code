import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
print(choices[player_choice])
computer_choice = random.randint(0, 2)

if player_choice == 0 and computer_choice == 1:
    print(f"{choices[computer_choice]} You Lose")
elif player_choice == 0 and computer_choice == 2:
    print(f"{choices[computer_choice]} You win")
elif player_choice == 1 and computer_choice == 2:
    print(f"{choices[computer_choice]} You Lose")
elif player_choice == 1 and computer_choice == 0:
    print(f"{choices[computer_choice]} You win")
elif player_choice == 2 and computer_choice == 0:
    print(f"{choices[computer_choice]} You Lose")
elif player_choice == 2 and computer_choice == 1:
    print(f"{choices[computer_choice]} You win")
else:
    print(f"{choices[computer_choice]} It's a tie")
