import streamlit as st

st.header("st.sliders")

age = st.slider("how old are you?", 0,120,30)
st.write(f"**I** am **{age}** old")


st.subheader("Range Slider")

st.slider("blablabla",
          0,
          100,
          (20,80)
          )




