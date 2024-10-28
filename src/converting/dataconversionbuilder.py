from collections.abc import Iterable
from src.converting.setblock import SetBlock
from src.converting.conversionblock import ConversionBlock
from src.converting.dataconverter import DataConverter
from src.converting.datasetter import DataSetter
from src.converting.locationsdictionary import LocationsDictionary
from src.converting.workbookdictionary import WorkbookDictionary
from src.intervalutil import indices_range

class DataConversionBuilder:
    def __init__(self):
        self.locations_dictionary = LocationsDictionary()
        self.conversion_blocks = []
        self.setblocks = []

    def location(self, name, location):
        self.locations_dictionary.add_location(name, location)
        return self

    def string_range(self, table_name, string_range_):
        self.locations_dictionary.set_string_range(table_name, string_range_)
        return self

    def path(self, table_name, path):
        self.locations_dictionary.set_path(table_name, path)
        return self

    def global_path(self, path):
        self.locations_dictionary.set_global_path(path)
        return self

    def path_for_all(self, path):
        self.locations_dictionary.set_path_for_all(path)
        return self

    def global_sheet_name(self, sheet_name):
        self.locations_dictionary.set_global_sheet_name(sheet_name)
        return self

    def convert(self, source_names, destination_name, convert_method):
        if not isinstance(source_names, Iterable):
            source_names = [source_names]

        sources = self._get_locations(source_names)
        destination = self._get_location(destination_name)

        self._add_conversion_block(sources, destination, convert_method)

        return self

    def set_data_generator(self, destination_name, data_generator):
        destination = self._get_location(destination_name)
        self._add_setblock(destination, data_generator)
        return self
        

    def execute(self):
        workbook_dictionary = WorkbookDictionary()

        DataConverter(workbook_dictionary).multiple_convert(self.conversion_blocks)
        DataSetter(workbook_dictionary).multiple_set(self.setblocks)

        workbook_dictionary.save()

    def _get_location(self, name):
        return self.locations_dictionary.get_location(name)

    def _get_locations(self, names):
        return self.locations_dictionary.get_locations(names)

    def _add_conversion_block(self, sources, destination, convert_method):
        self.conversion_blocks.append(ConversionBlock(sources, destination, convert_method))

    def _add_setblock(self, destination, data_generator):
        self.setblocks.append(SetBlock(destination, data_generator))
