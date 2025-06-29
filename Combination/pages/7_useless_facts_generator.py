import requests
import json
import streamlit as st
import time

url = "https://uselessfacts.jsph.pl/random.json?language=en"


if st.button("Generate a fact!"):
        request = requests.get(url)
        data = json.loads(request.text)
        useless_fact = data['text']
        st.success(useless_fact)
      
        

      

