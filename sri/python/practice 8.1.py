import streamlit as st
st.title("beggining")
n=st.number_input(("enter the no of series:"))
a=0
b=1
for i in range(0,n):
    st.write(a,end=" ")
    c=a+b
    a=b
    b=c

             
