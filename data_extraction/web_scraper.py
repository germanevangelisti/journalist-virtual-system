import requests
from bs4 import BeautifulSoup


def scrape_news(url):
    """
    Function to scrape news articles from a given URL.

    Args:
        url (str): The URL of the news website to scrape.

    Returns:
        list: A list of text content from all the articles found on the page, or an empty list if an error occurs.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article")
        
        return [article.text for article in articles]
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return []  # Return an empty list if an error occurs
