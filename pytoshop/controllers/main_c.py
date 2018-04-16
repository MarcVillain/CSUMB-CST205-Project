from PyQt5.QtCore import Qt

class MainController:

    def __init__(self, view):
        self.view = view
        self.command_pressed = False

    def onKeyPressed(self, event):
        if event.key() == Qt.Key_Control:
            self.command_pressed = True
            self.view.changeCursor(Qt.OpenHandCursor)

    def onKeyReleased(self, event):
        if event.key() == Qt.Key_Control:
            self.command_pressed = False
            self.view.changeCursor(Qt.ArrowCursor)
        
    def onMousePressed(self, event):
        if self.command_pressed:
            self.offset = event.pos()
            self.workspaceOffset = self.view.workspace.pos()
            self.view.changeCursor(Qt.ClosedHandCursor)

    def onMouseReleased(self, event):
    	if self.command_pressed:
            self.view.changeCursor(Qt.OpenHandCursor)

    def onMouseMove(self, event):
    	if self.command_pressed:
            x_g = event.globalX()
            y_g = event.globalY()
            x_l = self.workspaceOffset.x()
            y_l = self.workspaceOffset.y()
            x_o = self.offset.x()
            y_o = self.offset.y()
            x_s = self.view.x()
            y_s = self.view.y() + 22

            deltaX = x_g - x_s - x_o
            deltaY = y_g - y_s - y_o

            self.view.workspace.move(x_l + deltaX, y_l + deltaY)