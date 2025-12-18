from langchain_core.prompts import PromptTemplate
from config.llm_manager import LLMManager

def create_script_with_langchain(data, tone="neutral", ideology="neutral"):
    """
    Function to create a news script using LangChain, based on input data, tone, and ideology.

    Args:
        data (dict): A dictionary containing structured news data (e.g., 'title', 'content', 'source').
        tone (str): The tone of the script (e.g., 'formal', 'casual', 'neutral').
        ideology (str): The ideological perspective for the script (e.g., 'progressive', 'conservative', 'neutral').

    Returns:
        str: The generated news script.
    """
    try:
        # Get the LLM instance
        llm = LLMManager().get_llm()
        
        # Define the Prompt Template
        prompt_template = """
        You are a virtual journalist with the following characteristics:
        - Tone: {tone}
        - Ideology: {ideology}
        
        Using the provided news data, generate a professional news script. 
        Make the script engaging and relevant to the target audience.
        
        News Data:
        Title: {title}
        Content: {content}
        Source: {source}
        
        Script:
        """
        prompt = PromptTemplate(
            input_variables=["tone", "ideology", "title", "content", "source"],
            template=prompt_template
        )

        # Create the Runnable Sequence
        sequence = prompt | llm

        # Input Data for the Sequence
        input_data = {
            "tone": tone,
            "ideology": ideology,
            "title": data.get("title", "No Title Available"),
            "content": data.get("content", "No Content Available"),
            "source": data.get("source", "Unknown Source"),
        }

        # Generate the Script
        script = sequence.invoke(input_data)
        return script

    except Exception as e:
        print(f"An error occurred while creating the script: {e}")
        return "Unable to generate script."