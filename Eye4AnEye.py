import pkg_resources
pkg_resources.require("numpy==1.14.6")
pkg_resources.require("opencv-python==4.3.0.38") #previous versions are required to run this program
import cv2
import numpy as np



class cataract:
   def __init__(self, myinput):
      self.myInput = myinput #declare the input
      self.img = cv2.resize(cv2.imread(self.myInput), (915,612)) #load the image and reduce it's size to 1/10 of a normal 1080p image

      self.newim = self.img[int(self.img.shape[1]/2) - 360:int(self.img.shape[1]/2) + 100, int(self.img.shape[0]/2) - 150:int(self.img.shape[0]/2) + 450] #crop the image so that the algorithm focuses more on the eye and not it's surroundings
      self.imgHSV = cv2.cvtColor(self.newim, cv2.COLOR_BGR2HSV) #convert the cropped image's colour scheme from BGR to HSV as it is easier to process

      h_min = 0 #minimum hue
      h_max = 227 #maximum hue
      s_min = 25 #minimum saturation
      s_max = 70 #maximum saturation
      v_min = 25 #minimum value aka brightness
      v_max = 255 #maximum value ...



      lower = np.array([h_min, s_min, v_min])
      upper = np.array([h_max, s_max, v_max])

      mask = cv2.inRange(self.imgHSV, lower, upper)
      self.imgResult = cv2.bitwise_and(self.newim, self.newim, mask=mask) #perform an array comparison

      self.img2 = cv2.cvtColor(self.imgResult, cv2.COLOR_HSV2RGB) #convert the cropped and processed image back to RGB
      #cv2.imshow("img2", self.img2)
      self.counter = 0 #declare pixel counter
   def CDetector(self):

      for i in range(self.newim.shape[0]): #these two loops iterate through every pixel on the cropped processed and converted image
         for j in range(self.newim.shape[1]):
            a = self.img2[i,j] #this variable is assigned as an array that holds the three BGR values of the pixel at p(i,j)

            if a[0] != 0 and a[1] != 0 and a[2] != 0: #check if the pixel is black
               if a[0] <= 100 and a[1] <= 100 and a[2] <= 100: #check if the pixel's colour is in range from 1-100
                  self.counter += 1 #incriment the pixel counter by 1 as we now know that it is part of the cataract
                  continue
               else:
                  #cv2.rectangle(self.img2, (i,j), (i+3,j+3), (255,0,0), 5) //ignore
                  continue
      #cv2.imwrite('images/newimg.png', self.img2, [cv2.IMWRITE_JPEG_QUALITY, 50]) //ignore
      return ((self.counter/276000) * 1000) #returns the ‰ of all cataract pixels in the picture instead of the % as it is easier to work with bigger numbers

class BloodInChamber:
   
   def __init__(self,myInput):
      self.myinput = myInput #declare input
      self.img = cv2.imread(self.myinput) #load image without resizing as now we are not going to convert our input
      self.counter = 0 #counts the amount of red (blood) pixels in our image

   def BDetector(self):
      
      for i in range(self.img.shape[0]): #these two loops iterate through every pixel on the cropped processed and converted image
         for j in range(self.img.shape[1]):
            a = self.img[i, j] #this variable is assigned as an array that holds the three BGR values of the pixel at p(i,j)

            if a[2] >= 20 and a[0] <= 30 and a[1] <= 20: #check whether or not the said pixel p(i,j) is red
               self.counter += 1
               #print(self.img[i, j], "cords", str(i), str(j)) //ignore
               continue
      return ((self.counter / (self.img.shape[0] * self.img.shape[1])) * 1000) #returns the ‰ of all red identified pixels in the picture instead of the % as it is easier to work with bigger numbers

