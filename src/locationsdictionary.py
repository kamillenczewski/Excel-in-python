from src.datalocation import DataLocation


class LocationsDictionary:
    def __init__(self, names_and_locations: dict[str, DataLocation]):
        self.names_and_locations = names_and_locations

    def __getitem__(self, name):
        if name not in self.names_and_locations:
            raise ValueError(f'There is no such location with name: {name}!')
    
        return self.names_and_locations[name]
        
    def get_locations_gen(self):
        return self.names_and_locations.values()