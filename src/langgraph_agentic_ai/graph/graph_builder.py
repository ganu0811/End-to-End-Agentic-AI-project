from langgraph.graph import StateGraph, END, MessagesState, START
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder:
    
    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)
    
    
    def basic_chatbot_build_graph(self):
        """Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the BasicChatbotNode class
        and integrates it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.
        """
        self.basic_chatbot_node = BasicChatbotNode(self.model)
        
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot" )
        self.graph_builder.add_edge("chatbot", END)
        
    
    def setup_graph(self, usecase:str):
        """Sets up the graph for the selected use case

        Args:
            usecase (str): _description_
        """

        if usecase.lower() == 'basic chatbot':
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()
    
        
        