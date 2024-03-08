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
