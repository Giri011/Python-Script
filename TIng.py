import random

def human_guess_game():
    number = random.randint(1, 100)
    tries = 0
    print("🤖 I've picked a number between 1 and 100.")
    while True:
        guess = int(input("🔍 Your guess: "))
        tries += 1
        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {tries} tries.")
            return tries

def computer_guess_game():
    low = 1
    high = 100
    tries = 0
    print("🎯 Think of a number between 1 and 100. I will guess it.")
    input("Press Enter when you're ready...")
    while low <= high:
        guess = (low + high) // 2
        print(f"🤖 Is it {guess}?")
        response = input("Type 'h' for too high, 'l' for too low, or 'c' for correct: ").lower()
python guess_game.py
