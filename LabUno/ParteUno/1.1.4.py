# Введите одномерный целочисленный список. Найдите наибольший
# нечетный элемент. Найдите минимальный по модулю элемент списка.

def find_largest_odd_and_min_abs(numbers):
    largest_odd = None
    min_abs = None

    for num in numbers:
        if num % 2 != 0:
            if largest_odd is None or num > largest_odd:
                largest_odd = num

        if min_abs is None or abs(num) < abs(min_abs):
            min_abs = num

    return largest_odd, min_abs

input_list = input("Введите целочисленный список, разделенный запятыми: ")
numbers = list(map(int, input_list.split(',')))

largest_odd, min_abs = find_largest_odd_and_min_abs(numbers)

if largest_odd is not None:
    print(f"Наибольший нечётный элемент: {largest_odd}")
else:
    print("В списке нет нечётных элементов.")

print(f"Минимальный по модулю элемент: {min_abs}")