result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print(f"Помилка TypeError: Неправильний тип даних ({a}, {b})")
        return None
    if a < b:
        print(f"Помилка ValueError: Число 'a' повинно бути не менше 'b' ({a} < {b})")
        return None
    if b > 100:
        print(f"Помилка IndexError: Число 'b' не повинно бути більше 100 ({b})")
        return None
    if b == 0:
        print(f"Помилка: Ділення на нуль ({a} / {b})")
        return None
    return a / b

data = {10: 2, 2: 5, 18: 0, 8: 4}

for key, value in data.items():
    res = divider(key, value)
    if res is not None:
        result.append(res)

print(result)