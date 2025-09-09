import re


class UnknownOperationError(Exception):
    """ Створення власного винятку """

    def __init__(self, message="Невідома операція! Використовуйте тільки такі оператори для обчислення: +, -, *, /"):
        super().__init__(message)


class Calculator:
    """ Клас калькулятор з магічними методами для арифметичних операцій """

    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return Calculator(self.value / other.value)

    def __str__(self):
        return f"{self.value}"


def main():
    """ Функція, яка обробляє користувацький та винятки, також виконує арифметичні операції за допомогою класу Calculator. """
    while True:
        try:
            # Запрошуємо введення данних від користувача
            expression = input("Введіть вираз для обчислення (напр., 3 + 4) або 'exit' для виходу: ")

            # Умова виходу з программи:
            if expression.lower() == "exit":
                print("Вихід з калькулятора")
                break

            # Використання регулярного виразу для його прсингу.
            # (-?\d+\.?\d*) - знаходить число (ціле або десяткове, можу бути від'ємне)
            # \s*([+\-*/])\s* - знаходить оператор з пробілами навколо

            match = re.match(r'(-?\d+\.?\d*)\s*([+\-*/])\s*(-?\d+.?\d*)', expression)

            if not match:
                raise ValueError("Некорректний формат виразу. Використовуйте 'число оператор число'.")

            num1_str, operator, num2_str = match.groups()

            # Створення об'єктів з отриманих чисел
            num1 = Calculator(num1_str)
            num2 = Calculator(num2_str)

            # Виклик відповідного магічного методу
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                raise UnknownOperationError()

            # Обробка винятку переповнення
            if abs(result.value) == float('inf'):
                raise OverflowError("Результат обчислення занадто великий або занадто малий")

            print(f"Результат: {result}")

        except ValueError as ex:
            print(f"Помилка: {ex}")
        except ZeroDivisionError as ex:
            print(f"Помилка: {ex}")
        except UnknownOperationError as ex:
            print(f"Помилка: {ex}")
        except OverflowError as ex:
            print(f"Помилка: {ex}")
        except Exception as ex:
            print(f"Сталася неочікувана помилка: {ex}")


main()
