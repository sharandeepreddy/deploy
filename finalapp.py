import streamlit as st


# Function to display the main website
def display_main_website(url):
    st.components.v1.iframe(url, height=600)

# Main Streamlit app
def main():
    st.title("Combined Websites")

    # Button to go to website 1
    if st.button("Go to Website 1"):
        display_main_website("https://group17.streamlit.app/")

    # Button to go to website 2
    if st.button("Go to Website 2"):
        display_main_website("https://group17web1.streamlit.app")

# Run the main Streamlit app
if __name__ == "__main__":
    main()
