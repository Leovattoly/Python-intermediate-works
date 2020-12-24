#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Open a picture in OpenCV

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
  
img = cv2.imread('opencv_image.jpg',cv2.IMREAD_UNCHANGED )
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[19]:


# Access pixel values and modify them
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img = cv2.imread('opencv_image.jpg',cv2.IMREAD_UNCHANGED )
print("Pixel Values before modification: " ,img[519,519])
# modifying Pixel values

img[519,519] = [255,255,255]
print("Pixel Values After modification: " ,img[519,519])


# In[21]:


#  Access image properties
print ("Shape of image:",img.shape)
print ("Size of image: ",img.size)


# In[30]:


# Setting Region of Image (ROI)
bridge = img[280:340, 330:390]
img[273:333, 100:160] = bridge
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[32]:


# Splitting and Merging images 

b,g,r = cv2.split(img)
print("Blue:",b)
print("Green:",g)
print("Red:",r)
img = cv2.merge((b,g,r))


# In[2]:


# Read video, Display video, and Save video. 

import numpy as np
import cv2

cap = cv2.VideoCapture('vdo.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:


# Capture video from a camera and Display it by using cv.VideoCapture(), cv.VideoWriter() Functions.

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

