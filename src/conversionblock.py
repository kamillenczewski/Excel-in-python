class ConversionBlock:
    def __init__(self, source_names, destination_name, convert_method):
        self.source_names = source_names
        self.destination_name = destination_name
        self.convert_method = convert_method