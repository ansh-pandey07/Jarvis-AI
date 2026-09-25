import requests
from PIL import Image
from io import BytesIO
import pytesseract

#url of the image to be fetched
url = input("Enter Url Of Image:-")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#fetch the image from the url
response = requests.get(url)
img = Image.open(BytesIO(response.content))
text = pytesseract.image_to_string(img)  #using pytesseract library to extract text from image 
print(text)