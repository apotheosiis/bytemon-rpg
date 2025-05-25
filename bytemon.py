class Bytemon:
    def __init__(self, specie, level=1, name=None):
        self.specie = specie
        self.level = level

        if name:
            self.name = name
        else:
            self.name = specie

    def __str__(self):
        return f"{self.name}({self.level})"

class LeafBytemon(Bytemon):
    type = "Leaf"
    def attack(self, enemy):
        return "{self} uses some leafs on {enemy}!"

class FireBytemon(Bytemon):
    type = "Fire"
    def attack(self, enemy):
        return f"{self} lanches a fire orb on {enemy}!"

class WaterBytemon(Bytemon):
    type = "Water"
    def attack(self, enemy):
        return f"{self} launches some water on {enemy}!"
    
class Pyrobyte(FireBytemon):
    specie = "Pyrobyte"
    def attack(self,enemy):
        return f"{self} executes Overheat Pulse on {enemy}! The air distorts with raw thermal energy!"
    
class Glitchfare(FireBytemon):
    specie = "Glitchfare"
    def attack(self, enemy):
        return f"{self} launches Thermal Corrupt at {enemy}! Reality flickers with glitching flames!"

class Hydroflux(WaterBytemon):
    specie = "Hydroflux"
    def attack(self, enemy):
        return f"{self} releases Data Surge on {enemy}! A torrent of encrypted water floods the field!"

class CryoLoop(WaterBytemon):
    specie = "CryoLoop"
    def attack(self, enemy):
        return f"{self} activates Freeze Protocol on {enemy}! The battlefield drops below zero!"
    
class Leafcode(LeafBytemon):
    specie = "Leafcode"
    def attack(self, enemy):
        return f"{self} uses Vine Inject on {enemy}! Code-infused vines pierce all the way!"

class Rootbit(LeafBytemon):
    specie = "Rootbit"
    def attack(self, enemy):
        return f"{self} sets a Backdoor Trap under {enemy}! A hidden payload is now ticking..."

    