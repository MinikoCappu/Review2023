import parse_true as pt
import pandas as pd
import os

def save(date):
    if os.path.isfile(f'{date}.csv'):
        df = pd.read_csv(f'{date}.csv')
    else:
        print("Подождите...")
        driver = pt.data(date)
        df = pt.finder(driver)
        df.to_csv(f'{date}.csv')
    return df

def cinema(date):
    ans = save(date).drop_duplicates(subset = "Theater")
    return ans['Theater'].tolist()

def movie(film, date):
    df = save(date)
    df = df.loc[(df['Movie'] == film),['Theater', 'Time']].values.tolist()
    return df

def Films(date):
    ans = save(date).drop_duplicates(subset = "Movie")
    return ans['Movie'].tolist()

def afisha(theater, date):
    df = save(date)
    df = df.loc[(df['Theater'] == theater),['Movie', 'Time']].values.tolist()
    return df

'''while True:
    start_text()
    argument = int(input())
    match argument:
        case 1:
            print("Введите желаемый день в формате YYYYMMDD")
            date = input()
            if os.path.isfile(f'{date}.csv'):
                df = pd.read_csv(f'{date}.csv')
            else:
                print("Подождите...")
                driver = data(date)
                df = finder(driver)
                df.to_csv(f'{date}.csv')
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