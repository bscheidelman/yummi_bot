#Somewhat sourced from https://www.geeksforgeeks.org/python-using-pil-imagegrab-and-pytesseract/
import numpy as nm
import pytesseract
import cv2 
from PIL import ImageGrab
from PIL import Image     

def grabText(left,upper,right,lower):
  
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    while(True):
        cap = ImageGrab.grab(bbox = (left,upper,right,lower))
        cap.show()
        
        tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang ='eng')
        break

    print(tesstr)
    li = tesstr.split('/')
    tli = []
    for val in li:
        temp = ""
        for oval in val:
            if oval == "\n":
                continue
            try:
                tmp = str(int(oval))
                temp += tmp
            except:
                temp += "0"
        if int(temp) == 0:
            temp = "1" + temp[1:len(temp)]
        print(temp)
        tli.append(temp)
        
    return tli
