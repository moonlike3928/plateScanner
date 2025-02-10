import cv2
import pytesseract

def recognize_plate(plate_img):
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 8 --oem 3')
    return text.strip()
