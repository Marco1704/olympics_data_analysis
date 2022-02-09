import os

import pandas

from file_folder_services.file_name_cleaner import get_clean_file_names


def generate_dictionary_of_dataframes_from_csv_folder(
        folder_path: str) -> dict:
    dictionary_of_dataframes = \
        dict()

    csv_files = \
        __get_all_csv_files_from_folder(
            folder_path)

    clean_csv_files = \
        get_clean_file_names(
            file_names=csv_files)

    for csv_file in clean_csv_files:
        dictionary_of_dataframes = \
            __add_dataframe(
                csv_file=csv_file,
                folder_name=folder_path,
                dictionary_of_dataframes=dictionary_of_dataframes)

    return \
        dictionary_of_dataframes


def __get_all_csv_files_from_folder(
        folder: str) \
        -> list:
    csv_files = \
        list()

    for file in os.listdir(folder):
        if file.endswith('.csv'):
            csv_files.append(
                file)
    return \
        csv_files



def __add_dataframe(
        csv_file: str,
        folder_name: str,
        dictionary_of_dataframes: dict) \
        -> dict:
    dataframe_name = \
        csv_file.replace(
            '.csv',
            '')

    csv_path = \
        os.path.join(
            folder_name,
            csv_file)

    dataframe = \
        pandas.read_csv(
            filepath_or_buffer=csv_path,
            dtype=str,
            encoding='cp1252')

    dictionary_of_dataframes.update(
        {dataframe_name: dataframe})

    return \
        dictionary_of_dataframes
