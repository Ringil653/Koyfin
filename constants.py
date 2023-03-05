PATH_to_tickers = 'C:/Users/filip/OneDrive/Pulpit/Giełdy i portfel/Giełdy/Investing/List_of_tickers.xlsx'

fin_categories = (
    ("reve", 2),
    ("gm", 4),
    ("ebitda", 6),
    ("ni", 8)
)

info_categories = {
    "name": '//*[@id="root"]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/div[1]/div[1]',
    "earnings_date": '//*[@id="quote-box-tab_i_0"]/div/div[1]/div/div',
    "sector": '//*[@id="quote-box-tab_i_1"]/div/div[1]/div/div',
    "industry": '//*[@id="quote-box-tab_i_2"]/div/div[1]/div/div',
    "last_rep_date": '//*[@id="root"]/div[1]/section/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[4]/div/div/div[1]/div[22]/div/div/div[2]',
    "cur_evebitda": '//*[@id="quote-box-tab_i_5"]/div/div[1]/div/div',
    "cur_pe": '//*[@id="quote-box-tab_i_6"]/div/div[1]/div/div'
}

dict_periods = {
    "-7Q": 8,
    "-6Q": 7,
    "-5Q": 6,
    "-4Q": 5,
    "-3Q": 4,
    "-2Q": 3,
    "-1Q": 2,
    "-curr": 1,
    "-ltm": 0,
}