# https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

import cv2
import numpy as np

#image_path
img_path = "106.jpg"

#read image
img_raw = cv2.imread(img_path)

#select ROIs function
ROIs = cv2.selectROIs("Select Rois",img_raw)

#print rectangle points of selected roi
print(ROIs)
print(type(ROIs))

#Crop selected roi ffrom raw image

#counter to save image with different name
crop_number = 0 

#loop over every bounding box save in array "ROIs"
for rect in ROIs:
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    #crop roi from original image
    img_crop = img_raw[y1: y1 + y2, x1: x1 + x2]

    #show cropped image
    cv2.imshow("crop" + str(crop_number), img_crop)

    #save cropped image
    cv2.imwrite("crop" + str(crop_number) + ".jpg", img_crop)
        
    crop_number += 1

#hold window
cv2.waitKey(0)