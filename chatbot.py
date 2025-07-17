import json
from difflib import get_close_matches
import time

def load_knowledge_base(file):
    with open(file, 'r') as file:
        data = json.load(file)

    return data


def save_knowledge_base(file, data):
    with open(file, "w") as file:
        json.dump(data, file, indent=2)


def find_best_matches(question, questions):
    matches = get_close_matches(question, questions, n=1, cutoff=0.6)

    return matches[0] if matches else None

def get_answer(question, kb):
    for q in kb["questions"]:
        if q["question"] == question:
            return q["answer"]
    
    return None


def chat_bot():
    kb = load_knowledge_base("data.json")
    while True:
        user_question = input("You: ").lower()
        if user_question == 'q':
            print("Bot: Goodbye!")
            time.sleep(1)
            break
        else:
            best_match = find_best_matches(user_question, [q["question"] for q in kb["questions"]])

            if best_match != None:
                answer = get_answer(best_match, kb)
                print(f"Bot: {answer}")
            else:
                print("Bot: I don't know the answer to that. Can you tell me? ")
                new_answer = input("Type the answer or 'skip' to skip: ").lower()

                if new_answer != 'skip':
                    kb["questions"].append({"question": user_question, "answer" : new_answer})
                    save_knowledge_base("data.json", kb)
                    print("Bot: Got it!")

chat_bot()