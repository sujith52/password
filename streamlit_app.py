import streamlit as st

# Define the password
PASSWORD = "password"
myurl="https://huntwithsujith.wordpress.com/wp-content/uploads/2024/06/10000915153044423841202866234.png?w=642";

# Create a login page
st.title("Login")
password_input = st.text_input("Enter Password", type="password")

# Check if password is correct
if st.button("Login"):
    if password_input == PASSWORD:
        # Display the main interface
        st.success("Logged in successfully!")
        st.write("Welcome to the main interface!")
        st.image(myurl, caption="G. Sujith Kumar", width=300)
        
        # Add your main interface components here
        st.write("Welcome to the Dark World all my Fellow People")
        
    else:
        st.error("Invalid password")
