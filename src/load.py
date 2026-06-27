import pandas as pd
from sqlalchemy import create_engine, text
from config import DB_CONFIG
from logger import logger

# =====================================================
# Database Connection
# =====================================================

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/"
    f"{DB_CONFIG['database']}"
)

engine = create_engine(DATABASE_URL)

# =====================================================
# Clear Table Before Loading
# =====================================================

def clear_table(table_name):
    try:
        with engine.begin() as conn:
            conn.execute(
                text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE;")
            )

        logger.info(f"{table_name} truncated successfully.")

    except Exception as e:
        logger.error(f"Error truncating {table_name}: {e}")
        raise

# =====================================================
# Load Data
# =====================================================

def load(df: pd.DataFrame, table_name: str):

    try:
        # Clear existing data
        clear_table(table_name)

        # Load new data
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            chunksize=1000,
            method="multi"
        )

        logger.info(
            f"{table_name} loaded successfully ({len(df)} records)"
        )

    except Exception as e:
        logger.error(f"Error loading {table_name}: {e}")
        raise