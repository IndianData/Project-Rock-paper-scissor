import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [Rock, Paper, Scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
my_choice = choices[choice]
print(f"\nYou chose {my_choice}")

computer = random.randint(0, 2)
computer_choice = choices[computer]
print(f"\nComputer chose {computer_choice}")

if (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
  print("You win!")
elif (choice == 0 and computer == 1) or (choice == 1 and computer == 2) or (choice == 2 and computer == 0):
  print("You loose!")
elif choice == computer:
  print("It's a draw!")
