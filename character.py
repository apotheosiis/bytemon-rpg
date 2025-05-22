from bytemon import *

class Character:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anonymous"
        
        self.pokemons = pokemons  

    def __str__(self):
        return self.nome

class Player(Character):
    tipo = "player"

class Enemy(Character):
    tipo = "enemy"


eu = Player(nome="Renamzim")
print(eu)

meuPokemon = FireBytemon(1,"Rogerim")
print(meuPokemon)