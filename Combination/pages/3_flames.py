import streamlit as st

st.title("Enter your and your crush's name below!")

with st.form(key="love_calc_page"):
    your_name = st.text_input("Enter your name here!").lower()
    their_name = st.text_input("Enter your crush's here!").lower()

    button = st.form_submit_button("Play FLAMES!")

if button:
  lst = []
  flames = ['f', 'l', 'a', 'm', 'e', 's']  # friend, love, affection, marry, enemies, siblings

  your_name = list(your_name)
  their_name = list(their_name)

  for i in your_name[:]:
    if i in their_name:
        your_name.remove(i)
        their_name.remove(i)

  for i in range(len(your_name)):
    lst.append(1)
  for i in range(len(their_name)):
    lst.append(1)
  lst = sum(lst)

  index = 0
  while len(flames) != 1:
    index = (index + lst) % len(flames)
    val = flames[index]
    flames.pop(index)

  if len(flames) == 1:
    if 'm' in flames:
        st.success(f"You two got 'M' which means marry!!!")
    elif 'f' in flames:
        st.success(f"You two got 'F' which means friendship!!!")
    elif 'l' in flames:
        st.success(f"You two got 'L' which means love!!!")
    elif 'a' in flames:
        st.success(f"You two got 'A' which means attraction!!!")
    elif 'e' in flames:
        st.success(f"You two got 'E' which means enemies!!!")
    elif 's' in flames:
        st.success(f"You two got 's' which means siblings!!!")
