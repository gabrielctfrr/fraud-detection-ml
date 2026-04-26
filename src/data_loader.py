import pandas as pd

def load_data(file_path:str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df

def _validate_data(df:pd.DataFrame) -> bool:
    if df.isnull().values.any():
        print('Data contains null values')
        return False
    if df.duplicated().any():
        print('Data contains duplicate values')
        return False
    return True 