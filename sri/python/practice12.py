import streamlit as st
n=st.number_input("enter number:")
s=st.number_math.sqrt(n)
st.write(s)
