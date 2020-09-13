import pytesseract
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
def convert():
    img=Image.open('Anjali Agrawal.jpg')
    text=pytesseract.image_to_string(img)
    print(text)

convert()
