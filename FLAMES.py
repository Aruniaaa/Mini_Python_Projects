lst = []
flames = ['f', 'l', 'a', 'm', 'e', 's'] # friend, love, affection, marry, enemies, siblings


your_name = input("Enter your name: ").lower()
their_name = input("Enter your crush's name: ").lower()
your_name = list(your_name)
their_name = list(their_name)

for i in your_name[:]:
    if i in their_name:
         your_name.remove(i)
         their_name.remove(i)
 

for i in range(len(your_name)):
        lst.append(1)
for i in range(len(their_name)):
        lst.append(1)
lst = sum(lst)


index = 0  
while len(flames) != 1:
    index = (index + lst) % len(flames)

    val = flames[index]

    flames.pop(index)



if 'm' in flames:
      print(f"You two got 'M' which means marry!!!")
elif 'f' in flames:
      print(f"You two got 'F' which means friendship!!!")
elif 'l' in flames:
      print(f"You two got 'L' which means love!!!")
elif 'a' in flames:
      print(f"You two got 'A' which means attraction!!!")
elif 'e' in flames:
      print(f"You two got 'E' which means enemies!!!")
elif 's' in flames:
      print(f"You two got 's' which means siblings!!!")
      
      