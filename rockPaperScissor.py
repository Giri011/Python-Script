import random

rps=input("Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if rps=="0":
    print("Rock")
elif rps=="1":
    print("Paper")
elif rps=="2":
    print("Scissors")
else:
    print("Invalid input. Please enter 0, 1, or 2.")

print("Computer chose:")
comp=random.randint(0,2)
if comp==0:
    print("Rock")
elif comp==1:
    print("Paper")
elif comp==2:
    print("Scissors")
if rps=="0" and comp==2:
    print("You win!")
elif rps=="1" and comp==0:
    print("You win!")
elif rps=="2" and comp==1:
    print("You win!")
elif rps==comp:
    print("It's a draw!")
else:
    print("You lose!")
    
