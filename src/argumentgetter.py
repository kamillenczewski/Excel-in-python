from src.datasets import DataSets
from src.argtype import ArgType
from src.argumenttypes import ArgumentTypes
from src.dictunion import dict_union

class ArgumentsGetter:
    def __init__(self, datasets: DataSets):
        self.datasets = datasets
        self.datasets_size = self.datasets.get_dataset_size()

    def get(self, all_source_names, argument_types_data: ArgumentTypes):
        if argument_types_data == None:
            self.source_names_and_arg_types = {name: ArgType.TABLE_ELEMENT for name in all_source_names}
        else:
            self.source_names_and_arg_types = dict_union(all_source_names, argument_types_data.source_names_and_arg_types, ArgType.TABLE_ELEMENT)
        
        self.all_source_names = all_source_names
        self.arg_types = list(self.arg_types_gen())

        return list(self.get_args_gen())

    def arg_types_gen(self):
        for name in self.all_source_names:
            yield self.source_names_and_arg_types[name]

    def get_args_gen(self):
        for element_index in range(self.datasets_size):
            yield list(self.get_args(element_index))

    def get_args(self, element_index):
        for source_name, arg_type in zip(self.all_source_names, self.arg_types):
            match(arg_type):
                case ArgType.WHOLE_TABLE:
                    yield self.datasets.get(source_name)
                case ArgType.TABLE_ELEMENT:
                    yield self.datasets.get_element(source_name, element_index)        