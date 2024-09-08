# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса.

class Phone:
    phone_count = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        Phone.phone_count += 1

    def call(self, number):
        print(f"{self.brand} {self.model} звонит на номер {number}.")

    def send_message(self, number, message):
        print(f"{self.brand} {self.model} отправляет сообщение '{message}' на номер {number}.")

    @classmethod
    def get_phone_count(cls):
        return cls.phone_count

    @staticmethod
    def is_valid_number(number):
        return isinstance(number, str) and number.isdigit() and len(number) >= 10

phone1 = Phone("Apple", "iPhone 13", 999)
phone2 = Phone("Samsung", "Galaxy S21", 799)

phone1.call("1234567890")
phone2.send_message("0987654321", "Привет!")

print(f"Общее количество телефонов: {Phone.get_phone_count()}")

number_to_check = "1234567890"
if Phone.is_valid_number(number_to_check):
    print(f"{number_to_check} является валидным номером.")
else:
    print(f"{number_to_check} не является валидным номером.")