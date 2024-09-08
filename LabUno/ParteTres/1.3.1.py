# Требуется написать программу, которая вычисляет общую площадь стены
# комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
# потолок оклеивать не нужно.

def calculate_wall_area(room_length, room_width, room_height, window_area, door_area):

    wall_area = 2 * room_height * (room_length + room_width)
    total_area = wall_area - (window_area + door_area)

    return total_area

room_length = float(input("Введите длину комнаты (м): "))
room_width = float(input("Введите ширину комнаты (м): "))
room_height = float(input("Введите высоту комнаты (м): "))
window_area = float(input("Введите площадь окон (м²): "))
door_area = float(input("Введите площадь дверей (м²): "))

total_wall_area = calculate_wall_area(room_length, room_width, room_height, window_area, door_area)

print(f"Общая площадь стены для оклейки обоями: {total_wall_area:.2f} м²")