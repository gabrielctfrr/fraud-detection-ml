import pandas as pd

COLS_NUM = ['distance_from_home', 'distance_from_last_transaction', 'ratio_to_median_purchase_price']
COLS_CAT = ['repeat_retailer', 'used_chip', 'used_pin_number', 'online_order', 'fraud']

def load_data(file_path)->pd.DataFrame:
    df = pd.read_csv(file_path)
    df = _convert_types(df)
    _validate(df)
    return df

def _convert_types(df: pd.DataFrame)->pd.DataFrame:
    for col in COLS_NUM:
        df[col] = df[col].astype(int)
    return df

def _validate(df: pd.DataFrame)-> None:
    if df.isnull().sum().any():
        raise ValueError("Dataset contém valores ausentes.")

    if df.duplicated().sum() > 0:
        raise ValueError("Dataset contém linhas duplicadas.")

    for col in COLS_NUM:
        if df[col].min() < 0:
            raise ValueError(f"{col}: contém valores negativos.")

    for col in COLS_CAT:
        invalidos = df[~df[col].isin([0, 1])]
        if len(invalidos) > 0:
            raise ValueError(f"{col}: contém valores fora de [0, 1].")

