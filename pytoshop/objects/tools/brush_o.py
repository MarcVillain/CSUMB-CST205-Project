from pytoshop.objects.tool_o import Tool


class Brush(Tool):

    def __init__(self, size=20, color=(0, 0, 0, 0), hardness=100, opacity=100):
        super().__init__()

        self.size = size
        self.color = color
        self.hardness = hardness
        self.opacity = opacity
