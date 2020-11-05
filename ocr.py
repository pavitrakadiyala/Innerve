from PIL import Image
#from tesserocr import PyTessBaseAPI, RIL
import cv2
import sys
import os
import numpy as np
import pytesseract
from pytesseract import Output
import logging
import numpy as np
import shutil
import base64
import requests
#./from natsort import natsorted, ns
import json
import time
from subprocess import Popen
import argparse
from textblob import TextBlob
def get_image_path():
	t=os.getcwd()+'/31.jpg'
	return t

# load the example image and convert it to grayscale
def change(path):
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# check to see if we should apply thresholding to preprocess the
	# image
	#if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	# make a check to see if median blurring should be done to remove
	# noise
	#elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.jpg".format(os.getpid())
	cv2.imwrite(filename, gray)
	#cv2.imshow("Image", image)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(Image.open(filename),lang="Devanagari")
	os.remove(filename)
	#print(text)
	tran=TextBlob(text)
	print("{0}".format(tran.translate(to='en')))
	# show the output images
	#cv2.imshow("Image", image)
	#cv2.imshow("Output", gray)
	#cv2.waitKey(0)
if(__name__=="__main__"):
	#print("Hello")
	t=get_image_path()
	#print(t)
	change(t)