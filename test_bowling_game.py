# -*- coding: utf-8 -*- #
"""TDD Function using the UnitTest Framework."""
import unittest

from bowling_game import BowlingGame


class BowlingGameTest(unittest.TestCase):
    """Main Class."""

    def setUp(self):
        """Create the Instance of the Game class."""
        self.game = BowlingGame()

    def test_gutter_game(self):
        """Test all missed."""
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())
        self.game.scoresheet()
        self.game.scoresheet()

    def test_all_ones(self):
        """Test 20 one in a row."""
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score())
        self.game.scoresheet()

    def test_one_spare(self):
        """Test only one Spare."""
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.total_score())
        self.game.scoresheet()

    def test_one_strike(self):
        """Test Only one Strike."""
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.total_score())
        self.game.scoresheet()

    def test_perfect_game(self):
        """Test 12 strike in a row."""
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.total_score())
        self.game.scoresheet()

    def test_simple_game(self):
        """Test Random Game with Stike, Spare."""
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 7]:
            self.game.roll(pins)
        self.assertEqual(125, self.game.total_score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)


if __name__ == '__main__':
    unittest.main()
