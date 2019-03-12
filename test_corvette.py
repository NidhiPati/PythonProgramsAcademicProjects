from unittest import TestCase
from TrekWars import Corvette
from TrekWars import Battle


class TestCorvette(TestCase):
    def test_move(self):
        # Arrange

        # Act
        ship = Corvette('Nship', 'Corvette', 4, -2, 'us')
        ship.move()
        print(ship._x_location)
        print(ship._y_location)

        # Assert
        self.assertEqual(9, ship._x_location)
        self.assertEqual(3, ship._y_location)

    def test_attack_same_alignment_in_range(self):
        # Arrange

        # Act
        ship = Corvette('Nship', 'Corvette', 4, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'us')
        ship.attack(target)
        print(ship._align)
        print(target._align)

        # Assert
        self.assertEqual(ship._align, target._align)

    def test_attack_diff_alignment_in_range(self):
        # Arrange

        # Act
        ship = Corvette('Nship', 'Corvette', 4, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        ship.attack(target)
        print(ship._align)
        print(target._align)

        # Assert
        self.assertEqual(ship._align, target._align)

    def test_attack_diff_alignment_and_not_in_range(self):
        # Arrange

        # Act
        ship = Corvette('Nship', 'Corvette', 40, -2, 'us')
        target = Battle('BattleEnemy', 'Battle', 0, 70, 'them')
        ship.attack(target)
        print(ship._align)
        print(target._align)

        # Assert
        self.assertEqual('them', target._align)
