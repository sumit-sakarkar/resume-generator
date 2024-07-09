import logging
from logger import logger  # Import the logger setup


def run_app():
    try:
        logger.info("Application started")
        # Application logic here
        logger.info("Application finished successfully")
    except Exception as e:
        logger.error("An error occurred", exc_info=True)

if __name__ == "__main__":

    run_app()