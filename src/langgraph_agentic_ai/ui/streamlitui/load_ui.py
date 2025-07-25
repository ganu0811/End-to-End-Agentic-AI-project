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