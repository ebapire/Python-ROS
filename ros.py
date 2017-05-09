import sys

class Message():
    def __init__(self, num, data):
        if num == 1:
            coor = Coordinates(data)
        else:
            raise ValueError()
        self.mess = [num, coor.x, coor.y, coor.z]


class Coordinates():
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]
