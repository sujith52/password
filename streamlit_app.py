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
       
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:  # Center column
            # Display the image with fit width
                st.success("Logged in successfully!")
                st.image(myurl, caption="G. Sujith Kumar", use_column_width=True)
        
        # Add your main interface components here
                st.write("Welcome to the Dark World all my Fellow People")
        
    else:
        st.error("Invalid password")
