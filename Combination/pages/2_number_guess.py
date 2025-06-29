import streamlit as st
import random
import time

st.title("Enter the max and min for the random number below!")

with st.form("max_min_inputs"):
    ran = st.number_input("Enter the maximum range: ")
    min_ran = st.number_input("Enter the minimum range: ")
    submitted = st.form_submit_button("Set Range")
    
if submitted:
     min_ran = int(min_ran)
     ran = int(ran)
     if min_ran > ran:
       st.error("Minimum range must be smaller than maximum range!")
       st.rerun()
     else:
          st.session_state.min = min_ran
          st.session_state.max = ran
          st.session_state.attempts = 0
          st.session_state.started = True
          st.session_state.target = random.randint(st.session_state.min, st.session_state.max)
     


if hasattr(st.session_state, 'started') and st.session_state.started:
     
     guess = st.number_input("Enter your guess!")
     if guess != 0:
       st.session_state.attempts += 1
     if guess > st.session_state.max or guess < st.session_state.min:
              st.warning(f"Please enter a number between {st.session_state.min} to {st.session_state.max}")
     else:
             if guess == st.session_state.target:
                    st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
                    if st.button("Play Again"):
                 
                        for key in ['started', 'target', 'attempts', 'min', 'max']:
                                if key in st.session_state:
                                   del st.session_state[key]
                        st.rerun()
                 
          
                 
             else:
               st.info(f"Attemps -> {st.session_state.attempts}")
               if guess > st.session_state.target:
                     st.warning("Too high!")
               else:
                     st.warning("Too low!")


         
    
