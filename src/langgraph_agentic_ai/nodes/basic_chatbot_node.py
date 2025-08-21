from src.langgraph_agentic_ai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """
    
    def __init__(self, model):
        self.model = model
    
    
    def process(self, state: State) -> dict:
        """Process the input state and generates chatbot responses"""
        response = self.model.invoke(state['messages'])
        return {"messages": [response]}
        