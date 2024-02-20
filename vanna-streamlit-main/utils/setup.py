import streamlit as st
import vanna as vn

def setup_connexion():
    # Set Vanna API key and model directly
    vn.set_api_key('d7cd1bd648894b48aeee39f3e507fb61')
    vn.set_model('chinook')
    
    # Connect to SQLite without specifying project_id
    vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

def setup_session_state():
    st.session_state["my_question"] = None

# Call the setup functions
setup_connexion()
setup_session_state()

# Now you can use Vanna functions in your Streamlit app
