def first_shooter():
    p1, p2 = "    Bang!      ", "         Bang!   "

    def whos_first(shoot1: str, shoot2: str) -> str:
        diff = shoot1.find("Bang!") - shoot2.find("Bang!")
        if diff < 0:
            return "p1"
        elif diff > 0:
            return "p2"
        else:
            return "tie"
    print(whos_first(p1, p2))


def calc_dice_scores(dices: list):
    res_sum = 0
    for dice in dices:
        if dice[0] != dice[1]:
            res_sum += sum(dice)
        else:
            res_sum = 0
            break

    return res_sum


def calc_dice_scores2(dices: list):
    return sum([a+b for a, b in dices]) if not any([a == b for a, b in dices]) else 0


def any_duplicates(square: list):
    return len(set(y for x in square for y in x)) != 9
    # myset = []
    # for x1 in square:
    #     myset += x1
    # return len(set(myset)) != 9


def solve_hanoi(disc):
    return 2**disc-1


if __name__ == "__main__":
    pass
    # first_shooter()
    # print(calc_dice_scores([(1, 2), (3, 4), (5, 6)]))
    # print(calc_dice_scores([(1, 1), (5, 6), (6, 4)]))
    # print(calc_dice_scores([(4, 5), (4, 5), (4, 5)]))
    # print(calc_dice_scores2([(4, 5), (4, 5), (4, 5)]))
    # print(calc_dice_scores2([(4, 5), (5, 5), (4, 5)]))
    print(any_duplicates([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(any_duplicates([[1, 2, 3], [4, 5, 4], [7, 8, 9]]))
