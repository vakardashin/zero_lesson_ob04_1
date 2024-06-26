#  Игра демонстрирует принцип открытости/закрытости
#  в Python


from abc import ABC, abstractmethod


#  Создаём абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


#  Создаём класс Sword, унаследованный от Weapon
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

#  Создаём класс Bow, унаследованный от Weapon
class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print("Боец не выбрал оружие.")


fighter = Fighter("Герой")
sword = Sword()
bow = Bow()

fighter.changeWeapon(sword)
fighter.attack()  # Боец наносит удар мечом.

fighter.changeWeapon(bow)
fighter.attack()  # Боец наносит удар из лука.


class Monster:
    def __init__(self, name):
        self.name = name

    def takeDamage(self):
        print(f"{self.name} побежден!")


monster = Monster("Монстр")

fighter.changeWeapon(sword)
fighter.attack()  # Боец наносит удар мечом.
monster.takeDamage()

fighter.changeWeapon(bow)
fighter.attack()  # Боец наносит удар из лука.
monster.takeDamage()
