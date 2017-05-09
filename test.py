import sys
import unittest
from ros import Coordinates, Message, Robot

class RosTest(unittest.TestCase):
    def test_newcoordinates(self):
        data = [1,1,1]
        expected = 1
        got = Coordinates(data)
        self.assertEqual(expected, got.x)
        self.assertEqual(expected, got.y)
        self.assertEqual(expected, got.z)

    def test_newmessage(self):
        data = [1,1,1]
        expected_coor = 1
        expected_type = 1
        got = Message(1, data)
        self.assertEqual(expected_type, got.mess[0])
        self.assertEqual(expected_coor, got.mess[1])
        self.assertEqual(expected_coor, got.mess[2])
        self.assertEqual(expected_coor, got.mess[3])

    def test_newrobot(self):
        data = [1,1,1]
        got = Robot(data)
        self.assertEqual([0,0,0], got.mines.get())

    def test_changedirecc(self):
        data = [1,1,1]
        got = Robot(data)
        new = [2,2,2]
        got.changedirecc(new)
        self.assertEqual(new, got.direcc.get())

    def test_direcOK(self):
        data = [1,1,1]
        expected = True
        got = Robot(data)
        self.assertEqual(expected, got.controller())

    def test_direcOK2(self):
        data = [-4, -100, 4]
        expected = True
        got = Robot(data)
        self.assertEqual(expected, got.controller())

    def test_direcnotOk(self):
        data = [-600, -100, 4]
        expected = False
        got = Robot(data)
        self.assertEqual(expected, got.controller())

if __name__ == '__main__':
    unittest.main()
