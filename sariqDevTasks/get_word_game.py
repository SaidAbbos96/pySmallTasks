import random
from uzwords import words as words_list

def mask_m(mask):
    return ''.join(mask).upper()

def my_game():
    word, temp = random.choice(words_list).lower(), ""
    word ="salom"
    while "-" in word or " " in word:
        word = random.choice(words_list).lower()

    mask = list("*" * len(word))
    print(f"Men {len(word)} xonali so'z o'yladim, krel alifbosida harflar kiriting !\nSo'z: {mask_m(mask)}")
    
    while True:
        char = input("Harfni kiriting: ")
        if len(char) > 0:
            char = char.strip()[0]

        if char in temp:
            print("Harflarni qayta kirityapsiz !")
            continue

        temp += char
        if char in word:
            print("Ha topdingiz, qolgan harflarni ham toping !")
            for index, sym in enumerate(word):
                # print(word.find(char)) boshqa usul ammo harf bir martadan ortiq uchrasa ishlamaydi
                if sym == char:
                    mask[index] = char
        else:
            print("Bu harf mavjud emas, yana urunib ko'ring !")
        if word == ''.join(mask):
            print(mask_m(mask), f"\nTabriklayman, so'z {len(temp)} urunishda to'liq topildi, o'yin tugadi !")
            break
        print(f"{'-'*30}\nSo'z: {mask_m(mask)}")


if __name__ == "__main__":
    live = True
    while live:
        my_game()
        print("Yana o'ynaylik, yuq demang ?")
        live = input("1 yoki 0 >>> ")
        if live not in ["1", "0"]:
            live = False
        else:
            live = int(live)


