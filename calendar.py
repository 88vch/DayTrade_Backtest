from datetime import date
from calendar import monthrange
from backtest import constant
"""
calendar.py
    if you run this every sunday, 
        start=last_sunday(today-6)
        end=sunday(today)
"""

def get_x_week_start(which_week: str) -> str:
    if (which_week in constant.WEEK_TYPES):
        pass
    else: # assume user passed in specific format["YYYY-MM-DD"]
        pass

def get_x_week_end(which_week: str) -> str:
    if (which_week in constant.WEEK_TYPES):
        pass
    else: # assume user passed in specific format["YYYY-MM-DD"]
        pass

def get_this_week_start() -> str:
    x = get_this_week_end()
    
    if (x.day < 7):
        # remaining days to subtract from prev month to get exact start of week
        residual_days_to_subtract = 6 - x.day
        # get prev month's days
        if (x.month != 1):
            x.replace(month=(x.month - 1), 
                    day=(monthrange(x.year, x.month - 1)[1] - residual_days_to_subtract))
        else:
            x.replace(year=(x.year - 1),
                      month=12, 
                      day=(monthrange(x.year - 1, 12)[1] - residual_days_to_subtract))

def get_this_week_end() -> str:
    x = date.today()

