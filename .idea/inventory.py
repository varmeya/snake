
import hero
import menu

def inventorymenu():
    anstrue=True
    while anstrue:
        print("""
        1.Sprawdź aktualnie założone przedmioty
        2.Zmień ekwipunek
        3.Otórz torbę podręczną
        4.Wróć do głównego menu
            """)
        ans=input("Co zamierzasz zrobić?")
        if ans =="1":
            inventorycharacter()
            exit()
        elif ans =="2":
            changeeq()
            exit()
        elif ans=="3":
            openbag()
            exit()
        elif ans=="4":
            print("Wracasz go głównego menu")
            menu.mainmenu()
            exit()
        else:
            print('Wybierz wartosc 1-4')


def inventorycharacter():
    print("Twój bohater aktualnie ma założone:")
#ten sam problem co z wyborem klasy
    # inventoryowned=(equipslot1= broń
    #                 equipslot2= armor
    #                 )
    print(inventoryowned)
    ans=input("Czy chcesz zmienić ekwpiunek?","\n", "T/N")
    if ans=="T":
        changeeq()
    elif ans=="N":
        inventorycharacter()
    else:
        print("Podaj wartość T/N")
# def changeeq():
# #print(f"Aktualnie założone przedmioty to: {inventoryowned}, czy chcesz zmienić swój ekwipunek?")

#lista zawartosci baga = poty, armor, broń, zioła, jedzenie
def openbag():
    print("Chyżo otwierasz swoją torbę...")
    bag =[
        rustedsword1.name,
        rustedsword2.name
    ]
    print(*bag, sep="\n")

#ARMORY
class weapontype:
    def __init__(self, sword, longsword, staff, knife, equipslot1):
        self.sword=sword
        self.longsword=longsword
        self.staff=staff
        self.knife=knife
        self.equipslot1=equipslot1
class weaponstats:
    def __init__(self, strenght, stamina, agility, intelect):
        self.strenght=strenght
        self.stamina=stamina
        self.agility=agility
        self.intelect=intelect

class sword:
    def __init__(self, name,  weaponstats, weight):
        self.name=name
        self.weaponstats=weaponstats
        self.weight=weight

    def printswordstats(self):
        print(self.name)
        print(f"Siła: {self.weaponstats.strenght}")
        print(f"Wytrzymałość: {self.weaponstats.stamina}")
        print(f"Zwinność: {self.weaponstats.agility}")
        print(f"Intelekt: {self.weaponstats.intelect}")
        print(f"Waga: {self.weight}")


weaponstats1 = weaponstats(1,1,1,1)
rustedsword1 = sword("Zardzewiały miecz +1 ", weaponstats1, 10)
# rustedsword1.printswordstats()

weaponstats2=weaponstats(2,3,1,1)
rustedsword2=sword("Zardzewiały miecz +2", weaponstats2, 15)
# rustedsword2.printswordstats()


# class longsword:
#     def __init__(self, name, weaponstats, weight):
#         self.name=name
#         self.weaponstats=weaponstats
#         self.weight=weight
#     def printlongswordstats(self):
#         print(self.name)
#         print(f"Siła: {self.weaponstats.strenght}")
#         print(f"Wytrzymałość: {self.weaponstats.stamina}")
#         print(f"Zwinność: {self.weaponstats.agility}")
#         print(f"Intelekt: {self.weaponstats.intelect}")
#         print(f"Waga: {self.weight}")
#
# weaponstats3=weaponstats(1,2,0,0)
# silverlongsword1=longsword("Długi miecz +1",weaponstats3, 15)
# silverlongsword1.printlongswordstats()
#
#
#
# class staff:
#     def __init__(self, weaponstats, weight):
#         self.weaponstats=weaponstats
#         self.weight=weight
#     def printstaffstats(self):
#         print(f"Siła: {self.weaponstats.strenght}")
#         print(f"Wytrzymałość: {self.weaponstats.stamina}")
#         print(f"Zwinność: {self.weaponstats.agility}")
#         print(f"Intelekt: {self.weaponstats.intelect}")
#         print(f"Waga: {self.weight}")
#
#
#
#
# class knife:
#     def __init__(self, weaponstats, weight):
#         self.weaponstats=weaponstats
#         self.weight=weight
#     def printknifestats(self):
#         print(f"Siła: {self.weaponstats.strenght}")
#         print(f"Wytrzymałość: {self.weaponstats.stamina}")
#         print(f"Zwinność: {self.weaponstats.agility}")
#         print(f"Intelekt: {self.weaponstats.intelect}")
#         print(f"Waga: {self.weight}")
#
#


