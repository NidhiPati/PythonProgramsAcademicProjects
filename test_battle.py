from unittest import TestCase
from TrekWars import Ship
from TrekWars import Alignment
from TrekWars import Battle


class TestBattle(TestCase):
    def test_init(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 2

        # Act
        ship = Battle(name, type_, x_location, y_location, align)

        # Assert
        self.assertEqual(10, ship._range)
        self.assertEqual(100, ship._max_health)
        self.assertEqual(10, ship._attack_power)
        self.assertEqual(10, ship._torpedoes)

    def test_move(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 4
        y_location = 2

        # Act
        ship = Battle(name, type_, x_location, y_location, align)
        ship.move()
        print(ship._x_location)
        print(ship._y_location)

        # Assert
        self.assertEqual(3, ship._x_location)
        self.assertEqual(1, ship._y_location)

    def test_attack_diff_alignment_in_range_check_torpedoes(self):
        # Arrange

        # Act
        ship = Battle('Nship', 'Battle', 3, 3, 'them')
        target = Ship('BattleEnemy', 'Battle', 0, 7, 'us')
        ship._current_health = 90
        ship._max_health = 100
        ship._torpedoes = 2
        target._current_health = 100
        target._max_health = 100
        print(ship._torpedoes)
        print(target._current_health)
        ship.attack(target)
        print(ship._torpedoes)
        print(target._current_health)

        # Assert
        self.assertEqual(1, ship._torpedoes)
        self.assertEqual(80, target._current_health)

    def test_attack_diff_alignment_in_range_zero_torpedoes(self):
        # Arrange

        # Act
        ship = Battle('Nship', 'Battle', 3, 3, 'them')
        target = Ship('BattleEnemy', 'Battle', 0, 7, 'us')
        ship._current_health = 90
        ship._max_health = 100
        ship._torpedoes = 0
        target._current_health = 100
        target._max_health = 100
        print(ship._torpedoes)
        print(target._current_health)
        ship.attack(target)
        print(ship._torpedoes)
        print(target._current_health)

        # Assert
        self.assertEqual(0, ship._torpedoes)
        self.assertEqual(90, target._current_health)

    def test_attack_chaotic_alignment_in_range(self):
        # Arrange

        # Act
        ship = Battle('Nship', 'Battle', 3, 3, 'chaotic')
        target = Ship('BattleEnemy', 'Battle', 0, 7, 'them')
        ship._current_health = 90
        ship._max_health = 100
        ship._torpedoes = 9
        target._current_health = 50
        target._max_health = 100
        print(ship._torpedoes)
        print(target._current_health)
        ship.attack(target)
        print(ship._torpedoes)
        print(target._current_health)

        # Assert
        self.assertEqual(8, ship._torpedoes)
        self.assertEqual(30, target._current_health)

    def test_attack_same_alignment_in_range(self):
        # Arrange

        # Act
        ship = Battle('Nship', 'Battle', 3, 3, 'them')
        target = Ship('BattleEnemy', 'Battle', 0, 7, 'them')
        ship._current_health = 90
        ship._max_health = 100
        ship._torpedoes = 9
        target._current_health = 100
        target._max_health = 100
        print(ship._torpedoes)
        print(target._current_health)
        ship.attack(target)
        print(ship._torpedoes)
        print(target._current_health)

        # Assert
        self.assertEqual(9, ship._torpedoes)
        self.assertEqual(100, target._current_health)

    def test_attack_diff_alignment_out_of_range(self):
        # Arrange

        # Act
        ship = Battle('Nship', 'Battle', 30, 30, 'them')
        target = Ship('BattleEnemy', 'Battle', 0, 7, 'us')
        ship._current_health = 90
        ship._max_health = 100
        ship._torpedoes = 8
        target._current_health = 80
        target._max_health = 100
        print(ship._torpedoes)
        print(target._current_health)
        ship.attack(target)
        print(ship._torpedoes)
        print(target._current_health)

        # Assert
        self.assertEqual(8, ship._torpedoes)
        self.assertEqual(80, target._current_health)

    def test_status(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 4

        # Act
        ship = Battle(name, type_, x_location, y_location, align)
        result = ship.status()
        print(result)

        # Assert
        self.assertEqual(str("Ship name: {},Ship type: {}, Current health: {},"
                             " Location: ({},{}), Torpedoes available: {}").format(name, type_, 0, x_location,
                                                          y_location, 10), result)


