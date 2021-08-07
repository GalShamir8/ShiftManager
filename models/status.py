import os
from csv import DictReader

from common.handler import print_table
from common.logger import logger


class Status:
    def __init__(self, file_path):
        self.file_path = file_path
        self.isExist = os.path.exists(self.file_path)

    def show_status(self):
        if not self.isExist:
            logger.info("No status to display")
        else:
            with open(self.file_path, newline='') as csvfile:
                reader = DictReader(csvfile)
                print_table(reader)

