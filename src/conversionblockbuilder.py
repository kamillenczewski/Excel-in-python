from src.conversionblock import ConversionBlock


class ConversionBlockBuilder:
    def __init__(self):
        self.source_names = []
        self.destination_name = None
        self.convert_method_ = None
    
    def source(self, name):
        self.source_names.append(name)
        return self
    
    def sources(self, *names):
        self.source_names = names
        return self

    def destination(self, name):
        self.destination_name = name
        return self

    def convert_method(self, value):
        self.convert_method_ = value
        return self 
    
    def build(self):
        return ConversionBlock(self.source_names, self.destination_name, self.convert_method_)
