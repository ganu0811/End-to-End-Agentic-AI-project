# This load_ui is just for loading things initially whenever the page is loaded.

import streamlit as st
import os
from datetime import date

# The message in the UI page will either be a human message or an AI message

from langchain_core.messages import AIMessage, HumanMessage
from src.langgraph_agentic_ai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()  # configuration file
        self.user_controls = {}
    
    
    def initialize_session(self):
        return {
            "current_step": 'requirements',
            "requirements": "",
            "user_stories": "",
            "user_storeis": "",
             "po_feedback": "",
             "generated_code": "",
             "review_feedback": "",
             'decision': None
            
        }
    
    
    def render_requirements(self):
        st.markdown("## Requirements Subsmission ")
        st.session_state.state["requirements"] = st.text_area(
            "Enter your requirements: ",
            height = 200,
            key = "req_input"
        )
        
        if st.button("Submit Requirements", key="submit_req"):
            st.session_state.state['current_step'] = 'generate_user_stories'
            st.session_state.IsSDLC = True
        
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title= " 🤖" + self.config.get_page_title(), layout = 'wide')
        st.header("🤖" + self.config_get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        
        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_option()
            
            usecase_options = self.config.get_usecase_options()
            
            
            # LLM Selection
            
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls['selected_llm'] == 'Groq':
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Model", model_options)
                
                # API Key Input
                self.user_controls['GROQ_API_KEY'] = st.session_state['groq_api_key'] = st.text_input("API KEY", type = 'password') # The API key is being stored in the session state. ANd the session state is a text_input
                 
                
                # Validate API Key
                
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning(" Please enter your Groq API key to proceed. Don't have? refer : https://console.groq.com/keys")
            
            
            
            # Use Case Options
            
            self.user_controls['selected_usecase'] = st.selectbox('Select Usecases', usecase_options)
            
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            self.render_requirements() # Render requirements will load the right hand side of the app page.
        
        
        return self.user_controls
                