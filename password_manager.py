import random
import string
with open ("passwords.txt", "r") as f:
    tracker = f.read()
x = 0
password = ""
choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"


class Passwordmanager:
    def __init__(self, website, username, password, tracker):
        self.website = website
        self.username = username
        self.password = password
        self.tracker = tracker

    # Function to loa):
    def load(self):
     self.tracker = {}
     try:
         with open("passwords.txt", "r") as file:
             for line in file:
                # Parse the line: "website - username , password"
                 parts = line.strip().split(" - ")
                 if len(parts) == 2:
                     self.website = parts[0]
                     user_pass = parts[1].split(" , ")
                     if len(user_pass) == 2:
                         self.username, self.password = user_pass
                         self.tracker[self.website] = [self.username, self.password]
         print("Tracker loaded from file.")
     except FileNotFoundError:
         print("File not found. Starting with an empty tracker.")
     return tracker

    def enter(self):
        amount = int(input("How many password manager enteries do you wish to create? "))
        for i in range(amount):
            self.website = input("Enter the website name: ").lower()
            self.username = input("Enter the username: ")
            if self.website in self.tracker and self.username in self.tracker:
                print("Website and Username alreadye exists! ")
                pass
            else: 
             length = random.randint(8, 12)

             self.password = ""

             while len(self.password)  <= length:
                 self.choice = random.randint(0, len(choices) - 1)
                 self.password = self.password + choices[self.choice]
                

             self.tracker[self.website] = [self.username, self.password]
             print(self.tracker)
             with open ("passwords.txt", "a") as file:
                 file.write(f"{self.website} - {self.username} , {self.password}\n")

    def search(self):
        self.web = input("Enter the website name: ").lower()
        if self.web in self.tracker:
            print(self.tracker[self.web])
        else:
            print("website not found!")


t1 = Passwordmanager("", "", "", tracker)
t1.load()
cmd = input("Enter 'add' to create a new entry in the tracker or 'search' to search for a username/password: ").lower()
if cmd == "add":
  t1.enter()
elif cmd == 'search':
    t1.search()
else:
    print("please enter a valid command")


