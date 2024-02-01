import unittest
from game import Rifle, Shotgun, Deer, Bear, Player

class TestGame(unittest.TestCase):
    def test_rifle_shoot(self):
        rifle = Rifle()
        # Test by calling multiple times and check if it returns both True and False
        results = [rifle.shoot() for _ in range(10)]
        self.assertIn(True, results)
        self.assertIn(False, results)

    def test_shotgun_shoot(self):
        shotgun = Shotgun()
        results = [shotgun.shoot() for _ in range(10)]
        self.assertIn(True, results)
        self.assertIn(False, results)

    def test_animal_points(self):
        deer = Deer()
        bear = Bear()
        self.assertEqual(deer.points, 10)
        self.assertEqual(bear.points, 20)

    def test_player_shooting(self):
        player = Player(Rifle())
        deer = Deer()
        # Simulate shooting
        hit = player.shoot(deer)
        # Since shooting is random, we check if points are updated correctly when hit
        if hit:
            self.assertEqual(player.points, deer.points)
        else:
            self.assertEqual(player.points, 0)

# Run the tests
if __name__ == '__main__':
    unittest.main()
