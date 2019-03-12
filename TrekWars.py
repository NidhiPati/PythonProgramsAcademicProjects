from enum import Enum
from math import sqrt


class Alignment(Enum):
    us = 1,
    them = 2,
    chaotic = 3


class Ship:
    def __init__(self, name: str, type_: str, x_location: int, y_location: int, align):
        self._name = name
        self._type = type_
        self._align = align
        self._x_location = x_location
        self._y_location = y_location
        self._range = 0
        self._attack_power = 0
        self._max_health = 0
        self._current_health = self._max_health

    def get_type(self):
        return self._type

    def get_x_location(self):
        return self._x_location

    def get_y_location(self):
        return self._y_location

    def get_alignment(self):
        if self._align not in Alignment.__members__:
            raise ValueError("Unexpected alignment value: {}\n"
                             "Expected value are: {}".format(self._align, [e.name for e in Alignment]))
        return self._align

    def status(self):
        return "Ship name: {},Ship type: {}, Current health: {}, Location ({},{}) " \
            .format(self._name, self._type, self._current_health, self._x_location, self._y_location)

    def move(self):
        if self._current_health < self._max_health:
            self._current_health = self._current_health + 1

    def change_alignment(self):
        if self._align == 'us':
            self._align = 'them'
        elif self._align == 'them':
            self._align = 'us'

    def assess_damage(self, amount_of_damage: int):
        self._current_health = self._current_health + amount_of_damage
        if self._current_health > self._max_health:
            self._current_health = self._max_health
        elif self._current_health <= 0:
            self._current_health = 0
            print("Ship Destroyed")

    def _get_distance_from_target(self, target: 'Ship'):
        return int(sqrt((target._x_location - self._x_location) ** 2 + (target._y_location - self._y_location) ** 2))

    def attack(self, target: 'Ship'):
        alignment_ = self.get_alignment()
        if (((target.get_alignment() != alignment_) or alignment_ == 'chaotic')
                and self._get_distance_from_target(target) <= self._range):
            target.assess_damage(amount_of_damage=-self._attack_power)


class Battle(Ship):
    def __init__(self, name, type_, x_location, y_location, align):
        super().__init__(name, type_, x_location, y_location, align)
        self._range = 10
        self._max_health = 100
        self._attack_power = 10
        self._torpedoes = 10

    def move(self):
        x_location = -1
        y_location = -1
        self._x_location = self._x_location + x_location
        self._y_location = self._y_location + y_location
        super().move()

    def attack(self, target: 'Ship'):
        alignment_ = self.get_alignment()
        if (((target.get_alignment() != alignment_) or alignment_ == 'chaotic')
                and self._get_distance_from_target(target) <= self._range):
            if self._torpedoes > 0:
                self._attack_power = self._attack_power + 10
                self._torpedoes = self._torpedoes - 1
            target.assess_damage(amount_of_damage=-self._attack_power)

    def status(self):
        return "Ship name: {},Ship type: {}, Current health: {}, Location: ({},{}), Torpedoes available: {}" \
            .format(self._name, self._type, self._current_health, self._x_location,
                    self._y_location, self._torpedoes)


class Cruiser(Ship):
    def __init__(self, name, type_, x_location, y_location, align):
        super().__init__(name, type_, x_location, y_location, align)
        self._range = 50
        self._max_health = 50
        self._attack_power = 5

    def move(self):
        x_location = 1
        y_location = 2
        self._x_location = self._x_location + x_location
        self._y_location = self._y_location + y_location
        super().move()

    def attack(self, target: 'Ship'):
        pass


class Corvette(Ship):
    def __init__(self, name, type_, x_location, y_location, align):
        super().__init__(name, type_, x_location, y_location, align)
        self._range = 25
        self._max_health = 20

    def move(self):
        x_location = 5
        y_location = 5
        self._x_location = self._x_location + x_location
        self._y_location = self._y_location + y_location
        super().move()

    def attack(self, target: 'Ship'):
        if (target.get_alignment() != self.get_alignment()
                and self._get_distance_from_target(target) <= self._range):
            self.change_alignment()


class Repair(Cruiser):
    def __init__(self, name, type_, x_location, y_location, align):
        super().__init__(name, type_, x_location, y_location, align)
        self._range = 25
        self._max_health = 20

    def attack(self, target):
        if (target.get_alignment() == self.get_alignment()
                and self._get_distance_from_target(target) <= self._range):
            target.assess_damage(amount_of_damage=target._max_health - target._current_health)

