import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r'\b\d+\.\d+|\b\d+', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers)) 
