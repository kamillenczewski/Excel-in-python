from src.argtype import ArgType

class ArgumentTypes:
    def __init__(self, source_names: list[str], arg_types: list[ArgType]):
        
        self.source_names_and_arg_types = {
            source_name: arg_type 
            for source_name, arg_type 
            in zip(source_names, arg_types)
        }
