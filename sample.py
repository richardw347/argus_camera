#!/usr/bin/env python3
import cv2
from argus_camera import ArgusCamera

camera = ArgusCamera()

for i in range(1,100):
  image = camera.read()
  cv2.imshow("vid", image)
  cv2.waitKey(1)
