from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tool = TavilySearchResults(max_results = 5)
    
    return [tool]
    
    
def create_tool_node(tool):
    
    """
    Create a ToolNode from the given tool.
    
    """
    return ToolNode(tools = tool)

