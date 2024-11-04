from src.conversionblock import ConversionBlock
from src.argumentgetter import ArgumentsGetter
from src.argumenttypes import ArgumentTypes
from src.datasets import DataSets
from src.argumentconvertersdata import ArgumentConvertersData
from src.argumentsconverter import ArgumentsConverter
from src.datamanager import DataManager


class DataConverter:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

        self.source_names = None
        self.destination_name = None
        self.convert_method = None

        self.argument_types_data = None
        self.argument_converters_data = None 

        self.datasets = None
        self.size = None

    def single_convert(self, conversion_block: ConversionBlock, argument_types_data: ArgumentTypes, argument_converters_data: ArgumentConvertersData):
        self.source_names = conversion_block.source_names
        self.destination_name = conversion_block.destination_name
        self.convert_method = conversion_block.convert_method
        
        self.argument_types_data = argument_types_data
        self.argument_converters_data = argument_converters_data

        self.datasets = self.get_datasets()
        self.size = self.datasets.get_dataset_size()

        output = self.get_output()

        self.data_manager.set_values(output, self.destination_name)

    def get_datasets(self):
        return DataSets(self.source_names, self.get_datasets_gen())
    
    def get_datasets_gen(self):
        for name in self.source_names:
            yield list(self.data_manager.get_values(name))

    def get_output(self):
        return list(self.get_output_gen())

    def get_output_gen(self):
        for args_set in self.get_args_sets():
            yield self.convert_method(*args_set)

    def get_args_sets(self):
        args_sets = ArgumentsGetter(self.datasets).get(self.source_names, self.argument_types_data)
        args_sets = ArgumentsConverter(args_sets).convert(self.source_names, self.argument_converters_data)
        return args_sets