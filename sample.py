#!/usr/bin/env python3
import cv2
from argus_camera import ArgusCamera

camera = ArgusCamera()

for i in range(1,1000):
  image = camera.read()
  bgr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  cv2.imshow("camera", bgr)
  cv2.waitKey(1)

