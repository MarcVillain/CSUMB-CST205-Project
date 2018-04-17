from PyQt5.QtCore import Qt
import numpy as np
import cv2

class MainController:

    def __init__(self, view, drawing_board):
        self.view = view
        self.drawing_board = drawing_board
        self.command_pressed = False

    def onKeyPressed(self, event):
        if event.key() == Qt.Key_Control:
            self.command_pressed = True
            self.view.changeCursor(Qt.OpenHandCursor)

    def onKeyReleased(self, event):
        if event.key() == Qt.Key_Control:
            self.command_pressed = False
            self.view.changeCursor(Qt.ArrowCursor)
        
    def onMousePressed(self, event, drawing):
        if self.command_pressed:
            self.offset = event.pos()
            self.drawing_board_offset = self.drawing_board.pos()
            self.view.changeCursor(Qt.ClosedHandCursor)
        elif drawing:
            radius = 5
            color = (0, 0, 255)
            thickness = -1 # Fill
            draw(event.x(), event.y(), radius, color, thickness)

    def onMouseReleased(self, event):
    	if self.command_pressed:
            self.view.changeCursor(Qt.OpenHandCursor)

    def onMouseMove(self, event):
    	if self.command_pressed:
            x_g = event.globalX()
            y_g = event.globalY()
            x_l = self.drawing_board_offset.x()
            y_l = self.drawing_board_offset.y()
            x_o = self.offset.x()
            y_o = self.offset.y()
            x_s = self.view.x()
            y_s = self.view.y() + 22

            deltaX = x_g - x_s - x_o
            deltaY = y_g - y_s - y_o

            self.drawing_board.move(x_l + deltaX, y_l + deltaY)
        elif drawing:
            radius = 5
            color = (0, 0, 255)
            thickness = -1 # Fill
            draw(event.x(), event.y(), radius, color, thickness)

    def draw(self, event):
        if not self.command_pressed:
            cv2.circle(self.image,(event.x(),event.y()),5,(0,0,255),-1)

    def createImage(self, width, height, image_name=None):
        if image_name == None:
            self.image = cv2.cvtColor(np.full((height, width, 3), 255, np.uint8), cv2.COLOR_BGR2RGB)
        else:
            self.image = cv2.imread(image_name)