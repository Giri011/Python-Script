import time

def print_pause(message, delay=1.5):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("🌫️ You wake up in a dark, cold dungeon...")
    print_pause("🗝️ There's a rusty sword beside you.")
    print_pause("💀 You hear strange noises echoing in the halls.")
    print_pause("What will you do?")

def choose_path():
    print("\nYou see two paths:")
    print("1. Go left into the foggy tunnel.")
    print("2. Go right toward the flickering torchlight.")
    choice = input("Enter 1 or 2: ")
    return choice

def left_path():
    print_pause("\nYou walk carefully into the foggy tunnel...")
    print_pause("A wild goblin jumps out!")
    action = i
