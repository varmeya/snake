#menu pozwlające na wybór aktywności
import hero
import inventory

def mainmenu():

    anstrue=True

    while anstrue:
        print("""
        1.Otwórz swój ekwipunek
        2.Udaj się na arenę
        3.Zatańcz
        4.Wyjdź z gry
            """)
        ans=input("Co zamierzasz zrobić?")
        if ans =="1":
            print("Witaj w swoim ekwipunku!")
            inventory.inventorymenu()

        elif ans =="2":
            print("Zmierzasz w kierunku areny...")
            #plik z areną
            exit()
        elif ans=="3":
            print("Tańczysz szybko")
            exit()
        elif ans=="4":
            print("Do zobaczenia!")
            exit()
        else:
            print('Wybierz wartosc 1-4')

