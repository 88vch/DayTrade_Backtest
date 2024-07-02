import requests
from setups import SETUPS

NOTION_TOKEN = "secret_o1hLhegKc6iIS7ZZdP0EhDfXn6XW24QL5u09lswDS2l"
DATABASE_ID = "ce17339287144dfdbcbf15d391ec5e96"

CURRENT_YEAR = 2024 # for is_valid_date()
MAX_RISK_PERCENT = 1 # for is_valid_rr()
MIN_REWARD_PERCENT = 1.5 # for is_valid_rr()
TIME_UNITS = ["sec(s)", "min(s)", "hour(s)"]
MIN_PROFIT_CASH = 25
MAX_LOSS_CASH = 100


headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}



""" Displays page information to the console. """
def show_pages(res: list) -> None:
    if res == []:
        return

    # if database is not empty
    for page in res:
        page_id = page["id"]
        props = page["properties"]

        if props["Date"]["title"] != []:
            date_text = props["Date"]["title"][0]["text"]["content"] # Column 1
            setup_multiSelect = props["Setup"]["multi_select"][0]["name"] # Column 2
            riskreward_text = props["R:R"]["rich_text"][0]["text"]["content"] # Column 3
            potentialPL_text = props["Potential P/L"]["rich_text"][0]["text"]["content"] # Column 4
            timeInTrade_text = props["Time in Trade"]["rich_text"][0]["text"]["content"] # Column 5
            timeSignature_multiSelect = props["Time Signature"]["multi_select"][0]["name"] # Column 6
            
            json_str = date_text + "_" + setup_multiSelect + "_" + riskreward_text + "_" + potentialPL_text + "_" + timeInTrade_text + "_" + timeSignature_multiSelect
            print(f'{date_text} {setup_multiSelect}\t{riskreward_text} {potentialPL_text} {timeInTrade_text} {timeSignature_multiSelect}')
        
        else: # props["Date"]["title"] == None implies done going through all pages' data!
            break

""" Get's data from [num_pages] pages. Stops and returns early if actual pages in db does NOT exceed [num_pages]. """
def get_pages(num_pages: int):
    global DATABASE_ID

    try:
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        # payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
        payload = {"page_size": num_pages}
        response = None

        response = requests.post(url, headers=headers, json=payload)

        # print(response.status_code)
        data = response.json()
        return data["results"]
    except:
        print(f'request unsuccessful with status code [{response.status_code}]...')

""" Checks if date is valid using [datetime] module. """
def is_valid_date(date: str) -> bool:
    global CURRENT_YEAR
    import datetime

    date = date.split("/")
    date = [int(elem) for elem in date]
    try:
        newDate = datetime.datetime(year=date[2], month=date[0],day=date[1])
        if date[2] > CURRENT_YEAR:
            return False
        return True
    except ValueError:
        return False

"""
Checks if setup is valid amongst setups in rotation.
- a setup is valid if it exists amongst our global SETUPS
"""
def is_valid_setup(setup: str) -> bool:
    global SETUPS
    
    if setup in SETUPS:
        return True
    return False

"""
Checks if risk:reward ratio is valid amongst my own conditions.
- A R:R Ratio is valid iff
    Risk:   less than or equal to MAX_RISK_PERCENT
    Reward: greater than or equal to MIN_REWARD_PERCENT
"""
def is_valid_rr(rr_ratio: str) -> bool:
    global MAX_RISK_PERCENT
    global MIN_REWARD_PERCENT

    risk, reward = rr_ratio.split(":")

    if float(risk) <= MAX_RISK_PERCENT and float(reward) >= MIN_REWARD_PERCENT:
        return True
    return False

"""
Checks if profit/loss is valid amongst my own conditions.
- A P&L is valid iff 
    Profit: gives a profit greater than $MIN_PROFIT_CASH
    Loss:   gives a loss less than $MAX_LOSS_CASH
"""
def is_valid_pl(pl_ratio: str) -> bool:
    global MIN_PROFIT_CASH
    global MAX_LOSS_CASH
    
    pm_symbols = ["+", "-"]
    first_char = pl_ratio[0]
    
    if first_char in pm_symbols:
        if first_char == "+":
            if int(pl_ratio[1:]) > MIN_PROFIT_CASH: # return true if profit greater than MIN_PROFIT_CASH
                return True
            return False
        else:
            if int(pl_ratio[1:]) < MAX_LOSS_CASH: # true if loss less than MAX_LOSS_CASH
                return True
            return False
    return False

""" Checks if time in trade is valid amongst my own conditions. (Currently just returns True) """
def is_valid_timeTraded(time_traded: str) -> bool:
    return True

""" Checks if time signature is valid amongst my own conditions. """
def is_valid_timeSignature(time_unit: str) -> bool:
    global TIME_UNITS

    if time_unit in TIME_UNITS:
        return True
    return False


"""
Given a dictionary, check if it's properly formatted. Return a boolean.
- More specific checks go in here.
Current properties:
    date_text = props["Date"]["title"][0]["text"]["content"]
    setup_multiSelect = props["Setup"]["multi_select"][0]["name"]
    riskreward_text = props["R:R"]["rich_text"][0]["text"]["content"]
    potentialPL_text = props["Potential P/L"]["rich_text"][0]["text"]["content"]
    timeInTrade_text = props["Time in Trade"]["rich_text"][0]["text"]["content"]
    timeSignature_multiSelect = props["Time Signature"]["multi_select"][0]["name"]
"""
def is_valid(data: dict):
    if (
        is_valid_date(data["Date"]["title"][0]["text"]["content"]) and
        is_valid_setup(data["Setup"]["multi_select"][0]["name"]) and
        is_valid_rr(data["R:R"]["rich_text"][0]["text"]["content"]) and
        is_valid_pl(data["Potential P/L"]["rich_text"][0]["text"]["content"]) and
        is_valid_timeTraded(data["Time in Trade"]["rich_text"][0]["text"]["content"]) and
        is_valid_timeSignature(data["Time Signature"]["multi_select"][0]["name"])
    ):
        return True
    return False

"""
Given a proper dictionary (formatted according to db col-names), put it into the notion db.
"""
def create_page(data: dict):
    url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
    res = requests.post(url, headers=headers, json=payload)
    # print(res.status_code)
    return res

if __name__ == "__main__":
    test_date = "03/28/2024"
    test_setup = "ICT The One"
    test_rr = "1:4"
    test_pl = "+75"
    test_time = "41.5"
    test_timeSig = "sec(s)"

    data = {
        "Date": {"title": [{"text": {"content": test_date}}]},
        "Setup": {"multi_select": [{"name": test_setup}]},
        "R:R": {"rich_text": [{"text": {"content": test_rr}}]},
        "Potential P/L": {"rich_text": [{"text": {"content": test_pl}}]},
        "Time in Trade": {"rich_text": [{"text": {"content": test_time}}]},
        "Time Signature": {"multi_select": [{"name": test_timeSig}]}
    }

    if is_valid(data):
        create_page(data)
    else:
        print(f"data is not valid!")
    # res = get_pages(5)
    # show_pages(res)