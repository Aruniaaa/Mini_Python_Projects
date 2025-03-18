import random

ran = int(input("Enter the maximum range: "))
min_ran = int(input("Enter the minimum range: "))

target = random.randint(min_ran, ran + 1)
counter = 0
while True:
    try:
     guess = (input("Enter your guess or Quit(Q) to quit the game: ")).lower()
     counter += 1
     if guess == "q":
         print(f"Goodbye!")
         break
     else:
         guess = int(guess)
         if guess > 0 and guess < 50:
             if guess == target:
                 print(f"Congratulations! You have guessed the number, it was {target}. It took you {counter} attempts to guess the number!")
                 break
             else:
                 if guess > target:
                     print("Too high!")
                 else:
                     print("Too low!")
         else:
             print("Please enter a number greater than 0 and smaller than 50!")
    except ValueError as v:
        print("Please enter a number and in the form of digits!")


print(f"The number was {target}")
     