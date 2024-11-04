from src.locationsdictionary import LocationsDictionary
from src.requests.request import Request
from src.datamanager import DataManager

class RequestsBuilder:
    def __init__(self):
        self.locations_dictionary = None
        self.data_manager = None

        self.requests: list[Request] = []

    def locations(self, locations_dictionary: LocationsDictionary):
        self.locations_dictionary = locations_dictionary
        return self

    def request(self, request_):
        self.requests.append(request_)
        return self

    def execute(self):
        self.data_manager = DataManager(self.locations_dictionary)

        for request in self.requests:
            request.execute(self.data_manager)
        
        return self

    def save(self):
        self.data_manager.save()
