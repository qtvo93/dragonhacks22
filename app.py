import streamlit as st
import bcrypt
import requests
import pandas as pd
import numpy as np
from streamlit import legacy_caching
import time
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqldatabase import UserInput


st.markdown("""
Welcome to our new app ***
Dragonhacks 2022 *** 
App written by:
Quoc Thinh Vo - Tuong Tran - Hiep Nguyen
""")

def welcome():
    st.title("Going to a new city and worry about the real-time Air Quality?")
    st.subheader("Simply enter a city name to look for real-time Air Quality index")
    # st.title("Login")
    # st.write("We will login here")
    # with st.form(key='my_form'):
    #     username , passcode = st.columns(2)
    #     with username:
    #         U_name = st.text_input("Username")
    #     with passcode:
    #         U_code = st.text_input("Password",type="password")
    #     password = U_code
    #     hashed = bcrypt.hashpw("a".encode(), bcrypt.gensalt())
    #     submit_button=  st.form_submit_button('Login')
    #     if submit_button:
    #         if bcrypt.checkpw(password.encode(), hashed):
    #             st.write("It Matches!")
    #         else:
    #             st.write("Failed!")
    with st.form(key='request_api'):
        city_name = st.text_input("City")
        user_phone = st.text_input("Phone")      
        request_button = st.form_submit_button("Request")
        if request_button:
            request_url = "https://api.waqi.info/feed/{}/?token=5938b35ceb20607ac17a113fe733908af8fbb1b7".format(city_name)
            #st.write(city_name)
            req = requests.get(request_url)
            if req.status_code == 200:
                st.write("real-time Air Quality index in {}:".format(city_name))
                st.write(req.json()["data"]["aqi"]) 
                lat, lon = req.json()["data"]["city"]["geo"][0],req.json()["data"]["city"]["geo"][1]
            #st.write(user_email)
            
            engine = create_engine('sqlite:///users_db.sqlite')
            Session = sessionmaker(bind=engine)
            sess= Session()
            st.write("You are now in the list {}. You will be notifed every 1 hour if the Air Quality index at the location is above 75".format(user_phone))  
            entry = UserInput(userPhone=user_phone, city=city_name)
            sess.add(entry)
            sess.commit()  
            time.sleep(5)
            legacy_caching.clear_cache()   
            data = pd.DataFrame({
            'awesome cities' : [city_name],
            'lat' : [lat],
            'lon' : [lon]
                })
            st.map(data)


        
            
    # btn2 = st.button('Need an acount? register here')
    # if btn2 :

# def subscribe():
#     with st.form(key='subscribe_button'):
#         user_email = st.text_input("Email")
#         submit_button = st.form_submit_button('Subscribe')
#         if submit_button:
#             st.write(user_email)
if __name__ == "__main__":
    welcome()


