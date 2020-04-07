#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cv2
import numpy as np
#image = cv2.imread(r'C:\Users\datta\Desktop\tfidf\train\slide\intro_to_prog_cyc000278.png') # reading the image
path=input('Give Path')
image = cv2.imread(path)
#image = cv2.imread(r'C:\Users\datta\Desktop\tfidf\videos\Historical Perspective of development of remote sensing technology\hist_persp_000234.png')
#image = cv2.imread(r'C:\Users\datta\Desktop\tfidf\a.jpg') # reading the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert2grayscale
(thresh, binary) = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # convert2binary


# In[15]:


from typing import List
minLineLength = 100
maxLineGap = 50
def lines_extraction(gray: List[int]) -> List[int]:
    """
    this function extracts the lines from the binary image. Cleaning process.
    """
    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
    return lines
mask = np.ones(image.shape[:2], dtype="uint8") * 255 # create a white image
lines = lines_extraction(gray) # extract lines
try:
    for line in lines: # write lines to mask
        x1, y1, x2, y2 = line[0]
        cv2.line(mask, (x1, y1), (x2, y2), (0, 255, 0), 3)
except TypeError:
    pass
( contours, _) = cv2.findContours(~binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # find contours
areas = [cv2.contourArea(c) for c in contours] # find area of contour
avgArea = sum(areas)/len(areas) # finding average area
for c in contours:# average area heuristics
    if cv2.contourArea(c)>60*avgArea:
        cv2.drawContours(mask, [c], -1, 0, -1)
binary = cv2.bitwise_and(binary, binary, mask=mask) # subtracting the noise


# In[16]:


binary = binary[0:int(image.shape[0]*0.25), 0:image.shape[1]]


# In[17]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\datta\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image
from pytesseract import image_to_string
from pytesseract import Output
d = pytesseract.image_to_data(binary, output_type=Output.DICT)


# In[18]:


att=0
ait=[]
c=0
for i in range(len(d['height'])):
    k=d['height'][i]
    if(d['conf'][i]!='-1'):
        ait.append(i)
        att=att+k
        c=c+1
att=att/c
ne=[]
for i in ait:
    k=d['text'][i]
    if(k=="" or k==" " or d['height'][i]>2*att):
        continue
    else:
        ne.append(i)


# In[19]:


bot=d['top'][ne[0]]+d['height'][ne[0]]
for n in ne:
    if(d['top'][n]<bot):
        print(d['text'][n],end=" ")

