import random
from typing import Any, Protocol, Optional, List, Tuple, Iterable, Literal, Final, Dict, TypedDict, Union, overload


#
# class Character:
#     def __init__(self, armor: int, damage: int):
#         """my simple Character class"""
#         self.damage = damage
#         self.armor = armor
#
#     def get_armor(self) -> int:
#         return self.armor
#
#
# obj1 = Character(10, 55)
# print(obj1.armor)
#
# myvar: int = 15
# # mover = "salom"
# var1: int = 5
# var2: str = "salom"
# var3: Any = None
# var4: Optional[int]
# var5: List = [1, 5]
# var6: Dict[int, str]
# var7: Tuple[str, int]
# var8: Tuple[int, ...]
#
#
# def randoms(min: int, max: int) -> Iterable[int]:
#     while True:
#         yield random.randint(min, max)
#
#
# def simple_func(arg1, arg_mode: Literal["a", "b"]):
#     print(arg1, arg_mode)
#
#
# # constanta using type hint Final
#
# MYCONST: Final = 15
#
# person: Dict[str, str] = {"name": "Said"}
# # combienit Type
# person2: Dict[str, Any] = {"name": "said", "age": 25, "isman": True}
#
#
# # custom type hint Dict
# class Person(TypedDict):
#     name: str
#     age: int
#     isman: bool
#
#
# person3: Person = {"name": "said", "age": 25}


#  overload
# @overload
# def funcsum(x: int, y: int, parse_str: Literal[False]) -> int: ...
#
#
# @overload
# def funcsum(x: int, y: int, parse_str: Literal[True]) -> str: ...
#
#
# def funcsum(x: int, y: int, parse_str: bool) -> Union[str, int]:
#     res = x + y
#     return str(res) if parse_str else res
#
#
# print(funcsum(10, 5, False))
# print(type(funcsum(10, 5, True)))

# protocol hnting
class Bird:
    def fly(self):
        print(f"Flying bird")


class Plane:
    def fly(self):
        print(f"Flying airplane")


class Fish:
    def swim(self):
        print("fish is swin")

class Flyable(Protocol):
    def fly(self): ...


def run_fly(objects: List[Flyable]):
    for obj in objects:
        obj.fly()


# run_fly([Bird(), Plane(), Fish()])# AttributeError: 'Fish' object has no attribute 'fly'
run_fly([Bird(), Plane()])# ok