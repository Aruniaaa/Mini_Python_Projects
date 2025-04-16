import random

def roll():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    while num1 == num2:
        num2 = random.randint(1,6)
    dice = set()
    dice = (num1, num2)
    print(dice)


def leave():
    return "Thanks for playing!"
    

while True:
    try:
        cmd = input("Roll the dice (y/n)? ").lower()
        if cmd == 'y':
            roll()
        elif cmd == 'n':
            leave()
            quit()
        else:
            print("Please enter a valid command!")
    except Exception as e:
        print(e)


    


