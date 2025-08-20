from src.langgraph_agentic_ai.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot logic implementation
    """
    
    def __init__(self, model):
        self.llm = model
    
    
    def process(self, state: State) -> dict:
        """Process the input state and generates chatbot responses"""
        response = self.llm.invoke(state['messages'])
        return {"messages": [response]}
        