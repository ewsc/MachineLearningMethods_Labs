def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль!"
    except TypeError:
        return "Ошибка: Неверные типы данных. Ожидались числа."
    else:
        return f"Результат: {result}"
    finally:
        print("Выполнение блока finally. Завершение функции.\n")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 'a'))