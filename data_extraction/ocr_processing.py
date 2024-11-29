import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    """
    Function to extract text from an image using OCR.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: The extracted text from the image.
    """
    try:
        image = Image.open(image_path)
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"An error occurred while processing the image: {e}"