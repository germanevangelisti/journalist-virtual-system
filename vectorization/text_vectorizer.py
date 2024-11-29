from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(corpus):
    """
    Function to vectorize a list of text documents using TF-IDF.

    Args:
        corpus (list of str): A list of text documents.

    Returns:
        tuple: (vectorized_data, feature_names)
            - vectorized_data: Sparse matrix of TF-IDF scores.
            - feature_names: List of feature names corresponding to the TF-IDF scores.
    """
    try:
        # Initialize the TF-IDF Vectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
        
        # Fit and transform the corpus
        vectorized_data = vectorizer.fit_transform(corpus)
        
        # Get the feature names (words)
        feature_names = vectorizer.get_feature_names_out()
        
        return vectorized_data, feature_names
    except Exception as e:
        print(f"An error occurred during vectorization: {e}")
        return None, []