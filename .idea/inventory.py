#wprowadzanie imienia i nazwiska bohatera
#wybór klasy z listy > jesli nie chcesz wybrac klasy to wybiera randomowo
#dodawanie i usuwanie przedmiotow z ekwipunku > postac musi miec przynajmniej 1 przedmiot typu bron i typu zbroja
#statystyki postaci- sila, intelekt, stamina, zwinnosc - statystyki zalezne od klasy i mozliwe do rozdawania po lvl up
#ekwipunek ma wymagana wartosc statystyk do  uzywania np 15 sily dla longsworda
#maksymalny udzwig postaci- kazdy przedmiot ma swoja wage
#walki na arenie - przeciwnicy zadaja okreslona ilsoc dmg fizycznego i magizcnego w zaleznosci od swoich stat
#staty sa zalezne od lvl potwora i sa porownywane ze statami bohatera, wstepnie mechanizm wiecej sily lub inta wygrywa z przelicznikiem dla danych stat, zwinnosc od dodgle
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

    inventoryowned=("Miecz",
               "tarcza",
               "czerwone buty szybkości",
               "mikstura many")
    print(inventoryowned)

def changeeq():
    print(f"Aktualnie założone przedmioty to: {inventoryowned}, czy chcesz zmienić swój ekwipunek?")

def openbag():
    print("Chyżo otwierasz swoją torbę...")



