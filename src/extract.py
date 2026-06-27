import os
import pandas as pd
from config import RAW_DATA_PATH
from logger import logger

def extract(file_name):

    file_path = os.path.join(RAW_DATA_PATH, file_name)

    logger.info(f"Extracting {file_name}")

    df = pd.read_csv(file_path)

    logger.info(f"{len(df)} records extracted from {file_name}")

    return df