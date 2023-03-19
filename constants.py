PATH_to_tickers = 'C:/Users/filip/OneDrive/Pulpit/Giełdy i portfel/Giełdy/Investing/List_of_tickers.xlsx'
PATH_TO_CHROMEDRIVER = r"C:\Users\filip\OneDrive\Pulpit\Koyfin_VM\chromedriver.exe"

MONTHS_AS_VALUES = {'Jan': 1,
                    'Feb': 2,
                    'Mar': 3,
                    'Apr': 4,
                    'May': 5,
                    'Jun': 6,
                    'Jul': 7,
                    'Aug': 8,
                    'Sep': 9,
                    'Oct': 10,
                    'Nov': 11,
                    'Dec': 12
                    }

FIN_CATEGORIES = (
    ("reve", 2),
    ("gm", 4),
    ("ebitda", 6),
    ("ni", 8)
)

INFO_CATEGORIES = {
    "ticker": '//*[@id="root"]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[1]/span',
    "name": '//*[@id="root"]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/div[1]/div[1]',
    "earnings_date": '//*[@id="quote-box-tab_i_0"]/div/div[1]/div/div',
    "sector": '//*[@id="quote-box-tab_i_1"]/div/div[1]/div/div',
    "industry": '//*[@id="quote-box-tab_i_2"]/div/div[1]/div/div',
    "last_rep_date": '//*[@id="root"]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div/div/div[1]/div[last()-1]/div/div/div[2]',
    "cur_evebitda": '//*[@id="quote-box-tab_i_5"]/div/div[1]/div/div',
    "cur_pe": '//*[@id="quote-box-tab_i_6"]/div/div[1]/div/div',
    "forward_pe": '//*[@id="quote-box-tab_i_4"]/div/div[1]/div/div'
}

DICT_PERIODS = {
    "_minus_7Q": 8,
    "_minus_6Q": 7,
    "_minus_5Q": 6,
    "_minus_4Q": 5,
    "_minus_3Q": 4,
    "_minus_2Q": 3,
    "_minus_1Q": 2,
    "_curr": 1,
    "_ltm": 0,
}
