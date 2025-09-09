import os


def calculate_average_from_file(file_name):
    """
    Зчитує числа з файлу та вираховує середнє арифметичне.
    Обробляє такі винятки, як FileNotFoundError та ValueError.

    Args:
        file_name (str): Ім'я текстового файлу

    Returns:
        float or None: Пораховане середнє арифметичне або None якщо помилки виявлено.
    """
    total = 0
    count = 0

    try:
        with open(file_name, 'r', encoding='utf-8') as lines:
            lines = lines.readlines()

        # Можливість обробки порожнього файлу та файлу, що містить один рядок.
        if not lines:
            print(f"Помилка: Файл '{file_name} порожній.'")
            return None

        for line in lines:
            # Очищення наших даних з файлу від не числових значень, а також перевірка чи на файл не пустий
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            total += float(cleaned_line)
            count += 1

    except FileNotFoundError:
        print(f"Помилка: Файл '{file_name}' не знайдено.")
        return None
    except ValueError:
        print(f"Помилка: Файл '{file_name}' містить нечислові дані.")
        return None
    except Exception as error:
        print(f"Виникла невідома помилка: {error}")
        return None

    # Вичислення та повернення значення середнього арифметичного
    if count > 0:
        return total / count
    else:
        print(f"Помилка: Файл '{file_name}' не містить чисел.")
        return None


def process_file_and_print_result(filename):
    """
    Викликає головну функцію, прораховує результат та виводить до консолі.
    """
    print(f"Спроба обробки файлу '{filename}'...")
    average = calculate_average_from_file(filename)
    if average is not None:
        print(f"Середнє арифметичне чисел у файлі: {average}")
    print("_______________________________________")


# Указуємо шлях до файлу з яким потрібно працювати
file_path = "2_list_of_numbers.txt"

print(f"Приклад якщо '{file_path}' не знайдено\n")
process_file_and_print_result(file_path)

print(f"Створюємо та перевіряємо файл '{file_path}' з числами\n")
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("10\n")
    file.write("20.5\n")
    file.write("30\n")
    file.write("38.8\n")

# Приклад використання з дійсним файлом
process_file_and_print_result(file_path)

print(f"Приклад використання якщо файл '{file_path}' містить не тільки числа\n")
with open(file_path, 'w', encoding='utf-8') as file:
    file.write("10\n")
    file.write("Hello!\n")
    file.write("205\n")

process_file_and_print_result(file_path)

print(f"Спроба використання якщо файл '{file_path}' порожній\n")
with open(file_path, 'w', encoding='utf-8') as file:
    pass  # Створює порожній файл

process_file_and_print_result(file_path)

# Видалення файлу
os.remove(file_path)
