from src.argumentconvertersdata import ArgumentConvertersData

class ArgumentConvertersBuilder:
    def __init__(self):
        self.source_names = []
        self.converters = []

    def arg(self, source_name, converter):
        self.source_names.append(source_name)
        self.converters.append(converter)
        return self

    def build(self):
        return ArgumentConvertersData(self.source_names, self.converters)