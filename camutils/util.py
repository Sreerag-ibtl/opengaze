import cv2
import string

def getCamera(src):
    src = formatSource(src)
    return cv2.VideoCapture(src)

def formatSource(src):
    if (src in string.digits) and (len(src)==1):
        return int(src)
    else:
        return src
        
    
