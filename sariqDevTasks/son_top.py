import random
print("Keling son topish o'yinini o'ynaymiz!")
def mygame():
    raqam, urunish = 0, 0
    raqam = random.randint(0, 10)
    print("1 dan 10 gacha son o'yladim toping ?")
    while True:
        user_num = int(input("Raqam: "))
        if user_num < raqam:
            print("Xato men o'ylaganim bundan katta !")
            urunish += 1
        elif user_num > raqam:
            print("Xato men o'ylaganim bundan kichkina !")
            urunish += 1
        elif user_num == raqam:
            print(f"Tabriklayman, {urunish} urunishda topdingiz !!!")
            break

    input("Endi siz biron raqam o'ylang men topaman, o'ylab bo'lganizdan kn enterni bosing.")
    app_raqam, app_urunish = 0, 0
    start, stop = 0, 10
    while True:
        app_num = raqam = random.randint(start, stop)
        print(
            f"Siz o'ylagan son: {app_num}, agar to'g'ri bo'lsa 'T', katta bolsa + kichik bo'lsa - yozing !")
        user_res = input(">>> ").lower()
        if user_res == "+":
            print("Obbo, hozir topamiz...")
            app_urunish += 1
            start = app_num + 1
        elif user_res == "-":
            print("Obbo, hozir topamiz...")
            app_urunish += 1
            stop = app_num - 1
        elif user_res == "t":
            if app_urunish > urunish:
                print(f"Siz mendan tezroq topdiz !")
            elif app_urunish < urunish:
                print(f"Sizdan tezroq topib qoydim :) !")
            else:
                print(
                    f"Durrang, ikkalamiz ham {app_urunish} urunishda topdik !")
            break


if __name__ == "__main__":
    live = True
    while live:
        mygame()
        print("Yana o'ynaylik, yuq demang ?")
        live = int(input("1 yoki 0 >>> "))
