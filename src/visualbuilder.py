from src.requests.requestsbuilder import RequestsBuilder
from src.requests.convertrequest import ConvertRequest
from src.requests.setrequest import SetRequest
from src.requests.sortrequest import SortRequest

class Builder(RequestsBuilder):
    def __init__(self):
        super().__init__()
        
    def convert_request(self, conversionblock, argument_types_data=None, arguments_converters=None):
        self.requests.append(ConvertRequest(conversionblock, argument_types_data, arguments_converters))
        return self
    
    def set_request(self, setblock):
        self.requests.append(SetRequest(setblock))
        return self
    
    def sort_request(self, source_names, key_source_name, destination_name, key=None):
        self.requests.append(SortRequest(source_names, key_source_name, destination_name, key))
        return self