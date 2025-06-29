import random
import streamlit as st
options = ['rock', 'paper', 'scissors']

 
col1, col2, col3 = st.columns(3)

with col1:
  rock = st.button("🪨")
with col2:
  paper = st.button("🗞️")
with col3:
  scissors = st.button("✂️")


if rock:
    user_command = 'rock'
elif paper:
    user_command = 'paper'
elif scissors:
    user_command = 'scissors'
else:
    user_command = None

if user_command:
    bot_command = random.choice(options)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.header(f"The option chosen by Python is: {bot_command}")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    

    if user_command == 'rock' and bot_command == 'paper':
        st.subheader("Paper beats rock. You lose!")
    elif user_command == 'rock' and bot_command == 'rock':
        st.subheader("It's a draw.")
    elif user_command == 'rock' and bot_command == 'scissors':
        st.subheader("Rock beats scissors. You win!")
    elif user_command == 'paper' and bot_command == 'paper':
        st.subheader("It is a draw")
    elif user_command == 'paper' and bot_command == 'rock':
        st.subheader("Paper beats rock. You win!")
    elif user_command == 'paper' and bot_command == 'scissors':
        st.subheader("Scissors beats paper. You lose!")
    elif user_command == 'scissors' and bot_command == 'scissors':
        st.subheader("It is a draw.")
    elif user_command == 'scissors' and bot_command == 'rock':
        st.subheader("Rock beats scissors. You lose")
    elif user_command == 'scissors' and bot_command == 'paper':
        st.subheader("Scissors beats paper. You win.")

