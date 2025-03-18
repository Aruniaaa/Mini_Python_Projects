
tasks = []


def enter():
    amount_of_tasks = int(input("What is the amount of tasks you want to enter: "))
    while len(tasks) <= amount_of_tasks - 1:
     task = input("Enter the task: ")
     tasks.append(task)
    print("Your tasks are mentioned below")
    for i in tasks:
     print(i)
    with open( "project.txt", "w+") as file:
      for i in tasks:
         file.write(i + "\n")

      
enter()


while True:
 command = input("What do you want to do next?\nType 'quit' to quit, \nType 'enter' to enter more tasks. \nType 'edit' to edit a task. \nType 'remove' to remove a task. \nType 'view' to view your tasks").lower()
 if command == 'enter':
    x = int(input("What is the amount of tasks you want to enter: "))
    for i in range(x):
       task = input("Enter a task: ")
       tasks.append(task)
    for i in tasks:
     print (i)
    print("All tasks entered successfully! ")
    with open( "project.txt", "w+") as file:
      for i in tasks:
         file.write(i + "\n")
 elif command == 'quit':
    print("Goodbye!")
    break
 elif command == 'remove':
    for i in tasks:
        print(i)
    to_remove = int(input("Enter the no. of the task you want to remove: "))
    tasks.remove(tasks[to_remove - 1])
    print("Sucessfully removed! ")
    for i in tasks:
        print(i)
    with open( "project.txt", "w+") as file:
      for i in tasks:
         file.write(i + "\n")
 elif command == 'edit':
    for i in tasks:
        print(i)
    to_edit= int(input("Enter the no. of the task you want to edit: "))
    new = input("Enter the new task: ")
    tasks[to_edit - 1] = new
    for i in tasks:
        print(i)
    print("Tasks edited! ")
    with open( "project.txt", "w+") as file:
      for i in tasks:
         file.write(i + "\n")
 elif command == 'view':
    print("Here are your tasks! ")
    for i in tasks:
     print(i)
   
 else:
    print("Please enter a valid command")
    quit()