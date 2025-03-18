response_set = {"sad": ["I am sorry to hear that. Do you think you can find a way to let it all out? Journaling or Crying perhaps?",
                        "Don't worry, it will get better. Life ALWAYs works out. You could try listening to some happy songs to cheer you up",
                        "I get it, feeling sad is like feeling you've hit rock bottom sometimes, it gets better hon. Do you think you can reach out to a trusted adult to talk about it?"
                        ],
                    "stressed" : ["Hey it's okay, it will be okay. Don't stress out. ",
                                  "It is completely human and sometimes good to be stressed. Do you think you can try writing down exactly why you feel stressed?"
                                  ],
                    "anxious" : ["Hey, listen to me, name 5 things you can see, 4 things you can touch/feel, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
                                 "Alright, lets go thorugh some breathing exercises. Inhale for 4 seconds, Hold for 4, Exhale for 4, and Hold again for 4. Repeat it atleast 5 times okay?"
                                 ]}

def main():
    import random
    while True:
        msg = input("MindfulListner: Hey! How are we doing today? ").lower()
        msg = msg.strip("!?.,")
        word_list = [word.strip("!?.,") for word in msg.split()]
        if 'exit' in word_list or 'bye' in word_list:
            print("MindfulListner: Take care, and remember, you are not alone. Goodbye!<3 ")
            break
        else:
            found = False
            for word in word_list:
                if word in response_set:   
                  print(random.choice(response_set[word]))
                  found = True
                  break 
            if not found:
                print("I am sorry, this chatbot is not prepared for that response yet. Maybe try talking to a trusted adult, journal, or pursure some relaxing hobbies.")
        break 


def mood_score(): 
     mood_log = {}    
     day = input("Please enter today's day: ").lower() 
     score = int(input("MindfulListner: Please enter your mood score between 1 to 5 (1 being the lowest, for bad moods and 5 being the highest, for great moods)."))
     if 1 <= score or score>= 5:
        symbol = "✦" * score
        mood_log[day] = [score, symbol]
        print(mood_log)
     else:
           input("Please enter a score between 1 to 5.")


    
         
    


start_input = input("MindfulListner: Please type 'hi' to talk, 'score' to track your mood score, and 'quit' to exit: ").lower()
if "hi" in start_input:
    main()
elif "score" in start_input:
    mood_score()
else:
    print("MindfulListner: Okay, just remember that I am here if you want to talk. Have a nice day/night ahead!")
    quit()