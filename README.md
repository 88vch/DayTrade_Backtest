# Backtest
automated hypothetical trades logged as backtests


### Notes
pull data from website on $(STOCK) <br />
dump data into a file (json) <br />
load data into dict() <br />
do something to data (check if setups are possible) <br />
finally post results to notion <br />

**AlphaVantage (Stock API)**
TIME_SERIES_DAILY: outputsize = [compact] | [full];
- can initially use [full] to grab ALL (20+ years) data from stock, then apply (i.e. backtest) your playbook's setups
TIME_SERIES_INTRADAY: interval = [1min], [5min], [15min], [30min]
- after initially doing a (very shallow) backtest, each day we should further confirm our setup's: 
    a. probability (success rate)
    b. validity (
        if probability keeps dropping and R:R is not sustaining the drop in probability, leading to a net negative trade setup, we should rethink the validity of this setup [
            by revising in the right direction, or knowing when to quit and move on
        ]
    )


### (RE)Sources
AlphaVantage (Stock API): https://www.alphavantage.co/documentation/ <br />
Notion API: https://developers.notion.com/reference/intro <br />
Machine Learning Financial Laboratory(MLfinLab): [https://www.mlfinlab.com/en/latest/backtest_overfitting/sevenpoint_protocol.html](https://www.mlfinlab.com/en/latest/backtest_overfitting/sevenpoint_protocol.html)
- how to backtest, how to ensure your testing is valid

### TODO
NEW NOTES;
- [crawler.py]
- validate AlphaVantage stock price accuracy


OLD NOTES;
- EITHER try to figure out why AlphaVantage Stock API is not giving correct data
- OR find a new free Stock API that will give you the correct data


NEW GOAL;
- futures (consistent pricing), but first: backtesting & data collection

OLD GOAL;
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
