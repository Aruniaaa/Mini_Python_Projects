import random
target = 100
player_postions = []
target_player_postions = []

no_of_players = int(input("How many users will play with you today? "))
no_of_players += 1
reached_100 = 0.5 # a number to indicate that whether or not a player has reached 100

for i in range(no_of_players):
    player_postions.append(1)
    target_player_postions.append(reached_100)

counter_dict = {}
snakes = {
    98: 79,
    95: 75,
    93: 73,
    87: 24,
    64: 60,
    62: 19,
    54: 34,
    47: 16,
    17: 7
}

ladders = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 91
}



while(player_postions != target_player_postions):
     for i in range(len(player_postions)):
        if(player_postions[i] <= 100 and player_postions[i] != reached_100):
                 cmd = input(f"Player {i}, press enter to roll the dice 🎲")
                 if(cmd != ""):
                  print("Please enter a valid command.")
                 else:
                  rolled = random.randint(1, 6)
                 curr_position = player_postions[i] + rolled
                 if curr_position in snakes.keys():
                    curr_position = snakes[curr_position]
                    print(f"""
₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊
                          
🐍 Player {i} got bitten by a snake and is now in tile number {curr_position}

₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊

""")

                 if curr_position in ladders.keys():
                    curr_position = ladders[curr_position]
                    print(f"""
₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊
                          
🪜 Player {i} climbed a ladder and is now in tile number {curr_position}

₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊

""")
                 player_postions[i] = curr_position       
                 if curr_position >= 100:
                    player_postions[i] = reached_100
                    counter = player_postions.count(reached_100)
                    counter_dict[i] = counter
                    print(f"""
₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊
                          
💯🏆 Player {i} has reached 100!!

₊˚ ‿︵‿︵‿︵୨୧ · · ♡ · · ୨୧‿︵‿︵‿︵ ˚₊

""")
                 else:
        
                  print(f"""
                        
Player {i}, you rolled the number {rolled}. You are now at tile number {player_postions[i]}.
                        
                        """)
   

print("💗 Game over! The final rankings are -->")
for key, value in counter_dict.items():
   print(f"Player number {key} -> Rank {value}")



