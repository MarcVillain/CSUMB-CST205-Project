import numpy as np
import cv2

class Image:

	def __init__(self, width, height, image_name=None):
		channels_count = 3

		if image_name == None:
			self.value = np.full((height, width, channels_count), 255, np.uint8)
			print(self.value)
		else:
			self.value = imread(image_name)

		self.width = width
		self.height = height
		self.bytesPerLine = width * channels_count

	def draw(self, brush, xTo, yTo, xFrom=None, yFrom=None):
		if xFrom == None or yFrom == None:
			cv2.circle(self.value, (xTo,yTo), brush.radius, brush.color, brush.thickness)
		else:
			cv2.line(self.value, (xFrom,yFrom), (xTo,yTo), brush.color, brush.radius*2)