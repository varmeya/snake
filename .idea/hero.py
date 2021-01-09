#dane postaci - atrybuty
import inventory
import menu

def hero():
    print('Witaj, bohaterze!')
    print('Wprowadź swoje imię:')
    yourhero= input()
    print(f"W porządku {yourhero}, co teraz chcesz zrobić?")

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
        print("Oddychasz głęboko, a przed Twoimi oczami materializuje się wykres statystyk...")
        #tutaj podział statystyk
        exit()
    elif ans=="2":
        print("Zamaszystym ruchem dostajesz się do rozdawania punktów...")
        #system dodawania punktów z przelicznikami
        exit()
    elif ans=="3":
        print("Owierasz swoją skrzynię...")
        inventory.inventory()
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



ansfalse=False
print("zakończyłeś działanie programu")
