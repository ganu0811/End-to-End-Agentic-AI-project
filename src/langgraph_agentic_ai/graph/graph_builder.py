from langgraph.graph import StateGraph, END, MessagesState, START
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.prompts import ChatPromptTemplate
import datetime
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agentic_ai.tools.search_tool import get_tools, create_tool_node
from src.langgraph_agentic_ai.nodes.chatbot_with_toolnode import ChatBotwithToolNode


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
    
    
    def chatbot_with_tools_build_graph(self):
        """Builds a chatbot graph with tool integration using LangGraph.
        This method initializes a chatbot node using the ChatBotwithToolNode class
        and integrates it into the graph. The chatbot node is set as both the
        entry and exit point of the graph.
        """
        # Define the tool and tool node
        
        tools = get_tools()
        tool_node = create_tool_node(tools)
        
        # Define llm 
        
        llm = self.model
        
        # Define the chatbot node
        
        obj_chatbot_with_node = ChatBotwithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        
        # Add nodes
        
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)
        
        # Adding Conditional eges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition,
            {"tools": "tools", END: END}
        )
        # self.graph_builder.add_edge("tools", "chatbot") If we want the tool response to go back to LLM
        
        
    
    def setup_graph(self, usecase:str):
        """Sets up the graph for the selected use case

        Args:
            usecase (str): _description_
        """

        if usecase.lower() == 'basic chatbot':
            self.basic_chatbot_build_graph()
        
        if usecase.lower() == 'chatbot with tool':
            self.chatbot_with_tools_build_graph()
        
        return self.graph_builder.compile()
    

        