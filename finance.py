tracker = {}
def add():
    amt_of_entries = int(input("How many entries of expenses do you want to enter? "))

    for i in range(amt_of_entries):  
      category = input("Enter a category: ").lower()
      name = input("Enter the name of the expense: ").lower()
      amount_spent = float(input("Enter the amount of money you spent on this purchase. Only enter the number: "))
      if category not in tracker:
        tracker[category] = []  
      tracker[category].append((name, amount_spent))
      print(tracker)
    
      
   

    
add()


while True: 
    next_step = input("""
Enter 'add' to add entries again.
Enter 'quit' to quit and exit the tracker (ALL YOU DATA WILL BE REMOVED!)
Enter 'expense of category' to view the sum of total expense of a particular category
Enter 'total' to see the sum all your expenses.
""").lower()
    if next_step == 'add':
        add()
    elif next_step == 'quit':
        print("Goodbye!")
        break
    elif next_step == 'expense of category':
        which_category = input("Which category's items sum do you want to see? ").lower()
        if which_category in tracker:
            total = sum(amount for _, amount in tracker[which_category])
            print(total)
        else:
            print("Category does not exist!")
    elif next_step == 'total':
        total_sum = sum(amount for expenses in tracker.values() for _, amount in expenses)
        print(total_sum)
    else:
        print("Please enter a valid response.")



    


 
