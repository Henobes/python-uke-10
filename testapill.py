from weapon import Weapon
from karakter import Karakter
from rom import Room
import random

navn = "Testus"
kniv = "ja"   
sverd = "ja"
pistol = "ja"
bue = "ja"

vil_gå_inn_i_rom1 = input("Vil du gå inn i det første rommet? (ja/nei): ")

mine_våpen = Weapon(kniv, sverd, pistol, bue)


min_karakter = Karakter(navn=navn, health=100, weapon=mine_våpen)

monster_navn = "Monsterus"
monster_helse = random.randint(50, 100)  # Tilfeldig monsterhelse
monster_våpen = Weapon(kniv, sverd, pistol, bue)  # Gi monsteret et våpen
monster = Karakter(navn=monster_navn, health=monster_helse, weapon=monster_våpen)

if vil_gå_inn_i_rom1.lower() == 'ja':
    Rom1 = "Første rom"
    Rom2 = None
    mine_rom = Room(Rom1=Rom1, Rom2=Rom2, monster=monster)
elif vil_gå_inn_i_rom1.lower() == 'nei':
    Rom1 = None
    Rom2 = "Andre rom"
    mine_rom = Room(Rom1=Rom1, Rom2=Rom2, monster=monster)
else:
    print("Ugyldig valg av rom.")

if Rom1:
    min_karakter.current_room = Rom1
elif Rom2:
    min_karakter.current_room = Rom2

min_karakter.skriv_info()

# Gå inn i rommet hvis et rom er valgt
if min_karakter.current_room:
    mine_rom.enter(min_karakter)

mine_våpen.take_damage()
class Room:
    def __init__(self, Rom1=None, Rom2=None, monster=None):
        self.Rom1 = Rom1
        self.Rom2 = Rom2
        self.monster = monster

    def enter(self, karakter):
        if karakter.current_room == self.Rom1:
            print(f"Velkommen til {self.Rom1}!")
        elif karakter.current_room == self.Rom2:
            print(f"Velkommen til {self.Rom2}!")
        else:
            print("Du kan ikke gå inn i dette rommet.")

        # Starter kampen hvis det er et monster i rommet
        if self.monster:
            print(f"Det er et monster i rommet! Kampen starter!")
            while karakter.health > 0 and self.monster.health > 0:
                # Karakteren angriper monsteret
                karakter.attack(self.monster)
                # Sjekker om monsteret er beseiret
                if self.monster.health <= 0:
                    print(f"{self.monster.navn} er beseiret!")
                    break
                # Monsteret angriper karakteren
                self.monster.attack(karakter)
                # Sjekker om karakteren er beseiret
                if karakter.health <= 0:
                    print(f"{karakter.navn} er beseiret!")
                    break
            # Skriver ut sluttresultatet av kampen
            print("Kampen er over!")
            karakter.skriv_info()
import random

class Karakter:
    def __init__(self, navn, health, weapon):
        self.navn = navn
        self.health = health
        self.weapon = weapon

    def attack(self, monster):
        damage = random.randint(1, 10)  # Tilfeldig skadedamage
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

        # Skriver ut informasjon om karakterens våpen
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
            print(f"{self.name} har {self.health} helse igjen.")

    def attack(self, karakter):
        damage = random.randint(1, 10)  # Tilfeldig skadedamage
        print(f"{self.name} angriper {karakter.navn} og gjør {damage} skade!")
        karakter.take_damage(damage)
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
