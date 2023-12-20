from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import os

#shtuka dla drivera
def data(date):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    url = "https://www.irk.ru/afisha/cinema/"+date+"/#event=sked"
    driver.get(url)
    return driver

def Take_info(page, df):
    if "cinema-list__item j-film-row" in page.get_attribute('class'):
        movie = page.find_element(By.CLASS_NAME, "cinema-list__title").text
        theater_1 = page.find_elements(By.CLASS_NAME, "cinema-table__tr")
        for theater in theater_1:
            theater_true = theater.find_element(By.CLASS_NAME, "cinema-table__th").text
            times = theater.find_elements(By.CLASS_NAME, "time-list__item")
            for time in times:
                df.loc[len(df.index)] = [movie, theater_true, time.text]

def finder(driver):
    df = pd.DataFrame(columns = ['Movie','Theater','Time'])
    movies = driver.find_elements(By.CLASS_NAME, "cinema-list__item")
    counter = 0
    for foo in movies: #для фильма и в каких местах идет
        Take_info(foo, df)
    driver.close()
    return df

def table(date):
    driver = data(date)
    df = finder(driver)
    return df
