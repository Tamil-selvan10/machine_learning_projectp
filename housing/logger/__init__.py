import logging
from datetime import datetime
import os

LOG_DIR='housing_logs'
CURRENT_TIMESTAMP=f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'
LOG_FILE_NAME=f'log_{CURRENT_TIMESTAMP}.log'

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
