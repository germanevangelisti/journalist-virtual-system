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
        - Title: Provide a concise title summarizing the article.
        - Content: Extract the main content of the article, ensuring it is concise and readable.
        - Source: Use "Example Source" unless a different source is explicitly mentioned in the text.

        Article Text:
        {article}

        Please return the structured data in the exact format below:
        Title: <title>
        Content: <content>
        Source: <source>

        Ensure each field is clearly labeled and separated by a newline.
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
                "title": "",
                "content": "",
                "source": ""
            }
            for line in structured_lines:
                if line.startswith("Title:"):
                    structured_entry["title"] = line.replace("Title:", "").strip()
                elif line.startswith("Content:"):
                    structured_entry["content"] = line.replace("Content:", "").strip()
                elif line.startswith("Source:"):
                    structured_entry["source"] = line.replace("Source:", "").strip()
            
            structured_data.append(structured_entry)
        
        return structured_data

    except Exception as e:
        print(f"An error occurred while generating structured data: {e}")
        return []