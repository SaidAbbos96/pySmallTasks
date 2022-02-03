import random
from typing import Any, Optional, List, Tuple, Iterable


class Character:
    def __init__(self, armor: int, damage: int):
        """my simple Character class"""
        self.damage = damage
        self.armor = armor

    def get_armor(self) -> int:
        return self.armor


obj1 = Character(10, 55)
print(obj1.armor)

myvar: int = 15
# mover = "salom"
var1: int = 5
var2: str = "salom"
var3: Any = None
var4: Optional[int]
var5: List = [1, 5]
var6: List[int, str]
var7: Tuple[str, int]
var8: Tuple[int, ...]


def randoms(min: int, max: int) -> Iterable[int]:
    while True:
        yield random.randint(min, max)
