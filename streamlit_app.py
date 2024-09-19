import streamlit as st

# Configure Streamlit to allow custom CSS
st.set_option('unsafe_allow_html', True)

# Load Tailwind CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Create a title with custom font and styling
st.markdown("""
    <div class="text-4xl font-bold text-purple-600 text-center mb-4">
        Simple Streamlit App
    </div>
""", unsafe_allow_html=True)

# Create a container with custom styling
st.markdown("""
    <div class="max-w-md mx-auto p-4 bg-white rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold text-gray-700">Welcome!</h2>
        <p class="text-lg text-gray-500">This is a custom Streamlit app.</p>
    </div>
""", unsafe_allow_html=True)

# Create a text input field with custom styling
st.markdown("""
    <div class="max-w-md mx-auto p-2">
        <input type="text" placeholder="Enter your name" class="w-full p-2 pl-10 text-sm text-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600">
    </div>
""", unsafe_allow_html=True)

# Create a button with custom styling
st.markdown("""
    <div class="max-w-md mx-auto p-2">
        <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600">
            Submit
        </button>
    </div>
""", unsafe_allow_html=True)

# Create a footer with custom styling
st.markdown("""
    <div class="text-center text-gray-500 text-sm mt-4">
        Developed by <a href="#" class="text-purple-600 hover:text-purple-700">Your Name</a>
    </div>
""", unsafe_allow_html=True)
