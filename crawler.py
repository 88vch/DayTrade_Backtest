import json
import requests

DATE = "03-27-2024"
SYMBOL = "NVDA"

def run():
    global DATE
    global SYMBOL

    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=1min&adjusted=true&extended_hours=false&outputsize=full&apikey=8HPH4D1XJP58NZHV'
    r = requests.get(url)
    data = r.json()

    print(data)

    with open(f'results/{DATE}_{SYMBOL}.json', 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    run()