import streamlit as st
import random
import time


if not "scores" in st.session_state:
   st.session_state.scores = []


with st.form("no_of_users_input"):
   st.session_state.no_of_players = st.number_input("Enter the no of users: ")

   button = st.form_submit_button()


st.session_state.no_of_players = int(st.session_state.no_of_players)

if st.session_state.no_of_players != 0:
   with st.form("times_roll"):
       for i in range(1, st.session_state.no_of_players + 1):
           times_roll = st.number_input(f"Player {i}, how many times do you wanna roll the dice? ", key=i)
           times_roll = int(times_roll)
          
       button2 = st.form_submit_button()

       
           
       if button2:
           for j in range(st.session_state.no_of_players):
               score = 0
               for x in range(int(st.session_state[j + 1])):
                   number_rolled  = random.randint(1, 6)
                   if number_rolled == 1:
                       score = 0
                   else:
                       score += number_rolled
               st.session_state.scores.append(score)
               st.success(f"The score of player number {j + 1} is {score}.")
           

       if len(st.session_state.scores) == st.session_state.no_of_players:
           st.write("Here are the results")
           for index, score in enumerate(st.session_state.scores):
               index += 1
               st.success(f"Player number {index} scored {score}.")

           max_score  = max(st.session_state.scores)
           idx  = st.session_state.scores.index(max_score)
   
           st.warning(f"The winner is player number {idx + 1} with a score of {max_score}")