import pandas as pd

from dataframe_services.column_name_refactor import refactor_column_names
from dataframe_services.dataframe_column_name_cleaner import get_clean_dataframe_column_names


def left_merge_dataframe(
        dictionary_of_dataframes: dict) \
        -> pd.DataFrame:

    left_dataframe = \
        dictionary_of_dataframes[
            'athlete_events']
    right_dataframe = \
        dictionary_of_dataframes[
            'noc_regions']

    merged_dataframe = \
        pd.merge(
            left=left_dataframe,
            right=right_dataframe,
            on='NOC')

    dataframe_with_clean_columns = \
        get_clean_dataframe_column_names(
            dataframe=merged_dataframe)


    return \
        dataframe_with_clean_columns
