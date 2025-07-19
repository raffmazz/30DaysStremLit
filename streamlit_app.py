import streamlit as st
from datetime import time
from datetime import datetime


st.header("st.sliders")

age = st.slider("how old are you?", 0,120,30)
st.write(f"**I** am **{age}** old")


st.subheader("Range Slider")

values =st.slider("blablabla",
          0,
          100,
          (20,80)
          )

st.write(values[0])
st.write(values[1])


valuesTime = st.slider("Schedule an appointment,",
            value=(time(11,30), time(12,45))
        )

st.write(valuesTime[0])
st.write(valuesTime[1])

valueDateTime = st.slider("Schedule an appointment",
                          value=datetime(2025,7,19,8,16)
                          format="MM//DD//YY - hh:mm"
)

st.write(valueDateTime)

