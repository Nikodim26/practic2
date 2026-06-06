import json

import requests


def get_currency_rate(currency):
    response = requests.get(f"https://www.cbr-xml-daily.ru/daily_json.js")
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate")
    rez = response.json()['Valute'].get(currency)  # dict

    return {
        "currency_code": rez['CharCode'],
        "rate": rez['Value']
    }

if __name__ == '__main__':
    print(json.dumps(get_currency_rate('USD'),ensure_ascii=False, indent=4))
