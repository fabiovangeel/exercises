class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.heigth = height
        self.width = width
        self.volume = depth * height * width
