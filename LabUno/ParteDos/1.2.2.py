# Напишите функцию, которая будет принимать один аргумент. Если
# в функцию передаётся кортеж, то посчитать его количество элементов.
# Если список, то найти сумму до первого нулевого элемента.
# Число – вывести его в обратном порядке.
# Строка – кол-во слов. Определить какой символ в строке встречается
# чаще всего.
# Сделать проверку со всеми этими случаями.

from collections import Counter

def process_argument(arg):

    if isinstance(arg, tuple):
        return f"Количество элементов в кортеже: {len(arg)}"

    elif isinstance(arg, list):
        total = 0
        for num in arg:
            if num == 0:
                break
            total += num
        return f"Сумма до первого нулевого элемента: {total}"

    elif isinstance(arg, int):
        return f"Число в обратном порядке: {str(arg)[::-1]}"

    elif isinstance(arg, str):
        words = arg.split()
        word_count = len(words)
        most_common_char = Counter(arg).most_common(1)[0]

        return (f"Количество слов в строке: {word_count}, "
                f"Самый частый символ: '{most_common_char[0]}' (встречается {most_common_char[1]} раз)")

    else:
        return "Недопустимый тип аргумента."

print(process_argument((1, 2, 3, 4)))
print(process_argument([1, 2, 0, 4, 5]))
print(process_argument(12345))
print(process_argument("Some strings for you."))