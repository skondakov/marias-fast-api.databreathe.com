import logging
import sys
import os
from datetime import datetime

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

logs_dir = 'logs/'

# Create logs dir if it does not exist
logs_dir_exists = os.path.exists(logs_dir)
if not logs_dir_exists:
   os.makedirs(logs_dir)

# Use a different log file for every day for easier log reviews
log_filename = "log_" + datetime.today().strftime('%Y-%m-%d') + '.txt'

# Log everything with a DEBUG or higher logging level <
fh = logging.FileHandler(logs_dir + log_filename)
fh.setLevel(logging.DEBUG)

# Show logs in the strdout with a logging level of INFO or higher
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)

# Determine the logging format - add datetime & millisecond details + levels in the logs
formatter = logging.Formatter(
    '[%(asctime)s.%(msecs)03d] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
)

fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)