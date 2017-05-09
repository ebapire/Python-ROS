import sys
import unittest
from ros import Coordinates

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
        self.assertEqual(expected_type, got[0])


if __name__ == '__main__':
    unittest.main()
