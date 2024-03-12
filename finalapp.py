import streamlit as st

# URLs of the external websites
website1_url = "https://group17.streamlit.app/"
website2_url = "https://group17web1.streamlit.app/"

# Function to display the website based on the selected index
def display_website(website_index):
    if website_index == 0:
        st.components.v1.iframe(website1_url, height=600)
    elif website_index == 1:
        st.components.v1.iframe(website2_url, height=600)

# Main Streamlit app
def main():
    st.title("Combined Websites")

    # Session state variable to track the current website index
    current_website_index = st.session_state.get('current_website_index', 0)

    # Display the current website
    display_website(current_website_index)

    # Back button to switch to the previous website
    if current_website_index > 0:
        if st.button("Back"):
            st.session_state['current_website_index'] -= 1

    # Forward button to switch to the next website
    if current_website_index < 1:
        if st.button("Next"):
            st.session_state['current_website_index'] += 1

# Run the main Streamlit app
if __name__ == "__main__":
    main()
