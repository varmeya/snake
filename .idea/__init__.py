import menu
import hero

def gamemenu():
    print("Witaj w AzeRPG!")

    while anstrue:
        print("""
        1.Przejdź do głównego menu
        2.Stwórz postać
        3.Wyjdź z gry
            """)
        ans=input("Co zamierzasz zrobić?")
        if ans =="1":
            print("Witaj w głownym menu!")
            menu.mainmenu()
        elif ans =="2":
            hero.chooseclass()

        elif ans =="3":
            print("See you soon!")
            exit()
anstrue=True
gamemenu()
