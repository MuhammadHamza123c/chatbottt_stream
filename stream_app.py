import streamlit as st 
import requests
user=st.text_input("Write down query here: ")
url=f"https://8201-103-172-166-163.ngrok-free.app/Chatbot?user={user}"
response=requests.get(url)
data=response.json()

st.write(data['Output'])