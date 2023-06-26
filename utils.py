import requests
import json
from config import keys

class exception1(Exception):
    pass

class Cryptoconverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            base_ticket = keys[base]
        except KeyError:
            raise exception1("Неверно набрана валюта")

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise exception1("Неверно набрана валюта")

        try:
            amount = float(amount)
        except ValueError:
            raise exception1('Целое число пожалуйста')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * int(amount)