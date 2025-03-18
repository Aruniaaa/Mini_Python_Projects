import random
options = ['rock', 'paper', 'scissors']

 
def game():
    options = ['rock', 'paper', 'scissors']
    user_command = input("Rock, Paper, or Scissors? ").lower()
    bot_command = random.choice(options)
    print(f"The option chosen by Python is: {bot_command}")
    if user_command == 'rock' and bot_command == 'paper':
     print("Paper beats rock. You lose!")
    elif user_command == 'rock' and bot_command == 'rock':
     print("It's a draw.")
    elif user_command == 'rock' and bot_command == 'scissors':
     print("Rock beats scissors. You win!")
    elif user_command == 'paper' and bot_command == 'paper':
     print("It is a draw")
    elif user_command == 'paper' and bot_command =='rock':
     print("Paper beats rock. You win!")
    elif user_command == 'paper' and bot_command == 'scissors':
     print("Scissors beats paper. You lose!")
    elif user_command == 'scissors' and bot_command == 'scissors':
     print("It is a draw.")
    elif user_command == 'scissors' and bot_command == 'rock':
     print("Rock beats scissors. You lose")
    elif user_command == 'scissors' and bot_command == 'paper':
     print("Scissors beats paper. You win.")




while True:
   to_do = input("Enter 'play' to start and 'quit' to stop the game. ")
   if to_do == 'play':
     game()
   elif to_do == 'quit':
      print("Goodbye!")
      break
    

 






 




