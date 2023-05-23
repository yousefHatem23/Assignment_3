from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.data = BinarySearchTree()
    
    def add_point(self, item: T):
        self.data.insert_aux(self.data.root, item, T)
    
    def remove_point(self, item: T):
        self.data.delete_aux(self.data.root, T)

    def ratio(self, x, y):
        result = []
        for value in self.data.in_order():
            if x < value < y:
                result.append(value)
        return result

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))

# python3 run_tests.py 2