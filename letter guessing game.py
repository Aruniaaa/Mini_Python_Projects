import random

possibilities = ['R', 'B', 'G', 'Y', 'O', 'V', 'W']
code = []
hints = []
hint_str = " "
guess_list = []
hint_possibilities = []
counter = 1

for i in range(4):
    code.append(random.choice(possibilities)) 


for i in code:
   if i not in hint_possibilities:
      hint_possibilities.append(i)

for i in range(len(possibilities)):
    ran = random.choice(possibilities)
    if ran not in hint_possibilities:
     hint_possibilities.append(ran)
     break

random.shuffle(hint_possibilities)
hints = hint_possibilities


for i in hint_possibilities:
   hint_str = " ".join(hint_possibilities)



print(f"Some of the letters from these hints are in the code, the code has {len(code)} number of letters, note that letters in the code can repeat: {hint_str}")


while True:
    correct_postions = 0
    incorrect_postions = 0
    guess = input("Enter your guesses and separate them by a space: ").upper()
    guess_list = guess.split(" ")
    try:
        for i in range(len(code)):
          if guess_list[i] == code[i]:
              correct_postions += 1
          if guess_list[i] != code[i] and guess_list[i] in code:
             incorrect_postions += 1
        if correct_postions == len(code):
          print(f"You guessed the code (which was: {code}), it took you {counter} attempts!")
          break
        else:
          print(f"Correct Positions --> {correct_postions} | Incorrect positions --> {incorrect_postions}")
        counter += 1
    except IndexError:
        print("You guessed more or less letters than given in the code, please try again.")