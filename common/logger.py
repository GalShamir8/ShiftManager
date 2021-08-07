import logging
logs_format = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d %(funcName)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename="logs.log", filemode='w', format=logs_format)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s %(funcName)s - %message)s')
# logger_man = logging.StreamHandler()
# logger_man.setFormatter(formatter)
logger = logging.getLogger(__name__)
# logger.addHandler(logger_man)
logger.setLevel(logging.DEBUG)