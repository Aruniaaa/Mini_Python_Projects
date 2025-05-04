import random
import time

# —————— Nietzsche ——————
nietzsche = {
    "motivation": [
        "He who has a why to live can bear almost any how.",
        "That which does not kill us makes us stronger."
    ],
    "depression": [
        "If you gaze long enough into an abyss, the abyss will gaze back into you.",
        "Invisible threads are the strongest ties."
    ],
    "confusion": [
        "There are no facts, only interpretations."
    ]
}

# —————— Kafka ——————
kafka = {
    "motivation": [
        "Start with what is right rather than what is acceptable.",
        "You are free, and that is why you are lost."
    ],
    "depression": [
        "I am a cage, in search of a bird.",
        "My 'fear' is my substance, and probably the best part of me."
    ],
    "confusion": [
        "A first sign of the beginning of understanding is the wish to die."
    ]
}

# —————— Dostoevsky (Fyodor) ——————
fyodor = {
    "motivation": [
        "To live without hope is to cease to live.",
        "Man is a mystery. It needs to be unraveled."
    ],
    "depression": [
        "Pain and suffering are always inevitable for a large intelligence and a deep heart.",
    ],
    "confusion": [
        "The soul is healed by being with children."  # bruh what does this even mean sometimes??
    ]
}

# —————— Seneca ——————
seneca = {
    "motivation": [
        "Difficulties strengthen the mind, as labor does the body.",
        "Luck is what happens when preparation meets opportunity."
    ],
    "depression": [
        "We suffer more often in imagination than in reality.",
    ],
    "confusion": [
        "He who is brave is free."
    ]
}

# —————— Marcus Aurelius ——————
marcus = {
    "motivation": [
        "You have power over your mind – not outside events. Realize this, and you will find strength.",
        "The impediment to action advances action. What stands in the way becomes the way."
    ],
    "depression": [
        "Waste no more time arguing what a good man should be. Be one.",
    ],
    "confusion": [
        "The universe is change; our life is what our thoughts make it."
    ]
}

# —————— Hypatia (baddie #1) ——————
hypatia = {
    "motivation": [
        "Reserve your right to think, for even to think wrongly is better than not to think at all.",
    ],
    "depression": [
        "Fables should be taught as fables, myths as myths, and miracles as poetic fantasies.",
    ],
    "confusion": [
        "Life is an unfoldment, and the further we travel the more truth we can comprehend."
    ]
}

# —————— Simone de Beauvoir (baddie #2) ——————
simone = {
    "motivation": [
        "Change your life today. Don't gamble on the future, act now, without delay.",
    ],
    "depression": [
        "One is not born, but rather becomes, a woman.",
    ],
    "confusion": [
        "In itself, homosexuality is as limiting as heterosexuality: the ideal should be to be capable of loving a woman or a man."
    ]
}

# —————— Dictionary of all philosophers ——————
philosophers = {
    "nietzsche": nietzsche,
    "kafka": kafka,
    "fyodor": fyodor,
    "seneca": seneca,
    "marcus": marcus,
    "hypatia": hypatia,
    "simone": simone
}

try:
    philosopher = input("""Enter a philosopher 
Possible options are -->
Kafka                      
Fyodor 
Nietzsche 
Seneca 
Marcus 
Hypatia 
Simone
Your choice --> """).lower()
except Exception as e:
    print(f"Error occured - {e}!")
except ValueError:
    print(f"Please enter a valid philosopher's name")

if philosopher not in philosophers.keys():
    print("That philosopher doesn't exist in the database, looks like you are going to have to enter a different one 😅")
    quit()

try:
    mood = input("""What's your mood for this random quote?
The possible options are -->
Motivation
Confusion
Depression
Your choice --> """).lower()
except Exception as e:
    print(f"Error occured - {e}!")
except ValueError:
    print(f"Please enter a valid mood!")

all_quotes = philosophers.get(philosopher)
print("""

‧˚₊꒷꒦︶︶︶︶︶꒷꒦︶︶︶︶︶꒦꒷‧₊˚⊹

""")
print(f"""The quote for you is --> 
{random.choice(all_quotes[mood])}""")
time.sleep(10)