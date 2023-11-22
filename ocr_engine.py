# importing the important libraries
import pytesseract
from PIL import Image
import os

class OCREngine:
    @staticmethod
    def extract_text(file_path):
        """
        1. Open the image file path using Image library
        2. Using Pytesseract library to extract text from the image
        3. return the text
        """
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            return str(e)
        
