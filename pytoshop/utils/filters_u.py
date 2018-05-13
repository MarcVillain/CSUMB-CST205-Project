import cv2


class FiltersUtil:

    def grayScaleFilter(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_BONE)

    def coolFilter(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_OCEAN)

    def warmFilter(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_OCEAN)

    def sepiaFilter(rgb):
        return cv2.applyColorMap(rgb, cv2.COLORMAP_PINK)

    def negativeFilter(rgb):
        return cv2.bitwise_not(rgb)

    def reduceNoise(rgb):
        return cv2.bilateralFilter(rgb, 9, 100, 100)

    def blur(rgb):
        return cv2.medianBlur(rgb, 5)