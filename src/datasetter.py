from collections.abc import Iterable
from setblock import SetBlock
from workbookdictionary import WorkbookDictionary

class DataSetter:
    def __init__(self, workbooks_dictionary):
        self.workbooks_dictionary: WorkbookDictionary = workbooks_dictionary

    def multiple_set(self, setblocks: Iterable[SetBlock]):
        for setblock in setblocks:
            self._single_set(setblock)

        return self
    
    def _single_set(self, setblock: SetBlock):
        path = setblock.destination.path
        sheet_name = setblock.destination.sheet_name
        string_range = setblock.destination.string_range
        data_generator = setblock.data_generator

        workbook = self.workbooks_dictionary[path]

        values = [value for value in data_generator]

        workbook.set(values, string_range, sheet_name=sheet_name)
