import os
from csv import DictReader
from logging import Logger

from common.handler import header


class Status:
    def __init__(self, file_path):
        self.file_path = file_path
        self.isExist = os.path.exists(self.file_path)

    def show_status(self):
        if not self.isExist:
            Logger.info("No status to display")
        else:
            with open(self.file_path, newline='') as csvfile:
                reader = DictReader(csvfile)
                for table_title in header:
                    print(table_title.rjust(12), end='  |  ')
                print()
                for row in reader:
                    for cell in header:
                        print(row[cell].rjust(12), end='  |  ')
                    print()

