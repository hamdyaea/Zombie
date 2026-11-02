# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from ZombieTextGame import Adventure

class ZombieTests(unittest.TestCase):
    def test_win_path(self):
        game = Adventure()
        for action in ("west", "north", "gun", "east", "escape"):
            game.move(action)
        self.assertEqual(game.room, "safe")
        self.assertTrue(game.finished)
    def test_dead_end(self):
        game = Adventure()
        game.move("east")
        self.assertEqual(game.room, "dead")
        self.assertTrue(game.finished)
    def test_invalid_does_not_move(self):
        game = Adventure()
        game.move("unknown")
        self.assertEqual(game.room, "start")
    def test_finished_immutable(self):
        game = Adventure(room="dead", finished=True)
        game.move("west")
        self.assertEqual(game.room, "dead")

if __name__ == "__main__":
    unittest.main()
