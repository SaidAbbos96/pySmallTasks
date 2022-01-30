def stars_game():
    sym = "*"
    while True:
        print("Ekranga chiqadigan yulduzchalar sonini kiriting !")
        countstars = input(">>> ")
        if countstars.isdigit() != True:
            print("iltimos raqam kiriting !!!")
            continue

        for num in range(1, int(countstars) + 1):
            print(sym * num)


def geme_EOE():
    print("Salom EVEN ODD EVEN o'yiniga hush kelibsiz !")
    while True:
        max_num = input("Tekshirish uchun maksimal sonni kiriting !\n>>> ")
        if max_num.isdigit() != True:
            print("iltimos raqam kiriting !!!")
            continue

        for num in range(1, int(max_num) + 1):
            if num % 2:
                print(f"{num} is ODD (Toq son !)")
            else:
                print(f"{num} is EVEN (Juft son !)")

        break


def sum_diapazon():
    maxbound = input("Maximal sonni kiriting\n>>> ")
    if maxbound.isdigit() != True:
        return print("iltimos raqam kiriting !!!")
    print(sum([num for num in range(int(maxbound) + 1) if num %
          3 == 0 or num % 5 == 0]))


def cards_sum():
    current_hand = [2, 3, 4, 10, 'Q', 5]
    current_hand = ["A", 3, 4, 10, "J", 4]

    all_cards = [
        [2, 3, 4, 5, 6],
        [7, 8, 9],
        [10, "J", "Q", "K", "A"]
    ]
    cards_sum = 0
    for card in current_hand:
        if card in all_cards[0]:
            cards_sum += 1
        elif card in all_cards[2]:
            cards_sum -= 1
    print(cards_sum)


def flush():
    table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
    hand_cards = ["J_D", "3_D"]
    suits = [card[-1] for card in table_cards+hand_cards]
    for suit in "CHSD":
        if suits.count(suit) >= 5:
            res = "Flush!"
            break
        else:
            res = "No Flush!"
    print(res)


def palindrom():
    number = 14541
    text = str(number)
    import re
    re.compile('[^a-zA-Z0-9]').sub('', text.lower())
    if text == text[::-1]:
        print("palindrome")
    else:
        print("No Palindrome")


if __name__ == "__main__":
    # stars_game()
    # geme_EOE()
    # sum_diapazon()
    # cards_sum()
    # flush()
    palindrom()
