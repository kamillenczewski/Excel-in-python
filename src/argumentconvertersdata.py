class ArgumentConvertersData:
    def __init__(self, source_names, converters):
        self.source_names_and_converters = {
            source_name: converter 
            for source_name, converter 
            in zip(source_names, converters)
        }