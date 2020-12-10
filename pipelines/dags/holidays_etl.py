import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

def download_data():
    print
    r = requests.get("https://feiertage-api.de/api/?jahr=2021")
    data = r.json()
    print("execute request")
    return data

def processing_data():
    data = download_data()
    for state in data:
         print(state, '-----------')
         state_info = data[state]
         for holidays in state_info:
             print(holidays, state_info[holidays]['datum'])
    print('-----------')

def get_holidays_germany():
    r = requests.get("https://feiertage-api.de/api/?jahr=2021")
    data = r.json()
    print("auuu")
    for state in data:
         print(state, '-----------')
         state_info = data[state]
         for holidays in state_info:
             print(holidays, state_info[holidays]['datum'])
    print('-----------')

def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print("No holidays downloaded. Finishing execution")
        return False 

    # Primary Key Check
    if pd.Series(df['xx']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")

    # Check for nulls
    if df.isnull().values.any():
        raise Exception("Null values found")

    # Check that all timestamps are of yesterday's date
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, '%Y-%m-%d') != yesterday:
            raise Exception("xxxx")

    return True


def run_holidays_etl():
    print("test")
    
    # Validate
    if check_if_valid_data(song_df):
        print("Data valid, proceed to Load stage")