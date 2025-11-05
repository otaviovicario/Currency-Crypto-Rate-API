"""
Currency & Crypto Rate API
Author: Otavio Vicario
Version: 1.0
Description: Fetches real-time exchange rates for any currency or cryptocurrency to BRL
Dependencies: requests
"""

import requests


def get_price(currency_pair: str) -> dict:
    url = "https://economia.awesomeapi.com.br/json/last/"
    response = requests.get(f"{url}{currency_pair}")
    response.raise_for_status()
    data = response.json()

    if currency_pair.replace("-", "") not in "".join(data.keys()):
        raise ValueError(f"Currency pair {currency_pair} not found in API response.")

    for item in data.values():
        if isinstance(item, dict): 
            return {
                "moeda": item.get("code","") + item.get("codein",""),
                "valor": round(float(item.get("bid",0)),2),
                "nome": item.get("name","Unknown")
            }
    raise ValueError("Unexpected API response format.")


if __name__ == "__main__":
    try:
        currency_pairs = input("Enter the currency pair code (e.g., BTC-BRL): ").strip().upper()
        price = get_price(currency_pairs)
        print(price)

    except requests.exceptions.RequestException as e:
        print("API connection error:", e)

    except (KeyError, ValueError):
        print("Error processing currency data.")
