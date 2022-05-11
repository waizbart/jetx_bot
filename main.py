import pyautogui
import cv2
import pytesseract
import pyscreenshot as pys
from time import sleep
import os
import numpy as np
import csv
from datetime import datetime

file = open('valores.csv', 'w', newline='', encoding='utf-8')

w = csv.writer(file)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

sleep(3)


last_number = 0

# while pyautogui.locateOnScreen('logo.png') != None:
while True:

    img = pys.grab(bbox=(70, 600, 240, 690))
    img.save('screenshot.png')
    img = cv2.imread('screenshot.png')

    gray = get_grayscale(img)
    gray = thresholding(gray)
    gray = remove_noise(gray)

    caminho = r"C:\Program Files\Tesseract-OCR"
    pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
    texto = pytesseract.image_to_string(gray)
    formatTxt = float(texto.replace('\n', '').replace(' ', ''))

    if formatTxt != '' and formatTxt != last_number:
        w.writerow([datetime.now(), formatTxt])
        print(formatTxt)

    last_number = formatTxt

    os.remove('screenshot.png')
    file.close()
    sleep(5)

