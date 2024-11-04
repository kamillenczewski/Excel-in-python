from src.requests.request import Request
from src.conversionblock import ConversionBlock
from src.dataconverter import DataConverter
from src.argumenttypes import ArgumentTypes
from src.argumentconvertersdata import ArgumentConvertersData
from src.datamanager import DataManager

class ConvertRequest(Request):
    def __init__(self, conversionblock: ConversionBlock, argument_types_data: ArgumentTypes, argument_converters_data: ArgumentConvertersData):
        self.conversionblock = conversionblock
        self.argument_types_data = argument_types_data
        self.argument_converters_data = argument_converters_data

    def execute(self, data_manager: DataManager):
        DataConverter(data_manager).single_convert(self.conversionblock, self.argument_types_data, self.argument_converters_data)