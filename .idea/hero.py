
import inventory
import menu

chooseclassB = None
chooseclasskey = None
# print(type(chooseclass))

def chooseclass():
    print('Witaj, bohaterze!')
    yourhero= input('Wprowadź swoje imię:')
    print(f"W porządku {yourhero}, jaka jest Twoja klasa?")
    anstrue=True
    while anstrue:
        print ("""
        1. Wojownik
        2. Mag
        """)
        chooseclasskey=input()
        if chooseclasskey=="1":
            print("""Wojownik bazuje na sile, jest wytrzymały, lecz ma niską zwinność i inteligencje.Może używać mieczy i toporów.
                  Czy chcesz wybrać klasę Wojownik?""")
            print("T/N")
            anstrue=input()
            if anstrue=="T":
                chooseclassB= warriorbasestats()
                print("Gratulacje, wybrałeś swoją klasę")
                heromenu(chooseclasskey,chooseclassB)
            else:
             chooseclass()
        elif chooseclasskey=="2":
            print("""Mag bazuje na intelekcie i mocno czaruje, ale pada na strzała, nie umie biegać i nie da rady przynieść 25kg cukru do domu
                  Czy chcesz wybrać klasę Mag?""")
            print("T/N")
            anstrue=input()
            if anstrue=="T":
                chooseclassB= magebasestats()
                print("Gratulacje, wybrałeś swoją klasę")
                heromenu(chooseclasskey,chooseclassB)


def heromenu(choose, chooseclassB):
    print(f"Witaj,co chcesz teraz zrobić?")
    anstrue=True
    while anstrue:
        print ("""
        1. Zobacz swoje statystyki
        2. Rozdaj punkty umiejętności
        3. Przejrzyj ekwipunek
        4. Zmień ekwipunek
        5. Wróć
        """)
        ans=input()
        if ans=="1":
            print("Twoje statystyki")
            if choose=="1":
                print("Twoje statystyki wynoszą:")
                chooseclassB.printwarriorstats()
            elif choose=="2":
                print("Twoje statystyki wynoszą:")
                chooseclassB.printmagestats()
            else:
                    heromenu(choose2)
            exit()

        elif ans=="2":
            print("Rozdawanie punktów statystyk")
            #system dodawania punktów z przelicznikami
            exit()
        elif ans=="3":
            print("Owierasz swoją skrzynię...")
            inventory.openbag()
            exit()
        elif ans=="4":
            print("Tyle wszystkiego, że nie wiesz w co się ubrać!")
            inventory.changeeq
            exit()
        elif ans=="5":
            print("Wracasz do menu")
            menu.mainmenu()
            exit()
        else:
            print('Wybierz wartosc 1-4')


class warriorbasestats:
    def __init__(self):
        self.strenght=10
        self.stamina=6
        self.agility=3
        self.intelect=2
    def printwarriorstats(self):
        print(f'Siła: {self.strenght}',
              f'Wytrzymałość: {self.stamina}',
              f'Zwinność: {self.agility}',
              f'Intelekt: {self.intelect}', sep="\n",)
#chooseclass= warriorbasestats()
# chooseclass.printwarriorstats()
class magebasestats:
    def __init__(self):
        self.strenght=2
        self.stamina=5
        self.agility=3
        self.intelect=15
    def printmagestats(self):
        print('Siła:',self.strenght, 'Wytrzymałość:', self.stamina, 'Zwinność:', self.agility, 'Intelekt:', self.intelect )
#chooseclass= magebasestats()
# chooseclass.printmagestats()