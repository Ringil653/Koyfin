from constants import fin_categories, info_categories, dict_periods, PATH_to_tickers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import pandas as pd
import time
import xlsxwriter
import winsound
import pyautogui
import os
import cv2

PATH = r"C:\Users\filip\OneDrive\Pulpit\Koyfin_VM\chromedriver.exe"
options = Options()
options.headless = False
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(PATH, options=options)
action = ActionChains(driver)

list_company_data = []


def login_to_koyfin():
    """The function logs into koyfin and prepares webdriver to scrapp data"""
    driver.get("https://app.koyfin.com/login")
    type_login = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/form/div[2]/div[1]/div/div[2]/input')
    type_login.send_keys("filip.nitwinko@wp.pl")

    type_password = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/form/div[2]/div[2]/div/div[2]/input')
    type_password.send_keys("Bylejakie1")
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div/form/div[3]/button').click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('-')
    pyautogui.press('-')
    pyautogui.keyUp('ctrl')
    pyautogui.doubleClick(1892, 125)
    print("Login finalized")
    pyautogui.press('f11')


def scrapping(path_screenshots, icon_flag, sheet_name):

    def indicate_flag():
        pyautogui.screenshot('temp_screen.png')
        image = cv2.imread('temp_screen.png', cv2.IMREAD_COLOR)
        roi = image
        print(image.shape)
        # image = cv2.resize(image, (0, 0), fx=0.7, fy=0.7)
        template = cv2.imread(icon_flag, cv2.IMREAD_COLOR)
        # template = cv2.resize(template, (0, 0), fx=0.7, fy=0.7)

        method = cv2.TM_CCOEFF_NORMED
        result = cv2.matchTemplate(roi, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        width = template.shape[1]
        height = template.shape[0]

        threshold = 0.75
        # indicate place to click if flag is not found
        if max_val > threshold:
            top_left = max_loc
        else:
            top_left = (1000, 500)
        bottom_right = (top_left[0] + width, top_left[1] + height)
        pyautogui.click(bottom_right)
        print("image shape:", image.shape, "max val:", max_val, "max loc:", max_loc, "w:", width, "w:", height,
              "template shape:", template.shape, "bottom right:", bottom_right)

    list_of_tickers = pd.read_excel(PATH_to_tickers, usecols="A", sheet_name=sheet_name)
    counter = 0
    initial_counter = 2
    temp_counter = 1

    workbook = xlsxwriter.Workbook(path_screenshots)
    worksheet = workbook.add_worksheet("Sheet1")
    print("workbook and worksheet created")
    time.sleep(3)

    for b in range(int(list_of_tickers.size)):
        ticker = str((list_of_tickers.iat[b, 0]))
        counter = counter + 1
        print(counter, ticker)

        temp_counter += 1
        if temp_counter == 30:
            pyautogui.press("f5")
            time.sleep(8)
            temp_counter = 0

        # Search
        pyautogui.click(100, 550)  # click on search box # 580/620 without top box as standard # 380/420 for smaller screen, 560 for 90%
        time.sleep(0.5)
        pyautogui.press('backspace', presses=5)
        pyautogui.typewrite(ticker, 0.1)
        time.sleep(1)
        indicate_flag()
        time.sleep(5)
        pyautogui.screenshot(str(ticker) + ".png")
        try:
            pyautogui.screenshot(str(ticker + "2.png"), region=(250, 60, 1610, 1000))
        except:
            continue

        loc_xpath_values(id_numb)

        # Insert data to worksheet
        worksheet.write("A" + str(initial_counter), ticker)
        try:
            worksheet.insert_image("B" + str(initial_counter), str(ticker) + "2.png", {'x_scale': 0.7, 'y_scale': 0.7})
        except:
            worksheet.insert_image("B" + str(initial_counter), str(ticker) + ".png", {'x_scale': 0.7, 'y_scale': 0.7})
        """
        worksheet.write("C" + str(initial_counter), short_list)
        worksheet.write("W" + str(initial_counter), date)
        worksheet.write("X" + str(initial_counter), period)

        worksheet.write("Y" + str(initial_counter), revenue_minus_four)
        worksheet.write("Z" + str(initial_counter), revenue_minus_three)
        worksheet.write("AA" + str(initial_counter), revenue_minus_one)
        worksheet.write("AB" + str(initial_counter), revenue_latest)

        worksheet.write("AC" + str(initial_counter), gross_margin_four)
        worksheet.write("AD" + str(initial_counter), gross_margin_three)
        worksheet.write("AE" + str(initial_counter), gross_margin_one)
        worksheet.write("AF" + str(initial_counter), gross_margin_latest)

        worksheet.write("AG" + str(initial_counter), ebitda_minus_four)
        worksheet.write("AH" + str(initial_counter), ebitda_minus_three)
        worksheet.write("AI" + str(initial_counter), ebitda_minus_one)
        worksheet.write("AJ" + str(initial_counter), ebitda_latest)

        worksheet.write("AK" + str(initial_counter), net_income_four)
        worksheet.write("AL" + str(initial_counter), net_income_three)
        worksheet.write("AM" + str(initial_counter), net_income_one)
        worksheet.write("AN" + str(initial_counter), net_income_latest)
        """
        initial_counter = initial_counter + 38

    workbook.close()
    print("woorkbook closed")


def loc_xpath_values(id_number):
    """The function iterates over info categories and creates dict with xpath values for each searched webpage element"""
    temp_dict = {}
    for key, value in info_categories.items():
        try:
            page_value = driver.find_element(By.XPATH, value).text
        except NoSuchElementException:
            page_value = 0
        temp_dict[key] = page_value
        #print(key, page_value)
    for cat in fin_categories:
        for key, value in dict_periods.items():
            xpath_loc = f'//*[@id="{id_number}"]/div[{cat[1]}]/div/div[last()-{value}]/div/div/div'
            try:
                page_value = driver.find_element(By.XPATH, xpath_loc).text
            except NoSuchElementException:
                page_value = 0
            temp_dict[cat[0] + key] = page_value
            #print(cat[0], key, page_value)
    list_company_data.append(temp_dict)

login_to_koyfin()
id_numb = input("")
scrapping(path_screenshots='Z:/VM_1_FR.xlsx', icon_flag='France_icon.png', sheet_name="FR")
