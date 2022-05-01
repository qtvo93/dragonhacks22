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


#%%
st.title('Welcome to AirCare')

#---------------------------------#
# About
expander_bar = st.expander("About the AirCare App")

expander_bar.markdown("""
* **AirCare App** is a simple Web-App to demonstrate Python, SQLalchemy, Twilio, Mailgun, and Data Science Streamlit framework
* **Version 1.0:** App written by Quoc Thinh Vo - Tuong Tran - Hiep Nguyen.                                                                                                                                     
    
""" )

#---------------------------------#

def welcome():
    st.write("Going to a new city and worry about the real-time Air Quality?")
    st.subheader("Enter a city name to look for real-time Air Quality index")
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
        user_email = st.text_input("Email")     
        request_button = st.form_submit_button("Request")
        if request_button:
            request_url = "https://api.waqi.info/feed/{}/?token=5938b35ceb20607ac17a113fe733908af8fbb1b7".format(city_name)
            #st.write(city_name)
            req = requests.get(request_url)
            if req.status_code == 200:
                st.write("Real-time Air Quality index in {}:".format(city_name))
                st.write(req.json()["data"]["aqi"]) 
                lat, lon = req.json()["data"]["city"]["geo"][0], req.json()["data"]["city"]["geo"][1]
            #st.write(user_email)
            
            engine = create_engine('sqlite:///users_db.sqlite')
            Session = sessionmaker(bind=engine)
            sess= Session()
            st.write("Your phone number is now in the list {}. You will be notifed every hour about the Air Quality index at {}".format(user_phone, city_name))  
            entry = UserInput(userPhone=user_phone, city=city_name, email = user_email)
            sess.add(entry)
            sess.commit()  
            time.sleep(5)
            legacy_caching.clear_cache()   
            data = pd.DataFrame({
            'cities' : [city_name],
            'lat' : [lat],
            'lon' : [lon]
                })
            st.map(data, zoom=9)

def unsub():
    with st.form(key='unsubscribe'):
        st.write("Want to unsubscribe from auto texting service?")
        user_phone = st.text_input("Phone") 
        request_button = st.form_submit_button("Unsubscribe")
        if request_button:
            engine = create_engine('sqlite:///users_db.sqlite')
            Session = sessionmaker(bind=engine)
            sess = Session()
            results = sess.query(UserInput).all()
            for result in results:
                if result.userPhone == user_phone:
                    sess.delete(result)
                    sess.commit() 
                    st.write("You are now unsubscribed from the alert list?")
                    legacy_caching.clear_cache()

if __name__ == "__main__":
    welcome()
    unsub()


