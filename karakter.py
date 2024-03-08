import random

class Karakter:
    def __init__(self, navn, health, weapon):
        self.navn = navn
        self.health = health
        self.weapon = weapon

    def attack(self, monster):
        damage = random.randint(5, 80)  
        print(f"{self.navn} angriper med {self.weapon.name} og gjør {damage} skade!")
        monster.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.navn} har blitt beseiret!")
        else:
            print(f"{self.navn} har {self.health} helse igjen.")

    def skriv_info(self):
        print("Karakter:")
        print(f"Navn: {self.navn}")
        print(f"Helse: {self.health}")

       
        print("Våpen:")
        print(f"- Sverd: {self.weapon.sword}")
        print(f"- Kniv: {self.weapon.kniv}")
        print(f"- Pistol: {self.weapon.pistol}")
        print(f"- Bue: {self.weapon.bue}")

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} har blitt beseiret!")
        else:
            print(f"{self.name} har {self.health} liv igjen.")

    def attack(self, karakter):
        damage = random.randint(5, 45)  
        print(f"{self.name} angriper {karakter.navn} og gjør {damage} skade!")
        karakter.take_damage(damage)
