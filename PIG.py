# input - how many users are there, 
import random
import time
scores = []
no_of_players = int(input("Enter the no of users: "))

for i in range(1, no_of_players + 1):
    score = 0
    print(f"This is the turn of player no. {i}.")
    time.sleep(2)
    times_roll = int(input("How many times do you wanna roll the dice? "))
    for x in range(times_roll):
        number_rolled  = random.randint(1, 6)
        if number_rolled == 1:
            score = 0
        else:
            score += number_rolled
    scores.append(score)
    print(f"The score of player number {i} is {score}.")
    time.sleep(3)

time.sleep(2)
print("Here are the results")
for index, score in enumerate(scores):
    index += 1
    print(f"Player number {index} scored {score}.")

max_score  = max(scores)
idx  = scores.index(max_score)
 
print(f"The winner is player number {idx + 1} with a score of {max_score}")
