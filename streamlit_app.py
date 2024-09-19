import streamlit as st

# Create a title for the app
st.title("Simple Streamlit App")

# Create a container with custom HTML and CSS
st.markdown("""
    <style>
        .container {
            background-color: #f0f0f0;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    <div class="container">
        <h2>Hello, World!</h2>
        <p>This is a custom HTML container.</p>
    </div>
""", unsafe_allow_html=True)

# Create a text input field
text_input = st.text_input("Enter your name:")

# Create a button
button_clicked = st.button("Submit")

# Check if button is clicked
if button_clicked:
    # Display greeting message
    st.write(f"Hello, {text_input}!")
