import time

from extract import extract
from transform import transform
from validate import validate
from load import load
from logger import logger

FILES = {
    "customers.csv": "customers",
    "products.csv": "products",
    "orders.csv": "orders",
    "order_items.csv": "order_items"
}

def main():

    start = time.time()

    logger.info("=" * 60)
    logger.info("RetailX Enterprise ETL Started")
    logger.info("=" * 60)

    for file_name, table_name in FILES.items():

        try:
            logger.info(f"Processing {table_name}...")

            df = extract(file_name)
            df = transform(df)
            df = validate(df, table_name)
            load(df, table_name)

            logger.info(f"{table_name} completed successfully.\n")

        except Exception as e:
            logger.exception(f"Failed processing {table_name}: {e}")

    end = time.time()

    logger.info("=" * 60)
    logger.info(f"Execution Time: {round(end-start, 2)} seconds")
    logger.info("RetailX ETL Completed Successfully")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()