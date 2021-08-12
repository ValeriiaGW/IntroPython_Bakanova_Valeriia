class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1

    def heal(self):
        self.health += 10
        if self.health > 100:
            self.health = 100

    def hurt(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def _damage(self, skill):
        return self.strength + self.agility + self.intelligence + 2 * self.__dict__[skill]

    def _skill_up(self, skill):
        self.__dict__[skill] += 1
        if self.__dict__[skill] > 10:
            self.__dict__[skill] = 10


class Mage(Unit):
    # mage_type could be only "air", "fire", "water"
    def __init__(self, name, clan, mage_type: str):
        super().__init__(name, clan)
        self.mage_type = mage_type
        self.skill = 'intelligence'

    def skill_up(self):
        super()._skill_up(self.skill)

    def damage(self):
        return super()._damage(self.skill)


class Knight(Unit):
    # knight_type could be only "sword", "axe", "peak"
    def __init__(self, name, clan, knight_type: str):
        super().__init__(name, clan)
        self.knight_type = knight_type
        self.skill = 'strength'

    def skill_up(self):
        super()._skill_up(self.skill)

    def damage(self):
        return super()._damage(self.skill)


class Archer(Unit):
    # archer_type could be only "bow", "arbalest"
    def __init__(self, name, clan, archer_type: str):
        super().__init__(name, clan)
        self.archer_type = archer_type
        self.skill = 'agility'

    def skill_up(self):
        super()._skill_up(self.skill)

    def damage(self):
        return super()._damage(self.skill)


mage = Mage('Hendalf', 'Brotherss of the Ring', 'water')
print(mage)
print(mage.health)
mage.health = 55
print(mage.health)
mage.heal()
print(mage.health)
print(mage.skill)
print(mage.intelligence)
print(mage.agility)
mage.skill_up()
print(mage.intelligence)
print(mage.agility)


print('########################')
knight = Knight("Cezar", 'Warrior', "peak")
print('damage: ', knight.damage())
print(knight.strength)
print(knight.agility)
knight.skill_up()
print('damage: ', knight.damage())
print(knight.strength)
print(knight.agility)
knight.skill_up()
print('damage: ', knight.damage())
print('#######################')
print('before ', mage.health)
mage.hurt(knight.damage())
print('after ', mage.health)
