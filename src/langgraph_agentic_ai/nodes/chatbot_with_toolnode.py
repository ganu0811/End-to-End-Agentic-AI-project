from src.langgraph_agentic_ai.state.state import State


class ChatBotwithToolNode:
    
    def __init__(self, model):
        
        
        self.model = model
    
    def process(self, state:State) -> dict:

        """
        Process the input state and generates a response with tool integreation.
        """
        
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.model.invoke([{"role": "user", "content": user_input}])
        
        # Simulate the tool-specifi logic:
        
        tools_response = f"Tool integration for: {user_input}"

        return {"messages": [llm_response, tools_response]}

    def create_chatbot(self, tools):
        """Returns a chatbot node function"""
        llm_with_tools = self.model.bind_tools(tools)
        
        def chatbot_node(state: State):
            """Chatbot logic for processing the input and returning a response"""
            messages = state["messages"]
            try:
                response = llm_with_tools.invoke(messages)
                return {"messages": [response]}
            except Exception as e:
                # Fallback to regular model if tool binding fails
                print(f"Tool binding error: {e}")
                response = self.model.invoke(messages)
                return {"messages": [response]}

        return chatbot_node
    
    # def create_chatbot(self, state, tools):
    #     llm_with_tools = self.llm.bind_tools(tools)
    #     return {"messages": [llm_with_tools.invoke(state["messages"])]}

    # return create_chatbot
    
    