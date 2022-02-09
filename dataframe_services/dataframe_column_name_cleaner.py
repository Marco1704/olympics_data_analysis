import pandas as pd


def get_clean_dataframe_column_names(
        dataframe: pd.DataFrame) \
        -> pd.DataFrame:

    for column_name in dataframe.columns:

        column_name.lower().replace(" ", "_").replace("-","_").replace(r"/","_").replace("\\","_").\
            replace(".","_").replace("$","").replace("%","")
    return \
        dataframe
