from langchain.prompts import PromptTemplate
from config.llm_manager import LLMManager

def generate_structured_data_with_langchain(cleaned_articles):
    """
    Function to generate structured data (title, content, source) from a list of cleaned articles using LangChain.

    Args:
        cleaned_articles (list of str): A list of cleaned article texts.

    Returns:
        list of dict: A list of structured dictionaries containing 'title', 'content', and 'source'.
    """
    try:
        # Get the LLM instance
        llm = LLMManager().get_llm()
        
        # Define the Prompt Template
        prompt_template = """
        You are a data extraction expert. For each given article text, extract the following structured information:
        - Title: A concise title summarizing the article.
        - Content: The main content of the article, keeping it concise and readable.
        - Source: Assume "Example Source" unless explicitly stated in the text.

        Article Text:
        {article}

        Structured Data:
        - Title:
        - Content:
        - Source:
        """
        prompt = PromptTemplate(
            input_variables=["article"],
            template=prompt_template
        )

        # Create the Runnable Sequence
        sequence = prompt | llm

        # Process each article and generate structured data
        structured_data = []
        for article in cleaned_articles:
            structured_response = sequence.invoke({"article": article})
            
            # Extract the text from the AIMessage object
            response_text = structured_response.content if hasattr(structured_response, 'content') else str(structured_response)
            
            # Parse response into a dictionary (simple parsing for this implementation)
            structured_lines = response_text.strip().split("\n")
            structured_entry = {
                "title": structured_lines[0].replace("Title: ", "").strip(),
                "content": structured_lines[1].replace("Content: ", "").strip(),
                "source": structured_lines[2].replace("Source: ", "").strip(),
            }
            structured_data.append(structured_entry)
        
        return structured_data

    except Exception as e:
        print(f"An error occurred while generating structured data: {e}")
        return []