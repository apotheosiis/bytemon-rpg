class Inventory:
    def __init__(self, items=None):
        self.items = [""]

    def __str__(self):
        return "This is your bag"


    def showItens(self):
        if self.items:
            print(">>> These are your items!")
            for item in self.items:
                print(f"({item})")
            print('-------')
        else:
            print("!!! You don't have any itens.")
    
    def addItem(self,item):
        self.items.append(item)
        print(f"!!! Congratulations, you got a {item}.")
        print("-------")

    def deleteItem(self,item):
        if item in self.items:
            self.items.remove(item)
            print("!!! Your item has been deleted")
            print("-------")
        else:
            print("!!! You don't have this item.")
            print("-------")

    def useItem(self, item):
        if item in self.items:
            if item == "Life Potion":
                print("!!! You used the Life Potion. It seems your strength has returned!\n   +2 Life ")
            if item == "Mana Potion":
                print("!!! You used the Mana Potion. You feel the mana emanating from your body.\n !!!+2 Mana")  
        else:
            print("!!! You don't have this item in your bag.")