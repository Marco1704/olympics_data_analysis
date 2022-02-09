import pandas as pd


def get_clean_dataframe_column_names(
        dataframe: pd.DataFrame) \
        -> pd.DataFrame:

    dataframe.columns = dataframe.columns.str.lower().str.replace(" ", "_").str.replace("-","_").str.replace(r"/","_").\
        str.replace("\\","_").str.replace(".","_").str.replace("$","").str.replace("%","")


    return \
        dataframe
