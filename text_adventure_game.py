username = input("Enter a username: ")
if len(username) > 50 or len(username) < 3:
    print("Your username can't contain more than 50 characters or less than 3 characters, try again. ")
    exit()
else:
    print(f"Welcome to the game, {username}")

direction = input(f"""You are standing in the middle of a dense forest.
You see two paths ahead of you, right and left, which way do you proceed, {username}?
""").lower()

if direction == 'right':
    action = input("""You go right and see a small cottage that seems to have light.
Do you knock on the door or ignore it? (type 'knock' to knock on the door and 'ignore' to ignore)""").lower()
    if action == 'knock':
        print(f"""A xylem, monster of the forest opens the door, it grabs you inside, and plans you as its next meal.
Game over, {username} """)
        quit()
       
    elif action == 'ignore':
        ignore_action = input(f"""You ignore the cottage, but find yourself getting hungry. 
Do you knock on the door or decide to explore for some time? (type 'knock on the door' to knock and 'explore' to explore the forests.) """).lower()
        if ignore_action == 'knock on the door':
         print(f"""A xylem, monster of the forest opens the door, it grabs you inside, and plans you as its next meal.
Game over, {username} """)
         quit()
        elif ignore_action == 'explore':
            action_left = input("""You explore the dark woods and after some time, see a large lake.
Do you try to swim or try to find materials to build a raft? (type 'swim' to swim and 'find' to find materials).""").lower()
            if action_left == 'swim':
                print(f"""You try to swim your way across, but you realize the lakes are full of vicious crocodiles.Perhaps a bit too late for such a realization.
A crocodile swims towards you and eats you up. Game over, {username}""")
                quit()
            
            elif action_left == 'find':
             print(f"""You find all the materials required and build a raft. You use this to travel across the lake, and finally find a village
You have finished and won the game, {username}. Congratulations""")
             print("Part I of 'What do you do?' finished")
            else:
                print("Please check your response for a typo or error and try again.")
        else:
            print("Please check your response for a typo or error and try again.")
        
        
    else:
        print("Please check your response for a typo or error and try again.")
        quit()
        

elif direction == 'left':
    action_left = input("""You go left and after some time, see a large lake. 
Do you try to swim or try to find materials to build a raft? (type 'swim' to swim and 'find' to find materials""").lower()
    if action_left == 'swim':
        print(f"""You try to swim your way across, but you realize the lakes are full of vicious crocodiles.Perhaps a bit too late for such a realization.
A crocodile swims towards you and eats you up. Game over, {username}""")
        quit()
    elif action_left == 'find':
        print(f"""You find all the materials required and build a raft. You use this to travel across the lake, and finally find a village
You have finished and won the game, {username}. Congratulations""")
        print("Part I of 'What do you do?' finished.")
else:
    print("Please check your response for a typo or error and try again.")
    quit()