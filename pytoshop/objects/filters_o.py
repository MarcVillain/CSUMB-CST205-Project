import cv2
import numpy as np


def grayScaleFilter(layer):
    layer = cv2.applyColorMap(layer, cv2.COLORMAP_BONE)

def coolFilter(layer):
    layer = cv2.applyColorMap(layer, cv2.COLORMAP_OCEAN)

def warmFilter(layer):
    layer = cv2.applyColorMap(layer, cv2.COLORMAP_OCEAN)

def sepiaFilter(layer):
    layer = cv2.applyColorMap(layer, cv2.COLORMAP_PINK)

def negativeFilter(layer):
    layer = cv2.bitwise_not(layer)

def reduceNoise(layer):
    layer = cv2.bilateralFilter(layer, 9, 100, 100)

def blur(layer):
    layer = cv2.medianBlur(layer, 5)


