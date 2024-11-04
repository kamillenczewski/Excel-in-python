from src.argumentconvertersdata import ArgumentConvertersData
from src.dictunion import dict_union

class ArgumentsConverter:
    def __init__(self, args_sets: list[list]):
        self.args_sets = args_sets

    def convert(self, all_source_names, argument_converters_data: ArgumentConvertersData):
        if argument_converters_data == None:
            return self.args_sets

        self.source_names_and_converters = dict_union(all_source_names, argument_converters_data.source_names_and_converters, None)
        self.converters = list(self.get_converters_gen(all_source_names))

        return list(self.converted_arg_sets_gen())
                
    def get_converters_gen(self, all_source_names):
        for name in all_source_names:
            yield self.source_names_and_converters[name]

    def converted_arg_sets_gen(self):
        for arg_set in self.args_sets:
            yield list(self.converted_arg_set_gen(arg_set))

    def converted_arg_set_gen(self, arg_set):
        for arg, converter in zip(arg_set, self.converters):
            if converter == None:
                yield arg
            else:
                yield converter(arg)

