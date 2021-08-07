import logging
import os

file_name = "logs.log"
file_path = os.getcwd() + f"{file_name}"

logs_format = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d %(funcName)s - %(message)s'

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format=logs_format,
    datefmt='%H:%M:%S'
)

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('\nLogger.%(levelname)s:  %(asctime)s  %(funcName)s -  %(message)s\n')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)
