import streamlit as st
import json
from src.langgraph_agentic_ai.ui.streamlitui.load_ui import LoadStreamlitUI
from src.langgraph_agentic_ai.LLMs.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder


def load_langgraph_agentic_ai_app():
    """Loads and runs the LangGraph AgenticAI application with Streamlit UI
    This function initializes the UI, handles user input, configures the LLM model, sets up the graph based
    on the selected use case, and displays the output while implementing exception handling for robustness"""
    load_ui = LoadStreamlitUI()
    user_input = load_ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return


# Text input for user message

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    elif st.session_state.IsSDLC :
        user_message = st.session_state.state
    else:
        user_message = st.chat_input("Enter your message:")
    
    
    
    if user_message:
        try:
            # Configure the LLM
            obj_llm_config = GroqLLM(user_controls_input = user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM could not be initialised")
                return
            
            # Initialise and set up the graph based use case
            
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: Use case not selected")
                return

            
            
            # Calling the graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return
        except Exception as e:
                raise ValueError(f'Error occurred while setting up graph: {e}')