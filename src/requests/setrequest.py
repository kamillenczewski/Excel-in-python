from src.requests.request import Request
from src.datasetter import DataSetter

class SetRequest(Request):
    def __init__(self, setblock):
        self.setblock = setblock

    def execute(self, locations_dictionary, workbook_dictionary):
        DataSetter(workbook_dictionary).single_set(self.setblock)