from unittest import TestCase
from TrekWars import Cruiser
from TrekWars import Battle


class TestCruiser(TestCase):
    def test_move(self):
        # Arrange

        # Act
        ship = Cruiser('Nship', 'Cruiser', 4, 0, 'us')
        ship.move()
        print(ship._x_location)
        print(ship._y_location)

        # Assert
        self.assertEqual(5, ship._x_location)
        self.assertEqual(2, ship._y_location)

    def test_attack_same_alignment_in_range(self):
        # Arrange

        # Act
        ship = Cruiser('Nship', 'Cruiser', 4, 0, 'them')
        ship._max_health = 100
        ship._current_health = 90
        ship._attack_power = 10
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        target._current_health = 50
        ship.attack(target)
        print(target._current_health)
        print(ship._current_health)

        # Assert
        self.assertEqual(50, target._current_health)

    def test_attack_diff_alignment_and_not_in_range(self):
        # Arrange

        # Act
        ship = Cruiser('Nship', 'Cruiser', 4, 0, 'us')
        ship._max_health = 100
        ship._current_health = 90
        ship._attack_power = 10
        target = Battle('BattleEnemy', 'Battle', 0, 70, 'them')
        target._current_health = 50
        ship.attack(target)
        print(target._current_health)
        print(ship._current_health)

        # Assert
        self.assertEqual(50, target._current_health)

    def test_attack_chaotic_alignment_and_in_range(self):
        # Arrange

        # Act
        ship = Cruiser('Nship', 'Cruiser', 4, 6, 'chaotic')
        ship._max_health = 100
        ship._current_health = 90
        ship._attack_power = 10
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        target._current_health = 50
        ship.attack(target)
        print(target._current_health)
        print(ship._current_health)

        # Assert
        self.assertEqual(50, target._current_health)
