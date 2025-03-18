import datetime
import ast
import os


class List:
    def __init__(self, task, li):
        self.task = task
        self.li = []
        self.dict = {}
         # Load tasks from file
        if os.path.exists("to-do_list.txt"):
            with open("to-do_list.txt", "r", encoding="utf-8") as file:
               for line in file:
                # Parse the line
                task, details = line.strip().split(" - ")
                priority, due_date = ast.literal_eval(details)
                
                # Add to self.dict and self.li
                self.dict[task] = [priority, due_date]
                self.li.append(task)
        



    def add(self):
     while True:  
        task = input("Enter the task or enter Q to quit: ").lower()
        if task == 'q':
             self.main()
        else:
             prior = input("Do you want to enter the priority level for the task? (Enter any key to add priority or hit spacebar if you don't want to)").lower()
             if prior != " ":
                 try:
                  level = int(input("Enter the priority level from 1-5, 1 being lowest and 5 being highest: "))
                  self.priority = level * "⭐"
                 except Exception as e:
                     print(e)
             else:
                 self.priority = 'none'
            
             
             date = input("Do you want to enter the due date for the task? (Enter any key to add priority or hit spacebar if you don't want to)").lower()
             if date != " ":
                 try:
                     self.due_date = input("Enter the date (DD/MM/YYYY): ")
                 except Exception as e:
                     print(e)
             else:
                 self.due_date = 'none'

             self.dict[task] = [self.priority, self.due_date]
             self.li.append(task)
             print("\nUpdated To-Do List:")
             for i, t in self.dict.items():
                 print(f"{i} - {t}")
                

    def view(self):
        print("here are your tasks - ")
        for i, t in self.dict.items():
                print(f"{i} - {t}")
        self.main()
                


    def remove(self):
        print("here are your tasks - ")
        for i, t in enumerate(self.li):
         print(f"{i} - {t}")
        to_remove = int(input("Which task would you like to remove?: "))
        task_to_remove = self.li[to_remove]
        self.li.remove([to_remove])
        del self.dict[task_to_remove]

        print("\nUpdated To-Do List:")
        for i, t in self.dict.items():
            print(f"{i} - {t}")

    def quit(self):
        quit()

    def edit(self):
        print("here are your tasks - ")
        for i, t in enumerate(self.li):
         print(f"{i} - {t}")

        to_edit = int(input("Which task would you like to edit? (enter the serial number of the task): "))
        newtask = input("Enter the new task: ")
        oldtask = self.li[to_edit]
    
        del self.dict[oldtask]

        self.li[to_edit] = newtask

        
        
        prior = input("Do you want to enter the priority level for the task? (Enter any key to add priority or hit spacebar if you don't want to)").lower()
        if prior != " ":
                 try:
                  level = int(input("Enter the priority level from 1-5, 1 being lowest and 5 being highest: "))
                  self.priority = level * "⭐"
                 except Exception as e:
                     print(e)
        else:
                 self.priority = 'none'
            
             
        date = input("Do you want to enter the due date for the task? (Enter any key to add priority or hit spacebar if you don't want to)").lower()
        if date != " ":
            try:
                     self.due_date = input("Enter the date (DD/MM/YYYY): ")
            except Exception as e:
                     print(e)
        else:
                 self.due_date = 'none'

        self.dict[newtask] = [self.priority, self.due_date]

        print("\nUpdated To-Do List:")
        for i, t in self.dict.items():
            print(f"{i} - {t}")

       
        


    def main(self):
        try:
         cmd = input("""Enter "add" to add tasks     
Enter "view" to view tasks
Enter "edit" to edit tasks                  
Enter "remove" to remove tasks
Enter "quit" to quit the programme: """).lower()
         if cmd == 'add':
             self.add()
         elif cmd == 'view':
             self.view()
         elif cmd == 'edit':
             self.edit()
         elif cmd == "remove":
             self.remove()
         elif cmd == "quit":
            with open("to-do_list.txt", "a", encoding="utf-8") as file:
             for o, i in self.dict.items():
                file.write(f"{o} - {i} \n")
                
            self.quit()
        except Exception as e:
            print("Please enter a valid command!")
            print(f"Error - {e}")
        

t1 = List(" ", [])
t1.main()