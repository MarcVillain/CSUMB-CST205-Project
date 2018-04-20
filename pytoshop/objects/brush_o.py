class Brush:
    
    def __init__(self, size=6, color=(0,0,0), hardness=0, opacity=100):
        self.size = size
        self.color = color
        self.hardness = hardness
        self.opacity = opacity

    def draw(self, image, x, y):
        pass