import re
from typing import Callable

def generator_numbers(text: str):
    # Регулярний вираз для виявлення дійсних чисел
    pattern = r'\b\d+\.\d+\b'
    # Знаходимо всі числа у тексті і повертаємо їх як генератор
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    # Використовуємо передану функцію для отримання генератора чисел
    numbers_generator = func(text)
    # Підсумовуємо всі числа з генератора
    total_income = sum(numbers_generator)
    return total_income

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

