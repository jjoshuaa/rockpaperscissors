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



choice =int(input("what do you choose ? Type 0 for rock , 1 for paper or 2 for scissors\n"))
if choice == 0:
  print(f"You chose\n{rock}")
elif choice > 3 or choice < 0: 
  print("You typed an invalid number, you lose!")
elif choice == 1:
  print(f"you chose\n{paper}")
else:
  print(f"you chose\n{scissors}")


#computer choice logic
cpu_choice = random.randint(0,1)
if cpu_choice == 0:
  print(f"computer chose\n{rock}")
elif cpu_choice == 1:
  print(f"computer chose\n{paper}")
else:
  print(f"Computer chose\n{scissors}")

#win logic 
if choice == 0 and cpu_choice == 2:
  print("You win!")
elif choice == 0 and cpu_choice == 2:
  print("You lose")
elif cpu_choice > choice:
  print("You lose")
elif choice > cpu_choice:
  print("You win!")
elif choice == cpu_choice:
  print("It's a draw")
