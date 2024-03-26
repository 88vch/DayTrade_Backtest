# Backtest
automated hypothetical trades logged as backtests


### Notes
pull data from website on $(STOCK) <br />
dump data into a file (json) <br />
load data into dict() <br />
do something to data (check if setups are possible) <br />
finally post results to notion <br />

### (RE)Sources
Stock API: https://www.alphavantage.co/documentation/ <br />
Notion API: https://developers.notion.com/reference/intro <br />

### TODO
- EITHER try to figure out why AlphaVantage Stock API is not giving correct data
- OR find a new free Stock API that will give you the correct data

- find free options data
    - once you have determined that you have found a trade you will take, 
    - DAY-TRADES: compare options volumes and choose option with
        1. expiry: 1 DTE
        2. high volume ("high" volume will depend on the day [news, etc...])
            - need a metric to reliably calculate that
        3. (trade-start) price: greater than $0.5, less than $2.5
    - SWING-TRADES: compare options volumes and choose option with 
        1. expiry: 
        2. volume:
        3. (trade-start) price: 
