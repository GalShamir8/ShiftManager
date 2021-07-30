import csv
import os
from logging import Logger

from common.handler import *


class EnterShift:
    def __init__(self, file_path):
        self.file_path = file_path
        self.isExist = os.path.exists(self.file_path)
        self.mode = 'w' if not self.isExist else 'a'

    def enter_new_shift(self):
        with open(self.file_path, mode=self.mode, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            if not self.isExist:
                writer.writeheader()
            try:
                update_table(writer)
                Logger.info(f'\nSaved successfully to file: {self.file_path}\n')
                # print(f'\nSaved successfully to file: {self.file_path}\n')
            except Exception as err:
                Logger.error(f'{repr(err)}')
                # print(f'{repr(err)}')