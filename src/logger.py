import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Create logs directory if it doesn't exist
LOGS_DIR = 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Set up root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Function to generate log file name with timestamp
def get_log_file_name():
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(LOGS_DIR, f'app_{current_time}.log')


# Define log file path and format
log_file = get_log_file_name()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create timed rotating file handler (1 file per day)
file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
