from weapon import Weapon
from karakter import Karakter
from rom import Room
import random

navn = "Player"
kniv = "ja"   
sverd = "ja"
pistol = "ja"
bue = "ja"

vil_gå_inn_i_rom1 = input("Vil du gå inn i det første rommet? (ja/nei): ")

mine_våpen = Weapon(kniv, sverd, pistol, bue)

min_karakter = Karakter(navn,  health = random.randint(100, 200), weapon=mine_våpen)

monster_navn = "Monster"
monster_helse = random.randint(100, 250)  
monster_våpen = Weapon(kniv, sverd, pistol, bue)  
monster = Karakter(navn=monster_navn, health=monster_helse, weapon=monster_våpen)

if vil_gå_inn_i_rom1.lower() == 'ja':
    Rom1 = "Første rom"
    Rom2 = None
    monster_rom = Room(Rom1=Rom1, Rom2=Rom2, monster=monster)
    monster_rom.monster = monster
    monster_rom.karakter = min_karakter
elif vil_gå_inn_i_rom1.lower() == 'nei':
    Rom1 = None
    Rom2 = "Andre rom"
    monster_rom = Room(Rom1=Rom1, Rom2=Rom2, monster=monster)
else:
    print("Ugyldig valg av rom.")

if Rom1:
    min_karakter.current_room = Rom1
elif Rom2:
    min_karakter.current_room = Rom2

min_karakter.skriv_info()


if min_karakter.current_room:
    monster_rom.enter(min_karakter)
     

    if monster_rom.monster:
        while min_karakter.health > 0 and monster_rom.monster.health > 0:
            valg = input("Vil du angripe monsteret? (ja/nei): ")
            if valg.lower() == 'ja':
                min_karakter.attack(monster_rom.monster)
                if monster_rom.monster.health <= 0:
                    print(f"{monster_rom.monster.navn} er beseiret! Du vant!")
                    break
                monster_rom.monster.attack(min_karakter)
                if min_karakter.health <= 0:
                    print(f"{min_karakter.navn} er beseiret! ")
                    
            else:
                print("Du velger å ikke angripe.")
                break
