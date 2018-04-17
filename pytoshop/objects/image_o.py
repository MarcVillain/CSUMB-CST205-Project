import numpy as np
import cv2

class Image:

	def __init__(self, width, height, image_name=None):
		channels_count = 3

		if image_name == None:
			self.value = cv2.cvtColor(np.full((height, width, channels_count), 255, np.uint8), cv2.COLOR_BGR2RGB)
		else:
			self.value = imread(image_name)

		self.width = width
		self.height = height
		self.bytesPerLine = width * channels_count

	def draw(self, x, y, brush):
		cv2.circle(self.value, (x,y), brush.radius, brush.color, brush.thickness)