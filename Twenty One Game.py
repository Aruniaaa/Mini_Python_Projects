import time

"""

Playing Instructions  -

1. You can choose the number of players that will be palying this game, it only supports minimum 2 or maximum 4 players
as of now.
2. After that, each player can enter their own username which can range from 3 to 8 total characters.
3. The game will now begin, each player can count upto 3 numbers max which will be added to the counter, which starts
from zero.
4. The player whose count makes the counter reach 21, will be eliminated, the game will continue for the rest of the
players, until there is one final winner.
5. Your count can not make the counter 21. For example, if the counter is at 20, counting 2 would nmake the counter 22,
breaking the rules and general structure of the game.
6. The winner's name will be displayed when all the rounds end.

Note  - 'time.sleep(1)' and 'time.sleep(2)' has been added to the game to create a bit of suspense, make it
realistic, and exciting. If you wish to remove it, you can remove line number 65 and 70.

Have fun playing! 💗💗


"""

no_of_players = int(input("Enter the number of players between 2-4: "))

while no_of_players > 4 or no_of_players <= 1:
    print("Please enter a valid number of players between 2 and 4")
    no_of_players = int(input("Enter the number of players between 2-4: "))

names = []

for i in range(no_of_players):
    name: str = input(f"Please enter the username for player number {i + 1} --> ")
    while len(name) < 3 or len(name) > 8:
        print("The username can only be 3-8 characters long, try again!")
        name: str = input(f"Please enter the username for player number {i + 1} --> ")
    names.append(name)



def game(names, counter):
        while counter <= 21:
            for i in range(len(names)):
             entry_nos = int(
                input(f"""{names[i]}, how many numbers do you want to count upto? The current count is {counter}.
You can only count upto 3 numbers max at one go --> """))
             print("\n")
             while entry_nos > 3 or entry_nos < 0:
                print("Please enter a valid number you want to count upto.")
                entry_nos = int(
                    input(f"""{names[i]}, how many numbers do you want to count upto? The current count is {counter}.
You can only count upto 3 numbers max at one go --> """))

             while counter + entry_nos > 21:
                 print("Too far! That would go past 21. Try a smaller number 🚨")

                 entry_nos = int(input("Enter a new number: "))

             counter += entry_nos

             print(f"""{names[i]}, you have counted upto {entry_nos}, making the current count {counter} """)
             print("\n")
             time.sleep(1)
             if counter == 21:
                print(f"""{names[i]} has been eliminated! 🚫
                 
""")
                time.sleep(2)
                names.remove(names[i])
                return names

names = game(names, counter = 0)

while len(names) != 1:

    game(names, counter=0)

print(f"{names[0]} is the winner! 🏆💯")







