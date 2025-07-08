import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


button_clicked = st.button('click me')
st.write(f"Button clicked: {button_clicked}")

if button_clicked:
    st.write('Why hello there')
else:
    st.write('Goodbye')

