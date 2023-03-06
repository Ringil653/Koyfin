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
sheet_name = 0
bottom_right = 0


def login_to_koyfin():
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