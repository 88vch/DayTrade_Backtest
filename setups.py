SETUPS = [
    "Nate's TT AM", 
    "ICT Pow-3 AM", 
    "ICT The One"
]

SPECIFIC_SETUPS = {
    "day": ["Nate's TT AM", 
            "ICT Pow-3 AM", 
            "ICT The One"], 
    "swing": []
}


# How do you determine the characteristics for a "valid", "clean", & "successful" setup?
# - What are the quantifiable indicators?

# check that conditions for a setup have been given
# check that r:r and p/l are valid


"""
Given the chart for a day, give us all possible setups. 
- The following is the format for each-element (data) in the list to be returned. 
    data = {
        "Date": {"title": [{"text": {"content": test_date}}]},
        "Setup": {"multi_select": [{"name": test_setup}]},
        "R:R": {"rich_text": [{"text": {"content": test_rr}}]},
        "Potential P/L": {"rich_text": [{"text": {"content": test_pl}}]},
        "Time in Trade": {"rich_text": [{"text": {"content": test_time}}]},
        "Time Signature": {"multi_select": [{"name": test_timeSig}]}
        }
"""
def get_setups(data: dict) -> list:
    pass