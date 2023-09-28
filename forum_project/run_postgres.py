from website_conf import local_settings
import psycopg2
import logging
from time import sleep
import os

logger = logging.getLogger(__name__)

config = {
    "host": os.getenv("DB_HOST", local_settings.DB_HOST),
    "dbname": os.getenv("DB_NAME", local_settings.DB_NAME),
    "user": os.getenv("DB_USER", local_settings.DB_USER),
    "password": os.getenv("DB_PASSWORD", local_settings.DB_PASSWORD),
    "port": os.getenv("DB_PORT", local_settings.DB_PORT)
}

# Connect to your postgres DB

def check_connection(retries: int) -> bool:
    """
    Check connection with database, before launching the whole app.
    """
    exc = ""
    i = 0
    while i < retries:
        try:
            conn = psycopg2.connect(**config)
            conn.close()
            return True
        except Exception as e:
            exc = e
            sleep(1)
            i +=1
            
    logger.error(f"{exc}")    
    return False

if __name__ == "__main__":
    retries = 5
    if check_connection(retries):
        logger.info("Postgres is ready! ✨ 💅")
    else:
        logger.error(f"We could not connect with to Postgres within {retries} tries.")
    

