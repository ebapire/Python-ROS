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

    def test_sendingmess(self):
        data = [1,1,1]
        got = Robot(data)
        mess = got.sendcoordinates()
        expected = Message(1, data)
        self.assertEqual(expected.get(), mess.get())

    def test_sendingmess2(self):
        data = [-600, -100, 4]
        got = Robot(data)
        mess = got.sendcoordinates()
        expected = [0]
        self.assertEqual(expected, mess.get())

    def test_update(self):
        data = [1,1,1]
        got = Robot(data)
        expected_origin = [0,0,0]
        self.assertEqual(expected_origin, got.mines.get())
        got.updatecoor()
        self.assertEqual(data, got.mines.get())

    def test_integrate(self):
        data_o = [1,1,1]
        robot = Robot(data_o)
        expected_origin = [0,0,0]
        self.assertEqual(expected_origin, robot.mines.get())
        self.assertEqual(data_o, robot.direcc.get())
        mess = robot.sendcoordinates()
        expected = Message(1, data_o)
        self.assertEqual(expected.get(), mess.get())
        robot.updatecoor()
        self.assertEqual(data_o, robot.mines.get())
        new_coor = [300, 3, -1]
        robot.changedirecc(new_coor)
        mess = robot.sendcoordinates()
        self.assertEqual(new_coor, robot.direcc.get())
        robot.updatecoor()
        self.assertEqual(new_coor, robot.mines.get())


if __name__ == '__main__':
    unittest.main()
