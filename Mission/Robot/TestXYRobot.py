import unittest
import XYRobot as r


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.t = r.XYRobot("Bot")

    def test_init(self):
        self.assertEqual(self.t.getnom(), "Bot", "Your robot doesn't have the right name")
        self.assertEqual(self.t.getangle(), 0,     "Your Robot is not facing EAST as expected")
        self.assertEqual(self.t.position(), (0,0), "Your Robot is not in 0,0 as expected")

    def test_turnleft(self):
        expected_position = self.t.position()
        # because of system axis we have to do -90
        expected_angle = (self.t.getangle() - 90) % 360
        self.t.turnleft()
        # below we are using assertAlmostEqual instead if assertEqual to allow for inaccurate calculations
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your robot took a wrong turn or did not update its angle while turning left")
        self.assertEqual(self.t.position(), expected_position, "Your robot changed position while turning left")

    def test_turnright(self):
        expected_position = self.t.position()
        expected_angle = (self.t.getangle() + 90) % 360
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your robot took a wrong turn or did not update its angle while turning right")
        self.assertEqual(self.t.position(), expected_position, "Your Robot changed position while turning right")

    def test_turn(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.turnleft()
        self.t.turnleft()
        self.t.turnright()
        self.t.turnright()
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your Robot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position, "Your Robot changed position while turning")


    def test_moveforward(self):
        forward = 50
        x, y = self.t.position()
        expected_position = (x + forward, 0 + y)
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your Robot has not moved forward " + str(forward) + " as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle, msg="Your Robot changed heading while moving forward")


    def test_movebackward(self):
        backward = 50
        x, y = self.t.position()
        expected_position = (x - backward, y - 0)
        expected_angle = self.t.getangle()
        self.t.movebackward(50)
        self.assertEqual(self.t.position(), expected_position,
                         "Your Robot has not moved backward " + str(backward) + " as expected")
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your Robot changed heading while moving backward")


    def test_move(self):
        expected_position = self.t.position()
        expected_angle = self.t.getangle()
        self.t.moveforward(50)
        self.t.movebackward(10)
        self.t.movebackward(90)
        self.t.moveforward(50)
        self.assertAlmostEqual(self.t.getangle(), expected_angle,
                               msg="Your Robot took a wrong turn or did not update its angle")
        self.assertEqual(self.t.position(), expected_position, "Your Robot changed position while turning")