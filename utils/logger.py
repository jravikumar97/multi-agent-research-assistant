import logging
from datetime import datetime

# Configure logger
logging.basicConfig(level=logging.INFO)

def log_with_timestamp(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"{timestamp}: {message}")