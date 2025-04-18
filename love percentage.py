lst = []

def love_calc():
    your_name = input("Enter your name: ").lower()
    their_name = input("Enter your crush's name: ").lower()
    your_name = list(your_name)
    their_name = list(their_name)

    for i in your_name[:]:
        if i in their_name:
            your_name.remove(i)
            their_name.remove(i)
            lst.append(2)

    for i in range(len(your_name)):
        lst.append(1)
    for i in range(len(their_name)):
        lst.append(1)


def reduce_list(lst):
    new = []
    left = 0
    right = len(lst) - 1

    while left < right:
        new.append(lst[left] + lst[right])
        left += 1
        right -= 1

    if left == right:
        new.append(lst[left])  

    return new



love_calc()

while len(lst) > 2:
    lst = reduce_list(lst)

print(f"Your love percentage is {lst[0]}{lst[1]}% ❤️")
