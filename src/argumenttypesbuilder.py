from src.argtype import ArgType
from src.argumenttypes import ArgumentTypes

class ArgumentTypesBuilder:
    def __init__(self):
        self.source_names = []
        self.arg_types = []

    def arg(self, source_name, string_arg_type):
        arg_type = self._string_arg_type_to_arg_type(string_arg_type)
        self._add_pair(source_name, arg_type)
        return self

    def build(self):
        return ArgumentTypes(self.source_names, self.arg_types)
    
    def _string_arg_type_to_arg_type(self, string_arg_type):
        match(string_arg_type):
            case 'table':
                return ArgType.WHOLE_TABLE
            case 'element':
                return ArgType.TABLE_ELEMENT

    def _add_pair(self, source_name, arg_type):
        self.source_names.append(source_name)
        self.arg_types.append(arg_type)

    def _source_name_to_index(self, source_name):
        return self.source_names.find(source_name)