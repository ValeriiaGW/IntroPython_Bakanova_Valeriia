# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.
from abc import ABC, abstractmethod
from enum import Enum


class Unit(ABC):
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1

    def recovery(self):
        self.health += 10
        if self.health > 100:
            self.health = 100

    @abstractmethod
    def improve_base_skill(self):
        pass


class Mage(Unit):
    class Magic(Enum):
        AIR = "air"
        FIRE = "fire"
        WATER = "water"

    def __init__(self, name, clan, magic_type):
        super(Mage, self).__init__(name, clan)
        if magic_type in Mage.Magic:
            self.magic_type = magic_type

    def improve_base_skill(self):
        if self.intelligence < 10:
            self.intelligence += 1


class Archer(Unit):
    class Bow(Enum):
        BOW = "bow"
        CROSSBOW = "crossbow"

    def __init__(self, name, clan, bow_type):
        super(Archer, self).__init__(name, clan)
        if bow_type in Archer.Bow:
            self.bow_type = bow_type

    def improve_base_skill(self):
        if self.agility < 10:
            self.agility += 1


class Knight(Unit):
    class Weapon(Enum):
        SWORD = "sword"
        AXE = "axe"
        PIKE = "pike"

    def __init__(self, name, clan, weapon_type):
        super(Knight, self).__init__(name, clan)
        if weapon_type in Knight.Weapon:
            self.weapon_type = weapon_type

    def improve_base_skill(self):
        if self.strength < 10:
            self.strength += 1
