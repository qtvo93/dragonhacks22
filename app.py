import streamlit as st
import bcrypt
import requests





st.markdown("""
Welcome to our new app
""")

def welcome():
    st.write("Some form here")
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
        user_email = st.text_input("Email")
        request_button = st.form_submit_button("request")
        if request_button:
            request_url = "https://api.waqi.info/feed/{}/?token=5938b35ceb20607ac17a113fe733908af8fbb1b7".format(city_name)
            st.write(city_name)
            req = requests.get(request_url)
            st.write(req.json()["data"]["aqi"])
            #st.write(user_email)
            # api call here
    # btn2 = st.button('Need an acount? register here')
    # if btn2 :
    #     st.write("here")

def subscribe():
    with st.form(key='subscribe_button'):
        submit_button = st.form_submit_button('Subscribe')

welcome()
subscribe()
