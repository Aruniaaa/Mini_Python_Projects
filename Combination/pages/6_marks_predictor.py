import numpy as np
import streamlit as st

if not "weights" in st.session_state:  
   st.session_state.weights = np.random.randn(2)
if not "hours_studied" in st.session_state:  
   st.session_state.hours_studied = 0
if not "hours_slept" in st.session_state:  
   st.session_state.hours_slept = 0
if not "predicted_score" in st.session_state:  
   st.session_state.predicted_score = 0
if not "inputs" in st.session_state:  
   st.session_state.inputs = []
if not "button" in st.session_state:  
   st.session_state.button = False


if st.session_state.hours_studied == 0 and st.session_state.hours_slept == 0:

  with st.form("inputs_user"):
     st.session_state.hours_studied = st.number_input("Enter the hours studied: ")
     st.session_state.hours_slept = st.number_input("Enter the hours slept: ")

     st.session_state.button = st.form_submit_button()
  
if st.session_state.button:

  st.session_state.inputs = np.array([st.session_state.hours_studied, st.session_state.hours_slept])

  st.session_state.predicted_score = np.dot(st.session_state.inputs, st.session_state.weights) 
  st.success(f"Predicted score (before updating the weights) - {st.session_state.predicted_score}")

if st.session_state.hours_studied != 0 and st.session_state.hours_slept != 0:
  actual_score = st.number_input("Enter your actual score: ")
  
  
  if actual_score != st.session_state.predicted_score and actual_score != 0:
   for x in range(20):
    error = actual_score - st.session_state.predicted_score
    nw1 = st.session_state.weights[0] + (error * st.session_state.inputs[0] * 0.01)
    nw2 = st.session_state.weights[1] + (error * st.session_state.inputs[1] * 0.01)
    st.session_state.weights = np.array([nw1, nw2]) 
    st.session_state.predicted_score = np.dot(st.session_state.inputs, st.session_state.weights)  
  
  if actual_score != 0:      
    st.success(f"Predicted score (after updating the weights) - {st.session_state.predicted_score}, Actual score - {actual_score}")
    if st.button("Enter new values"):
                 
                        for key in ['hours_studied', 'hours_slept', 'inputs', 'predicted_score', 'button']:
                                if key in st.session_state:
                                   del st.session_state[key]
                        st.rerun()
                 
    
          



