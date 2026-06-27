import pandas as pd
from logger import logger

def transform(df):

    before = len(df)

    df = df.drop_duplicates()
    df = df.dropna(how="all")

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype(str).str.strip()

    after = len(df)

    logger.info(f"Transformation completed. {before-after} duplicate rows removed.")

    return df