class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} увімкнено.")
        else:
            print(f"{self.name} вже увімкнено.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} вимкнено.")
        else:
            print(f"{self.name} вже вимкнено.")


class Smartphone(Device):
    def make_call(self, number):
        if self.is_on:
            print(f"Дзвінок на {number} з {self.name}...")
        else:
            print(f"{self.name} вимкнений. Спочатку увімкніть його.")


class Laptop(Device):
    def open_program(self, program_name):
        if self.is_on:
            print(f"Запуск програми {program_name} на {self.name}...")
        else:
            print(f"{self.name} вимкнений. Спочатку увімкніть його.")


phone = Smartphone("iPhone 13")
laptop = Laptop("MacBook Pro")

phone.turn_on()
phone.make_call("+380123456789")
laptop.open_program("VS Code")
laptop.turn_on()
laptop.open_program("VS Code")
