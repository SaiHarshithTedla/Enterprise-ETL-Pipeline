import pandas as pd
from logger import logger


def validate(df: pd.DataFrame, table_name: str):

    logger.info(f"Validating {table_name}")

    # Remove duplicate rows
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        logger.warning(f"{duplicate_count} duplicate rows found.")
        df = df.drop_duplicates()

    # Remove completely empty rows
    null_rows = df.isnull().all(axis=1).sum()

    if null_rows > 0:
        logger.warning(f"{null_rows} empty rows removed.")
        df = df.dropna(how="all")

    # Business Rules

    if table_name == "products":

        if "price" in df.columns:
            invalid = (df["price"] <= 0).sum()

            if invalid > 0:
                logger.warning(f"{invalid} invalid prices removed.")
                df = df[df["price"] > 0]

    if table_name == "order_items":

        if "quantity" in df.columns:
            invalid = (df["quantity"] <= 0).sum()

            if invalid > 0:
                logger.warning(f"{invalid} invalid quantities removed.")
                df = df[df["quantity"] > 0]

    logger.info(f"{table_name} validation completed.")

    return df