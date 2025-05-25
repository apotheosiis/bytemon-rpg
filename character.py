from bytemon import *
from inventory import *
import random

class Character:

    def __init__(self, name=None, bytemons=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(['Renatim','Cleitim','Rogerim','Mariazinha'])
        
        self.bytemons = bytemons  

    def __str__(self):
        return self.name
    
    def show_bytemons(self):
        if len(self.bytemons) == 0:
            print(f"!!! You don't have any bytemon.")
        else:
            for bytemon in self.bytemons:
                print(bytemon)
    
            
class Player(Character):
    tipo = "player"

    def capture_bytemon(self,bytemon,byteball):
        rnc = random.randint(1,10)

        if byteball == "HighBall":
            if rnc < 8:
                #if to see if theres any highball in the inventory
                print(f"!!! WOWW, you captured {bytemon} with your HighBall.")
                self.bytemons.append(bytemon)
                #remove 1 highball
            else:
                print("!!! It seems that you fail :( ")
                #remove 1 highball

        if byteball == "Byteball":
            if rnc <= 5:
                print(f"!!! WOWW, you captured {bytemon} with your ByteBall.")
                self.bytemons.append(bytemon)
                #remove 1 byteball
            else:
                print("!!! It seems that you fail :( ")
                #remove 1 byteball
        else:
            print("You're doing something wrong...")
        

class Enemy(Character):
    tipo = "enemy"
    
    def __init__(self):
        bytemon_pool = ['Pyrobite', 'Hydroflux', 'Leafcode']
        chosen = random.choice(bytemon_pool)
        super().__init__(bytemons=[chosen])
