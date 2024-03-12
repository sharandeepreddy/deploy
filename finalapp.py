import streamlit as st

# URLs of the external websites
website1_url = "https://group17.streamlit.app/"
website2_url = "https://group17web1.streamlit.app/"

# Main Streamlit app
def main():
    st.title("Combined Websites")

    # Button to go to website 1
    if st.button("Go to Website 1"):
        display_main_website()

    # Button to go to website 2
    if st.button("Go to Website 2"):
        display_main_website()

# Run the main Streamlit app
if __name__ == "__main__":
    main()
