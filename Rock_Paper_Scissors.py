import random

options = ("rock", "paper", "scissors")
warrior = None
robot = random.choice(options)

print("----WELCOME TO THE GREATEST GAME OF ALL TIME----")
print()
print("--------------ROCK PAPER SCISSORS---------------")
print()

warrior = input("In order to choose a warrior you need to spell his name (rock/paper/scissors): ").lower()
while warrior not in options:
    warrior = input("Don't anger the spirits, spell the name right (rock/paper/scissors): ").lower()

print()
print(f"The fierce warrior  {warrior.upper()} VS Lord {robot.upper()}")
print()
print("-------------------- FIGHT ---------------------")
print()

if warrior == robot:
    print("Tie! An onorable fight")
elif warrior == "rock" and robot == "scissors" or warrior == "paper" and robot == "rock" or warrior == "scissors" and robot == "paper":
    print(f"The {warrior.upper()} Warrior wins! Good choice")
else:
    print(f"The {warrior.upper()} Warrior loses! Train harder and come again")

print()
