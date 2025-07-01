import streamlit as st  
import pandas as pd
import numpy as np
import altair as at


st.header("st.write")

st.write("**Hello** *World* :sunglasses:")

st.write(1234*4567)

df = pd.DataFrame({
    "first column": [1,2,3,4,5],
    "second column": [6,7,8,9,10]
})

st.write(df)

st.write("before", df , "after :tada:")

df1 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=["a","b","c"]
)
st.write(df1)