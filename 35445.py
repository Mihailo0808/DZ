import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox


class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        url = 'https://bank.gov.ua/ua/markets/exchangerates'
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Не вдалося отримати дані з сайту НБУ.")

        soup = BeautifulSoup(response.text, 'html.parser')
        usd_row = soup.find('td', string='840').find_parent('tr')
        if not usd_row:
            raise Exception("Не вдалося знайти курс для долара США.")

        exchange_rate = usd_row.find_all('td')[4].text.strip().replace(',', '.')
        return float(exchange_rate)

    def convert_to_usd(self, amount_in_uah):
        return amount_in_uah / self.exchange_rate

def convert_currency():
    try:
        amount_in_uah = float(entry.get())
        amount_in_usd = converter.convert_to_usd(amount_in_uah)
        result_label.config(
            text=f"{amount_in_uah:.2f} грн = {amount_in_usd:.2f} USD\n(Курс: {converter.exchange_rate:.4f} грн/дол.)")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректне число.")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {e}")

root = tk.Tk()
root.title("Конвертер валют")
root.geometry("400x250")
converter = CurrencyConverter()
tk.Label(root, text="Введіть суму в гривнях:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)
convert_button = tk.Button(root, text="Конвертувати", font=("Arial", 12), command=convert_currency)
convert_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)
root.mainloop()
