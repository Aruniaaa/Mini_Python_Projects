import random
import streamlit as st


nietzsche = {
    "motivation": [
        "He who has a why to live can bear almost any how.",
        "That which does not kill us makes us stronger.",
        "No price is too high to pay for the privilege of owning yourself.",
        "Become who you are.",
        "In individuals, insanity is rare; but in groups, parties, nations and epochs, it is the rule."
    ],
    "depression": [
        "If you gaze long enough into an abyss, the abyss will gaze back into you.",
        "Invisible threads are the strongest ties.",
        "Man is the cruelest animal.",
        "Hope in reality is the worst of all evils because it prolongs the torments of man."
    ],
    "confusion": [
        "There are no facts, only interpretations.",
        "The snake which cannot cast its skin has to die.",
        "He who fights with monsters should look to it that he himself does not become a monster."
    ]
}

kafka = {
    "motivation": [
        "Start with what is right rather than what is acceptable.",
        "You are free, and that is why you are lost.",
        "A book must be the axe for the frozen sea within us.",
        "You do not need to leave your room. Remain sitting at your table and listen."
    ],
    "depression": [
        "I am a cage, in search of a bird.",
        "My 'fear' is my substance, and probably the best part of me.",
        "I no longer know if I wish to drown myself in love, vodka, or the sea.",
        "Sleep is the most innocent creature there is and a sleepless man the most guilty."
    ],
    "confusion": [
        "A first sign of the beginning of understanding is the wish to die.",
        "In the fight between you and the world, back the world.",
        "I have the true feeling of myself only when I am unbearably unhappy."
    ]
}


fyodor = {
    "motivation": [
        "To live without hope is to cease to live.",
        "Man is a mystery. It needs to be unraveled.",
        "Taking a new step, uttering a new word, is what people fear most.",
        "The mystery of human existence lies not in just staying alive, but in finding something to live for."
    ],
    "depression": [
        "Pain and suffering are always inevitable for a large intelligence and a deep heart.",
        "Lying to ourselves is more deeply ingrained than lying to others.",
        "Much unhappiness has come into the world because of bewilderment and things left unsaid."
    ],
    "confusion": [
        "The soul is healed by being with children.",
        "What is hell? I maintain that it is the suffering of being unable to love.",
        "Nothing in this world is harder than speaking the truth, nothing easier than flattery."
    ]
}


seneca = {
    "motivation": [
        "Difficulties strengthen the mind, as labor does the body.",
        "Luck is what happens when preparation meets opportunity.",
        "It is not that we have a short time to live, but that we waste a lot of it.",
        "The whole future lies in uncertainty: live immediately."
    ],
    "depression": [
        "We suffer more often in imagination than in reality.",
        "It is not the man who has too little, but the man who craves more, that is poor.",
        "A man who suffers before it is necessary, suffers more than is necessary."
    ],
    "confusion": [
        "He who is brave is free.",
        "If a man knows not to which port he sails, no wind is favorable.",
        "You act like mortals in all that you fear, and like immortals in all that you desire."
    ]
}

marcus = {
    "motivation": [
        "You have power over your mind – not outside events. Realize this, and you will find strength.",
        "The impediment to action advances action. What stands in the way becomes the way.",
        "Very little is needed to make a happy life; it is all within yourself.",
        "When you arise in the morning, think of what a precious privilege it is to be alive."
    ],
    "depression": [
        "Waste no more time arguing what a good man should be. Be one.",
        "How much more grievous are the consequences of anger than the causes of it.",
        "Do not indulge in dreams of having what you have not, but reckon the chief of the blessings you do possess."
    ],
    "confusion": [
        "The universe is change; our life is what our thoughts make it.",
        "Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.",
        "Accept whatever comes to you woven in the pattern of your destiny."
    ]
}

hypatia = {
    "motivation": [
        "Reserve your right to think, for even to think wrongly is better than not to think at all.",
        "All formal dogmatic religions are fallacious and must never be accepted by self-respecting persons.",
        "Falsity in intellectual action is intellectual immorality."
    ],
    "depression": [
        "Fables should be taught as fables, myths as myths, and miracles as poetic fantasies.",
        "To understand the things that are at our door is the best preparation for understanding those that lie beyond.",
        "Men will fight for superstition as quickly as for gold."
    ],
    "confusion": [
        "Life is an unfoldment, and the further we travel the more truth we can comprehend.",
        "The nature of the soul is eternal motion.",
        "There is no place for truth if the path is blocked by ignorance."
    ]
}


simone = {
    "motivation": [
        "Change your life today. Don't gamble on the future, act now, without delay.",
        "The most courageous act is still to think for yourself. Aloud.",
        "It is not in giving life but in risking life that man is raised above the animal."
    ],
    "depression": [
        "One is not born, but rather becomes, a woman.",
        "I tore myself away from the safe comfort of certainties through my love for truth — and truth rewarded me.",
        "In the face of an absurd world, you must act as if your choices still matter."
    ],
    "confusion": [
        "In itself, homosexuality is as limiting as heterosexuality: the ideal should be to be capable of loving a woman or a man.",
        "To lose confidence in one's body is to lose confidence in oneself.",
        "The body is not a thing, it is a situation."
    ]
}


philosophers = {
    "nietzsche": nietzsche,
    "kafka": kafka,
    "fyodor": fyodor,
    "seneca": seneca,
    "marcus": marcus,
    "hypatia": hypatia,
    "simone": simone
}


st.header("Enter a philosopher and a mood to get quotes!")

with st.form("inputs"):
     st.session_state.philosopher = st.text_input("""Enter a philosopher 
Possible options are -->
Kafka,                      
Fyodor,
Nietzsche,
Seneca,
Marcus, 
Hypatia, 
Simone
""").lower()
     st.session_state.mood = st.text_input(("""What's your mood for this random quote?
The possible options are -->
Motivation,
Confusion,
Depression""").lower())
     button  = st.form_submit_button()

if button:

  if st.session_state.philosopher not in philosophers.keys():
    st.warning("That philosopher doesn't exist in the database, looks like you are going to have to enter a different one 😅")
  elif st.session_state.mood != 'motivation' and st.session_state.mood != 'depression' and st.session_state.mood != 'confusion':
     st.warning("I don't have a quote for that mood, looks like you are going to have to enter a different one 😅")
  all_quotes = philosophers.get(st.session_state.philosopher)

  st.write(f"""The quote for you is --> 
{random.choice(all_quotes[st.session_state.mood])}""")

     


