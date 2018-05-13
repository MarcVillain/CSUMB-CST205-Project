import cv2


class FiltersUtil:

    def grayScale(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_BONE)

    def cool(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_OCEAN)

    def warm(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_OCEAN)

    def sepia(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_PINK)

    def negative(rgb):
        return cv2.bitwise_not(rgb)

    def reduceNoise(rgb):
        return cv2.bilateralFilter(rgb, 9, 100, 100)

    def blur(rgb):
        return cv2.medianBlur(rgb, 5)