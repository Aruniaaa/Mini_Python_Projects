import streamlit as st

st.title("Enter your and your crush's name below!")

with st.form(key="love_calc_page"):
    your_name = st.text_input("Enter your name here!").lower()
    their_name = st.text_input("Enter your crush's here!").lower()

    st.form_submit_button()



lst = []

def love_calc(your_name, their_name):

    your_name = list(your_name)
    their_name = list(their_name)

    for i in your_name[:]:
        if i in their_name:
            your_name.remove(i)
            their_name.remove(i)
            lst.append(2)

    for i in range(len(your_name)):
        lst.append(1)
    for i in range(len(their_name)):
        lst.append(1)


def reduce_list(lst):
    new = []
    left = 0
    right = len(lst) - 1

    while left < right:
        new.append(lst[left] + lst[right])
        left += 1
        right -= 1

    if left == right:
        new.append(lst[left])  

    return new



love_calc(your_name, their_name)

while len(lst) > 2:
    lst = reduce_list(lst)

if len(lst) != 0:
    st.write(f"Your love percentage is {lst[0]}{lst[1]}% ❤️")

