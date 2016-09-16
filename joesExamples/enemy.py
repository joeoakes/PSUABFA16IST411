class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)

e1 = Dog()
print(e1.name + " " + str(e1.hp) + " " + str(e1.damage))
e2 = Ogre()
print(e2.name + " " + str(e2.hp) + " " + str(e2.damage))
e3 = GiantSpider()
print(e3.name + " " + str(e3.hp) + " " + str(e3.damage))
