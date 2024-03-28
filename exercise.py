import cv2 as cv
import numpy as np

#Export image
def export(path, image):
    fileOutput = f"./{path}"
    cv.imwrite(fileOutput, image)
    print("Successful!")
    
#1a
list_color_range = {'Yellow':[(19,70,100), (35,255,255)],
                    'Orange':[(8,70,100), (15,255,255)],
                    'Pink': [(147,70,100), (170,255,255)],
                    'Blue':[(90,50,70), (128,255,255)],
                    'Green':[(36,50,70), (89,255,255)],
                    'Purple':[(129,50,70), (158,255,255)]
                    }
    
image = cv.imread("input1.jpg", cv.IMREAD_COLOR)
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

for color in list_color_range:
    mask = cv.inRange(hsv, list_color_range[color][0], list_color_range[color][1])
    output = cv.bitwise_and(image, image, mask = mask)
    kernel = np.ones((5,5), np.uint8)
    dst = cv.morphologyEx(output, cv.MORPH_OPEN, kernel)
    export(f'{color}.jpg', dst) 

#1b
image_GRAYSCALE = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_, temp1_image = cv.threshold(image_GRAYSCALE, 210, 255, cv.THRESH_BINARY_INV)
_, temp2_image = cv.threshold(image_GRAYSCALE, 145, 255, cv.THRESH_BINARY)
output = cv.bitwise_and(temp1_image, temp2_image)
kernel = np.ones((10,10), np.uint8)
opening = cv.morphologyEx(output, cv.MORPH_OPEN, kernel)
dst = cv.erode(opening,kernel,iterations = 0)
export("BlackColor.jpg", dst) 