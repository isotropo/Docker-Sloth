#!/usr/bin/env python

import cv2
import time
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
print("specify file name, then filetype")
name = input('name: ')
filetype = input('filetype: ')

# Locates the file to be processed after the name and file-extension (filetype) have been specified
cap = cv2.VideoCapture('/home/videos/'+name+'.'+filetype)

# Displays the FPS to the user and allows the user to specify the interval of image capture.
fps = cap.get(cv2.CAP_PROP_FPS)

print("Frames Per Second: "+str(fps))

interval = input("Specify the interval of image capture (in frames): ")

# Check if camera opened successfully
if(not cap.isOpened()):
  print("Error opening video stream or file")
  quit()

frameNum = 0
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  # if ret is true
  if(ret):
    # Only frames that are multiples of 30 are written to an image
    if(frameNum % round(fps/float(interval)) == 0):
      imgName = '/data/'+name+str(frameNum)+'.jpg'
      cv2.imwrite(imgName, frame)

    frameNum += 1
  else:
    break

# When everything done, release the video capture object
cap.release()