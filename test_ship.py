from unittest import TestCase
from TrekWars import Alignment
from TrekWars import Ship
from TrekWars import Battle
from TrekWars import Cruiser


class TestShip(TestCase):
    def test_init(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        print(ship.status())

        # Assert
        self.assertEqual(name, ship._name)
        self.assertEqual(type_, ship._type)
        self.assertEqual(align, ship._align)
        self.assertEqual(x_location, ship._x_location)
        self.assertEqual(y_location, ship._y_location)

    def test_get_type(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        result = ship.get_type()
        print(result)

        # Assert
        self.assertEqual(type_, result)

    def test_get_x_location(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        result = ship.get_x_location()
        print(result)

        # Assert
        self.assertEqual(x_location, result)

    def test_get_y_location(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 4

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        result = ship.get_y_location()
        print(result)

        # Assert
        self.assertEqual(y_location, result)

    def test_get_alignment(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        result = ship.get_alignment()
        print(result)

        # Assert
        self.assertEqual(align, result)

    def test_get_alignment_incorrect_align_name(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'Use'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)

        # Assert
        try:
            result = ship.get_alignment()
            print(result)
        except ValueError:
            print("Pass")
            self.assertTrue(True)

    def test_status(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = Alignment.us
        x_location = 2
        y_location = 4

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        result = ship.status()
        print(result)

        # Assert
        self.assertEqual(str("Ship name: {},Ship type: {}, Current health: {},"
                             " Location ({},{}) ").format(name, type_, 0, x_location,
                                                          y_location), result)

    def test_move_current_health_is_less(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._max_health = 100
        ship._current_health = 90
        ship.move()
        print(ship._current_health)

        # Assert
        self.assertNotEqual(90, ship._current_health)  # 90 and 91 won't be equal

    def test_move_current_health_is_max(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._max_health = 100
        ship._current_health = 100
        ship.move()
        print(ship._current_health)

        # Assert
        self.assertEqual(100, ship._current_health)  # current health = max health - so equal

    def test_change_alignment_us_to_them(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship.change_alignment()
        print(ship._align)

        # Assert
        self.assertNotEqual(align, ship._align)  # wont be equal because alignment is changed

    def test_change_alignment_them_to_us(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 2
        y_location = 2

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship.change_alignment()
        print(ship._align)

        # Assert
        self.assertNotEqual(align, ship._align)

    def test_assess_damage_max_health_minus_damage(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 2
        y_location = 2
        amount_of_damage = -10

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._current_health = 70
        ship._max_health = 100

        ship.assess_damage(amount_of_damage)

        # Assert
        self.assertEqual(70 - 10, ship._current_health)

    def test_assess_damage_current_health_zero_ship_destroyed(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 2
        y_location = 2
        amount_of_damage = -10

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._current_health = 0
        ship._max_health = 100

        ship.assess_damage(amount_of_damage)

        # Assert
        self.assertEqual(0, ship._current_health)

    def test_assess_damage_current_health_zero_repaired(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 2
        y_location = 2
        amount_of_damage = 10

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._current_health = 0
        ship._max_health = 100

        ship.assess_damage(amount_of_damage)

        # Assert
        self.assertEqual(10, ship._current_health)

    def test_assess_damage_max_health_add_damage_in_case_of_repair_ship(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 2
        y_location = 2
        amount_of_damage = 10

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._current_health = 100
        ship._max_health = 100

        ship.assess_damage(amount_of_damage)

        # Assert
        self.assertEqual(100, ship._current_health)

    def test__get_distance_from_target(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 3
        y_location = 3

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._range = 10
        ship._max_health = 100
        ship._attack_power = 10
        target = Cruiser('Cruise1', 'Cruiser', 0, 7, 'us')
        result = ship._get_distance_from_target(target)
        print(result)

        # Assert
        self.assertEqual(5, result)

    def test_attack_same_alignment_in_range(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'them'
        x_location = 3
        y_location = 3

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._range = 10
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

    def test_attack_diff_alignment_in_range(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 3
        y_location = 3

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._range = 10
        ship._max_health = 100
        ship._current_health = 90
        ship._attack_power = 10
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        target._current_health = 50
        ship.attack(target)
        print(target._current_health)
        print(ship._current_health)

        # Assert
        self.assertEqual(40, target._current_health)

    def test_attack_diff_alignment_and_not_in_range(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'us'
        x_location = 30
        y_location = 30

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._range = 10
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

    def test_attack_chaotic_alignment_and_in_range(self):
        # Arrange
        name = 'NShip'
        type_ = 'Battle'
        align = 'chaotic'
        x_location = 3
        y_location = 3

        # Act
        ship = Ship(name, type_, x_location, y_location, align)
        ship._range = 10
        ship._max_health = 100
        ship._current_health = 90
        ship._attack_power = 10
        target = Battle('BattleEnemy', 'Battle', 0, 7, 'them')
        target._current_health = 50
        ship.attack(target)
        print(target._current_health)
        print(ship._current_health)

        # Assert
        self.assertEqual(40, target._current_health)

