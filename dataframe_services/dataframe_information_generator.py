import pandas as pd


def generate_dataframe_information(
        dataframe: pd.DataFrame):
    print(
        dataframe.head(),
        dataframe.info(),
        dataframe.describe()
    )

