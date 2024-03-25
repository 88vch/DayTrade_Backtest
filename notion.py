import requests

NOTION_TOKEN = "secret_o1hLhegKc6iIS7ZZdP0EhDfXn6XW24QL5u09lswDS2l"
DATABASE_ID = "ce17339287144dfdbcbf15d391ec5e96"
CURRENT_YEAR = 2024
SETUPS = [
    "Nathan's TT AM", 
    "ICT Power of 3 AM", 
    "ICT The One"
]
MAX_RISK_PERCENT = 1
MIN_REWARD_PERCENT = 1.5
TIME_UNITS = ["sec(s)", "min(s)", "hour(s)"]



headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

"""
Prints page information to the console.
"""
def show_pages(res: list) -> None:
    if res != []: # if database is not empty
        for page in res:
            page_id = page["id"]
            props = page["properties"]

            if props["Date"]["title"] != []:
                # Column 1
                date_text = props["Date"]["title"][0]["text"]["content"]
                # Column 2
                setup_multiSelect = props["Setup"]["multi_select"][0]["name"]
                # Column 3
                riskreward_text = props["R:R"]["rich_text"][0]["text"]["content"]
                # Column 4
                potentialPL_text = props["Potential P/L"]["rich_text"][0]["text"]["content"]
                # Column 5
                timeInTrade_text = props["Time in Trade"]["rich_text"][0]["text"]["content"]
                # Column 6
                timeSignature_multiSelect = props["Time Signature"]["multi_select"][0]["name"]
                
                json_str = date_text + "_" + setup_multiSelect + "_" + riskreward_text + "_" + potentialPL_text + "_" + timeInTrade_text + "_" + timeSignature_multiSelect

                print(date_text, setup_multiSelect, riskreward_text, potentialPL_text, timeInTrade_text, timeSignature_multiSelect)
            
            else: # props["Date"]["title"] == None implies done going through all pages' data!
                break

"""
Get's data from [num_pages] pages. Stops and returns early if actual pages in db does NOT exceed [num_pages].
"""
def get_pages(num_pages: int):
    global DATABASE_ID

    try:
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        # payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
        payload = {"page_size": num_pages}
        response = None

        response = requests.post(url, headers=headers, json=payload)

        # print(res.status_code)
        data = response.json()
        res = data["results"]
        return res
    except:
        print(f'request unsuccessful with status code [{response.status_code}]...')

"""
Checks if date is valid using [datetime] module.
"""
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
"""
def is_valid_setup(setup: str) -> bool:
    global SETUPS
    
    if setup in SETUPS:
        return True
    return False

"""
Checks if risk:reward ratio is valid amongst my own conditions.
"""
def is_valid_rr(rr_ratio: str) -> bool:
    global MAX_RISK_PERCENT
    global MIN_REWARD_PERCENT

    risk, reward = rr_ratio.split(":")

    if risk <= MAX_RISK_PERCENT and reward >= MIN_REWARD_PERCENT:
        return True
    return False

"""
Checks if risk:reward ratio is valid amongst my own conditions.
"""
def is_valid_pl(pl_ratio: str) -> bool:
    if pl_ratio[0] == "+":
        pass
    elif pl_ratio[0] == "-":
        pass

"""
Checks if risk:reward ratio is valid amongst my own conditions.
"""
def is_valid_timeTraded(time_traded: str) -> bool:
    pass

"""
Checks if risk:reward ratio is valid amongst my own conditions.
"""
def is_valid_timeSignature(time_unit: str) -> bool:
    global TIME_UNITS


"""
Given a dictionary, check if it's properly formatted. Return a boolean.
- More specific checks go in here.
Current properties:
    date_text = props["Date"]["title"][0]["text"]["content"]
    setup_multiSelect = props["Setup"]["multi_select"][0]["name"]
    riskreward_text = props["would want to take live?"]["rich_text"][0]["text"]["content"]
    riskreward_text = props["R:R"]["rich_text"][0]["text"]["content"]
    potentialPL_text = props["Potential P/L"]["rich_text"][0]["text"]["content"]
    timeInTrade_text = props["Time in Trade"]["rich_text"][0]["text"]["content"]
    timeSignature_multiSelect = props["Time Signature"]["multi_select"][0]["name"]
"""
def is_valid(data: dict):
    if (
        is_valid_date(data["date"]) and
        is_valid_setup(data["setup"]) and
        is_valid_rr(data["rr"]) and
        is_valid_pl(data["pl"]) and
        is_valid_timeTraded(data["time"]) and
        is_valid_timeSignature(data["timeSignature"])
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

    title = "Test Title"
    description = "Test Description"
    data = {
        "Date": {"title": [{"text": {"content": description}}]},
        "Setup": {"multi_select": [{"text": {"content": title}}]},
        "R/R": {"rich_text": [{"text": {"content": description}}]},
        "Potential P/L": {"rich_text": [{"text": {"content": description}}]},
        "Time in Trade": {"rich_text": [{"text": {"content": description}}]},
    }

    # res = create_page(data)
    res = get_pages(1)
    show_pages(res)