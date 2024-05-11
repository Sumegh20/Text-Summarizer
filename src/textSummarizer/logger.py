import os, sys, logging
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H:%M:%S')}.log"
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    # filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] :: %(levelname)s :: %(module)s :: %(lineno)d :: [ %(message)s ]",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# logger = logging.getLogger('textSummarizerLogger')