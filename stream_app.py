import streamlit as st 
import requests
user=st.text_input("Write down query here: ")
if user:
 url=f"https://e095-103-172-166-163.ngrok-free.app/Chatbot?user={user}"
 response=requests.get(url)
 data=response.json()
 if data:
  st.write(data['Output'])
