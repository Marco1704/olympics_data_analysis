import pandas as pd

from file_folder_services.path_generator import get_folder_path
from file_folder_services.timestamp_folder_creator import create_timestamp_folder


def export_concatenated_dataframe_data(
        dataframe: pd.DataFrame,
        file_name: str):

    folder_path = \
        get_folder_path(
            title_message='output_folder')

    csv_folder_path = \
        create_timestamp_folder(
            folder_path=folder_path)

    dataframe.to_csv(
        fr'{csv_folder_path}\{file_name}.csv',
        index=False)
