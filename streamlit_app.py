import streamlit as st

# Define the password
PASSWORD = "password"

# Create a login page
st.title("Login")
password_input = st.text_input("Enter Password", type="password")

# Check if password is correct
if st.button("Login"):
    if password_input == PASSWORD:
        # Display the main interface
        st.success("Logged in successfully!")
        st.write("Welcome to the main interface!")
        
        # Add your main interface components here
        st.write("This is where you'll add your app's content")
        
    else:
        st.error("Invalid password")
