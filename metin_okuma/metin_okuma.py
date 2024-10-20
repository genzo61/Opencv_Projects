from PIL import Image
import pytesseract
img_to_str = pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\aliha\Downloads\\tesseract-ocr-w64-setup-5.3.0.20221222.exe"
img = Image.open("yazı.png")
result = pytesseract.image_to_string(img)

with open("text_result.txt",mode="w") as file:
    file.write(result)
    print("Ready !")