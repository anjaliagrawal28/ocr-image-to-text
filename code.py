import pytesseract
import os
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
def convert():
    img=Image.open('IMG-20181007-WA0060.jpg')
    text=pytesseract.image_to_string(img)
    print(text)

convert()
