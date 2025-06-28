import streamlit as st
import sqlite3 as sq
import datetime

today = datetime.datetime.now()

today_as_string = today.strftime("%Y-%m-%d")

conn = sq.connect('users.db')

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users(
            name text,
            counter integer,
            last_reset text

            )""")

query = "SELECT * FROM users WHERE name = ?"

cur.execute(query, ("Charu", ))

data = cur.fetchall()

if len(data) == 0:
      cur.execute("INSERT INTO users VALUES ('Charu', 0, '0-0-0')")

      cur.execute(query, ("Charu", ))
      data = cur.fetchall()




name = data[0][0]
counter = data[0][1]
last_reset = data[0][2]

if last_reset != today_as_string:
      cur.execute("""UPDATE users SET counter = ?, last_reset = ? WHERE name = ?""", (0, today_as_string, name))
      conn.commit()



cur.execute(query, ("Charu", ))

data = cur.fetchall()

name = data[0][0]
counter = data[0][1]
last_reset = data[0][2]


st.set_page_config(
    page_title="Touch Some Grass, Bro",
    page_icon="💚",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #000042;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px rgba(100, 71, 255, 0.3);
    }
            
    .status-text {
        font-size: 1.5rem;
        text-align: center;
        color: #c6d3e3;
        width: 100%;
        font-weight: 500;
        margin-top: 3rem;
    }
    
    .stButton > button {
        width: 50%;
        height: 100px;
        text-align: center;
        font-size: 1.2rem;
        button-align: center;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        transition: all 0.3s ease;
        margin: 0.5rem 0;
        margin-top: 3rem;
    }
    
    .touch-button {
        background: linear-gradient(145deg, #ff4757, #ff3742);
        color: white;
    }
    
    
   
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">Touch the Grass!!</h1>', unsafe_allow_html=True)

if "counter" not in st.session_state:
    st.session_state.counter = counter
if "grass" not in st.session_state:
    st.session_state.grass = False




left_spacer, button_col1, button_col2, right_spacer = st.columns([2, 1, 1, 2])



with button_col1:
      button1 =  st.button("🌿", key="grass1")

with button_col2:
      button2 = st.button("🌱", key="grass2")


   
if not st.session_state.grass:
            if button1 or button2:
                 st.session_state.grass = True
                 st.rerun()       
else:
        st.session_state.counter += 1
        cur.execute("""UPDATE users SET counter = ? WHERE name = ? """, (st.session_state.counter, name))
        conn.commit()
        st.session_state.grass = False




    
st.markdown(f'<div class="status-text"> You have touched grass {st.session_state.counter} times in total today! </div>', unsafe_allow_html=True)