import matplotlib.pyplot as plt

def visualize_data(data):
    """
    Function to visualize data as a bar chart.

    Args:
        data (dict): A dictionary where keys are categories and values are frequencies.

    Returns:
        None
    """
    try:
        if not data:
            raise ValueError("Data is empty. Provide a dictionary with categories and frequencies.")
        
        categories = list(data.keys())
        frequencies = list(data.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(categories, frequencies)
        plt.xlabel('Categories')
        plt.ylabel('Frequency')
        plt.title('Data Visualization')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error occurred during visualization: {e}")