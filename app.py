import streamlit as st
import bcrypt

st.markdown("""
Welcome to our new app
""")


def login():
    st.title("Login")
    st.write("We will login here")
    with st.form(key='my_form'):
        username , passcode = st.columns(2)
        with username:
            U_name = st.text_input("Username")
        with passcode:
            U_code = st.text_input("Password",type="password")
        password = U_code
        hashed = bcrypt.hashpw("a".encode(), bcrypt.gensalt())
        submit_button=  st.form_submit_button('Login')
        if submit_button:
            if bcrypt.checkpw(password.encode(), hashed):
                st.write("It Matches!")
            else:
                st.write("Failed!")
    with st.form(key='request_api'):
        City_name = st.text_input("City")
        request_button = st.form_submit_button("request")
        if request_button:
            st.write(City_name)
            # api call here
    # btn2 = st.button('Need an acount? register here')
    # if btn2 :
    #     st.write("here")

login()