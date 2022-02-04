import itertools


def count_vowels(text: str) -> int:
    return sum([1 for x in text.lower() if x in "aeiou"])
    # vowels = ["A", "E", "I", "O", "U", "Y"]
    # count: int = 0
    # for char in text.upper():
    #     if char in vowels:
    #         count += 1
    # return count


# print(count_vowels("hello world"))

def is_full_house(cards: list) -> bool:
    return all([cards.count(el) >= 2 for el in cards])


# print(is_full_house(["A", "A", "A", "K", "K"]))

class IceCream:
    gradients = {
        "Plain": 0,
        "Vanilla": 5,
        "ChocolateChip": 5,
        "Strawberry": 10,
        "Chocolate": 10
    }

    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles

    def get_candy(self):
        return IceCream.gradients[self.flavor] + self.sprinkles


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)


def sweetest_icecream(lst) -> int:
    return max([IceCream.gradients[obj.flavor] + obj.sprinkles for obj in lst])


# print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))


def check_sequence(lst):
    if sorted(set(lst)) == lst:
        return 1
    elif sorted(set(lst), reverse=True) == lst:
        return -1
    else:
        return 0


# print(check_sequence([1, 2, 3]))
# print(check_sequence([3, 2, 1]))
# print(check_sequence([1, 3, 2]))
# print(check_sequence([1, 1, 2]))


class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_pages = 1 if not self.items else (len(self.items) // self.page_size) + 1
        self.current_page = 1

    def get_items(self):
        return self.items

    def get_page_size(self):
        return self.page_size

    def get_current_page(self):
        return self.current_page

    def prev_page(self):
        if self.current_page == 1:
            return self
        self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page == self.total_pages:
            return self
        self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page: int):
        if page < 1:
            page = 1
        elif page > self.total_pages:
            page = self.total_pages

        self.current_page = page
        return self

    def get_visible_items(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]
