class Weapon:
    def __init__(self, kniv, sword, pistol, bue, max_health=100, name=""):
        self.kniv = kniv
        self.sword = sword
        self.pistol = pistol
        self.bue = bue
        self.max_health = max_health
        self.health = max_health
        self.name = name

    def take_damage(self):
        self.health -= 10
        if self.health < 0:
            self.health = 0
        print(f"{self.name} tok 10 skade. Nåværende helse: {self.health}/{self.max_health}")

    def is_broken(self):
        return self.health <= 0
