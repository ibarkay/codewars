class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    def set_helth(self, health):
        self.health = health

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        Warrior.__init__(self, health, )
        self.attack = attack


def fight(unit_1, unit_2):
    run = True
    answr = True
    while run:
        if unit_1.health > 0 and unit_2.health > 0:
            unit_2.set_helth(unit_2.health - unit_1.attack)

        if unit_2.health > 0 and unit_1.health > 0:
            unit_1.set_helth(unit_1.health - unit_2.attack)

        else:
            if unit_1.health > unit_2.health:
                answr = True
                run = False
            else:
                answr = False
                run = False
    return answr


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce)
print chuck.is_alive