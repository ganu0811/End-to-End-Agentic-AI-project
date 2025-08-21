import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class DisplayResults:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_results_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == 'Basic Chatbot':
            for event in graph.stream({'messages': [HumanMessage(content=user_message)]}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        # Handle the case where messages is a list
                        messages = value['messages']
                        if isinstance(messages, list) and len(messages) > 0:
                            # Get the last message from the list
                            last_message = messages[-1]
                            st.write(last_message.content)
                        else:
                            # Handle single message case
                            st.write(messages.content)
    
        elif usecase == 'Chatbot with Tool':
            initial_state = {"messages": [HumanMessage(content=user_message)]}
            res = graph.invoke(initial_state)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message)== ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write('Tool Call End')
                elif type(message)== AIMessage and message.content:
                    
                    with st.chat_message("assistant"):
                        st.write(message.content)
        
                