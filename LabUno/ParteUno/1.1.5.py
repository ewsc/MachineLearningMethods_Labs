# Создайте словарь из строки ' Enjoy every moment' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть
# будут числа, соответствующие количеству вхождений данной буквы в
# строку

def create_char_count_dict(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


input_string = 'Enjoy every moment'
char_count_dict = create_char_count_dict(input_string)

print(char_count_dict)