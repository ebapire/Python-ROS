import sys

class Message():
    def __init__(self, num, data):
        if num == 1:
            coor = Coordinates(data)
            self.mess = [num, coor.x, coor.y, coor.z]
        else:
            raise ValueError()


class Coordinates():
    def __init__(self, data):
        self.x = data[0]
        self.y = data[1]
        self.z = data[2]

    def get(self):
        return [self.x, self.y, self.z]


class Robot():

    def __init__(self, news):
        self.mines = Coordinates([0,0,0])
        self.direcc = Coordinates(news)

    #as far a UR3 robot have 500mm of action
    def controller (self, nuls, direcc):
        if abs(direcc.x) < 500 :#&& abs(direcc.y) && abs(direcc.z):
            return True
        else:
            return False

    def changedirecc(self, news):
        self.direcc = Coordinates(news)
