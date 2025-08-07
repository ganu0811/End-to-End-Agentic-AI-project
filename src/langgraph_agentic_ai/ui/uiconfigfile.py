from configparser import ConfigParser


class Config:
    def __init__(self, config_file = "./src/langgraph_agentic_ai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)
        
    def get_llm_option(self): # This function is to only read about the LLM field from uiconfigfile.ini file
        llm_options = self.config["DEFAULT"].get("LLM_OPTIONS")
        return llm_options.split(", ") if llm_options else ["Groq"]
    
    def get_usecase_options(self):
        usecase_options = self.config['DEFAULT'].get("USECASE_OPTIONS")
        return usecase_options.split(", ") if usecase_options else ["Basic Chatbot"]
    
    def get_groq_model_options(self):
        groq_options = self.config['DEFAULT'].get("GROQ_MODEL_OPTIONS")
        return groq_options.split(", ") if groq_options else [" llama3-8b-8192"] 
    
    def get_page_title(self):
        page_title = self.config["DEFAULT"].get("PAGE_TITLE")
        return page_title if page_title else "Agentic AI Application" 
    
        