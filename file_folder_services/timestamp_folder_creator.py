import os
from datetime import datetime


def create_timestamp_folder(
        folder_path:str)\
        -> str:
    today_time = \
        datetime.today()

    folder_name = \
        f'{today_time.strftime("%b%d%Y%H%M%S")}\\'

    timestamp_folder_path = \
        os.path.join(
            folder_path,
            folder_name)

    try:
        os.mkdir(
            timestamp_folder_path)

    except FileExistsError:
        print(
            'Target folder already exists.')

    return \
        timestamp_folder_path
