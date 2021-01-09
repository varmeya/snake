#menu pozwalające na wybór aktywności

import inventory

anstrue=True
while anstrue:
    print ("""
    1. Otwórz swój ekwipunek
    2. Udaj się na arenę
    3. Zatańcz
    4.Exit/Quit
    """)
    ans=input("Co zamierzasz zrobić? ")
    if ans=="1":
        print("Chyżo otwierasz swoją torbę...")
        inventory.inventory1()
        exit()
    elif ans=="2":
        print("Zmierzasz w kierunku areny...")
        exit()
    elif ans=="3":
        print("\n Tańczysz szybko...")
        exit()
    elif ans=="4":
        print("\n koniec")
        exit()
    else:
        print('Wybierz wartosc 1-4')



ansfalse=False
print("zakończyłeś działanie programu")
