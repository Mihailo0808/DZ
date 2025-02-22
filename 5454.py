# Спочатку встановлюємо бібліотеку (якщо ще не встановлена)

import colorama
from colorama import Fore, Back, Style

# Ініціалізація модуля colorama
colorama.init()

# Виконуємо інтроспекцію модуля за допомогою функції dir()
print("Атрибути та методи модуля colorama:")
print(dir(colorama))

# Приклад використання атрибутів для форматування тексту в консолі
print(Fore.RED + "Цей текст буде червоним." + Fore.RESET)
print(Back.GREEN + "Цей текст має зелений фон." + Back.RESET)
print(Style.BRIGHT + "Цей текст яскравий." + Style.RESET_ALL)

# Завершуємо використання colorama, якщо потрібно
colorama.deinit()
