from langchain_core.prompts import PromptTemplate
from config.llm_manager import LLMManager

def adapt_script_with_langchain(script):
    """
    Function to adapt a news script for virtual avatar presentation using LangChain.

    Args:
        script (str): The original news script.

    Returns:
        str: The adapted script with pauses and emphasis.
    """
    try:
        # Get the LLM instance
        llm = LLMManager().get_llm()
        
        # Define the Prompt Template
        prompt_template = """
        You are a virtual script editor for a news avatar. Adapt the following news script for effective presentation:
        - Insert pauses where appropriate.
        - Emphasize key phrases (e.g., breaking news, critical updates).
        - Ensure the script flows naturally for a virtual avatar's delivery.
        
        Original Script:
        {script}
        
        Adapted Script:
        """
        prompt = PromptTemplate(
            input_variables=["script"],
            template=prompt_template
        )

        # Create the Runnable Sequence
        sequence = prompt | llm

        # Run the adaptation process
        adapted_script = sequence.invoke({"script": script})
        return adapted_script

    except Exception as e:
        print(f"An error occurred while adapting the script: {e}")
        return "Unable to adapt the script for avatar presentation."