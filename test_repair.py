from unittest import TestCase
from TrekWars import Repair
from TrekWars import Battle


class TestRepair(TestCase):
    def test_attack_same_alignment_in_range(self):
        # Arrange

        # Act
        ship = Repair('Nship', 'Repair', 4, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'us')
        target._current_health = 50
        target._max_health = 100
        ship.attack(target)
        print(ship._align)
        print(target._align)
        print(target._current_health)
        print(target._max_health)

        # Assert
        self.assertEqual(ship._align, target._align)
        self.assertEqual(target._current_health, target._max_health)

    def test_attack_diff_alignment_in_range(self):
        # Arrange

        # Act
        ship = Repair('Nship', 'Repair', 4, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        target._current_health = 50
        target._max_health = 100
        ship.attack(target)
        print(ship._align)
        print(target._align)
        print(target._current_health)
        print(target._max_health)

        # Assert
        self.assertNotEqual(ship._align, target._align)
        self.assertNotEqual(target._current_health, target._max_health)

    def test_attack_same_alignment_and_not_in_range(self):
        # Arrange

        # Act
        ship = Repair('Nship', 'Repair', 40, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 70, 'us')
        target._current_health = 50
        target._max_health = 100
        ship.attack(target)
        print(target._current_health)
        print(target._max_health)

        # Assert
        self.assertNotEqual(target._current_health, target._max_health)

