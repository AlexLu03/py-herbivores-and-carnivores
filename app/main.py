class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            if self in Animal.alive:
                Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, obj: Animal):
        if isinstance(obj, Herbivore) and not obj.hidden:
            obj.take_damage(50)
