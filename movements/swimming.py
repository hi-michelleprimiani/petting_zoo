class Swimming:

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print(f"{self} swims")

    def speed(self):
        print(f"{self} swims at {self.swim_speed}")
