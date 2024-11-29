def normalize_text_data(data):
    """
    Function to normalize structured text data by standardizing its format.

    Args:
        data (dict): A dictionary containing text data with keys as categories 
                     (e.g., 'title', 'content') and values as text.

    Returns:
        dict: A dictionary with normalized text data.
    """
    try:
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary.")
        
        # Normalize each value in the dictionary
        normalized_data = {key: value.strip().lower() for key, value in data.items()}
        return normalized_data
    except Exception as e:
        print(f"An error occurred during normalization: {e}")
        return {}