# Вводится строка, содержащая буквы, целые неотрицательные числа и
# иные символы. Требуется все числа, которые встречаются в строке
# отдельно вывести на экран. Строка может содержать пробелы.

import re

def extract_numbers(input_string):
    numbers = re.findall(r'\d+', input_string)
    return numbers

input_string = input("Введите строку: ")
numbers = extract_numbers(input_string)

if numbers:
    print("Найденные числа:")
    for number in numbers:
        print(number)
else:
    print("Чисел не найдено.")