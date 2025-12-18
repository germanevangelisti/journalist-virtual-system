import re

def clean_text(text):
    """
    Function to clean and preprocess text.

    Args:
        text (str): The raw text to clean.

    Returns:
        str: The cleaned text.
    """
    try:
        # Convert text to lowercase
        text = text.lower()
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        # Remove non-alphanumeric characters (except spaces and punctuation)
        text = re.sub(r'[^a-zA-Z0-9\s.,;:!?\'"-]', '', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    except Exception as e:
        print(f"An error occurred during text cleaning: {e}")
        return ""