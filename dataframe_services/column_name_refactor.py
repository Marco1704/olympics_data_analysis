import pandas as pd


def refactor_column_names(
        dataframe: pd.DataFrame,
        columns: dict) \
        -> pd.DataFrame:

    dataframe.rename(
            columns=columns,
            inplace=True)

    return \
        dataframe
