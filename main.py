from typing import List, Any, Optional
import random

class MinPair:
    def __init__(self):
        self.min1: Optional[float] = None
        self.min2: Optional[float] = None

    def update(self, value: float):
        if self.min1 is None or value < self.min1:
            self.min2 = self.min1
            self.min1 = value
        elif self.min2 is None or value < self.min2:
            self.min2 = value

    def sum(self) -> float:
        if self.min1 is None or self.min2 is None:
            raise ValueError("Недостаточно числовых элементов для вычисления суммы.")
        return self.min1 + self.min2

def main(array: List[Any]) -> float:
    """
        Находит сумму двух минимальных чисел в массиве.
        :param array: Лист элементов разных типов
        :return: Сумма двух минимальных чисел
    """
    pair = MinPair()
    for item in array:
        if isinstance(item, (int, float)):
            pair.update(item)
    return pair.sum()

def random_array() -> List[Any]:
    """
        Создает случайный массив из разных типов элементов [str, int], может быть пустым
        :return: Случайный список
    """
    length = random.randint(0, 10)
    result = []
    for _ in range(length):
        if random.choice([True, False]):
            result.append(random.randint(-100, 100))
        else:
            result.append(''.join(random.choices('abcdef', k=random.randint(1, 5))))
    return result


arr = random_array()
print("Случайный массив:", arr)
try:
    print("Сумма двух минимальных чисел:", main(arr))
except ValueError as e:
    print("Ошибка:", e)
