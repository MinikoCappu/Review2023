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

#shtuka dla drivera
def data(date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.irk.ru/afisha/cinema/"+date+"/#event=sked"
    driver.get(url)
    return driver

def sort_text():
    print('''1 - Какие есть кинотеатры
2 - Какие есть фильмы
3 - Фильмы в кинотеатре
4 - В каком кинотеатре есть фильм          
5 - Расписание фильма в кинотеатре
6 - В начало
''')

def next_step():
    print('''Дальнейшие действия:
Отсортировать - 1
Вернуться в начало - 2''')

def start_text():
    print('''Выберите действие:
Выгрузить день - 1
Завершить - 2''')

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

'''while True:
    start_text()
    argument = int(input())
    match argument:
        case 1:
            print("Введите желаемый день в формате YYYYMMDD")
            date = input()
            driver = data(date)
            df = finder(driver)
            next_step()
            argument_1 = int(input())
            match argument:
                case 1:
                    flag = True
                    while flag:
                        sort_text()
                        argument_2 = int(input())
                        match argument_2:
                            case 1:
                                ans = df.drop_duplicates(subset="Theater")
                                print(ans['Theater'])
                            case 2:
                                ans = df.drop_duplicates(subset="Movie")
                                print(ans['Movie'])
                            case 3:
                                w_th = input("Кинотеатр ")
                                print(df.loc[(df['Theater'] == w_th),['Movie', 'Time']])
                            case 4:
                                w_movie = input("Фильм ")
                                print(df.loc[(df['Movie'] == w_movie),['Theater', 'Time']])
                            case 5:
                                w_movie = input("Фильм ")
                                w_th = input("Кинотеатр ")
                                print(df.loc[(df['Theater'] == w_th) & (df['Movie'] == w_movie),['Movie', 'Time']])
                            case 6:
                                flag = False
                case 2:
                    print('return')
        case 2:
            print("exit")
            break
'''