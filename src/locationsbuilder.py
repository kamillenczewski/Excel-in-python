from src.datalocation import DataLocation
from src.locationsdictionary import LocationsDictionary

class LocationsBuilder:
    def __init__(self):
        self.names_and_locations: dict[str, DataLocation] = {}

        self.global_path_ = None
        self.global_sheet_name_ = None



    def string_range(self, location_name, string_range):
        self._get_location(location_name).string_range = string_range
        return self

    def path(self, location_name, path):
        self._get_location(location_name).path = path
        return self

    def sheet_name(self, location_name, sheet_name):
        self._get_location(location_name).sheet_name = sheet_name
        return self

    def path_and_string_range(self, name, path, string_range):
        return self.path(name, path).string_range(name, string_range)
    


    def path_for_all(self, path):
        if self.global_path_ == None:
            self._set_all_paths(path)

        return self
    
    def sheet_name_for_all(self, sheet_name):
        if self.global_sheet_name_ == None:
            self._set_all_sheet_names(sheet_name)

        return self



    def global_path(self, path):
        self.global_path_ = path
        return self
    
    def global_sheet_name(self, sheet_name):
        self.global_sheet_name_ = sheet_name
        return self



    def build(self):
        self._set_global_path_for_all()
        self._set_global_sheet_name_for_all()

        return LocationsDictionary(self.names_and_locations)


    def _set_global_path_for_all(self):
        if self.global_path_ != None:
            self._set_all_paths(self.global_path_) 

    def _set_global_sheet_name_for_all(self):
        if self.global_sheet_name_ != None:
            self._set_all_sheet_names(self.global_sheet_name_) 

    def _set_all_sheet_names(self, sheet_name):
        for location in self._get_locations():
            location.sheet_name = sheet_name 

    def _set_all_paths(self, path):
        for location in self._get_locations():
            location.path = path 

    def _get_locations(self):
        return list(self._get_locations_gen())

    def _get_locations_gen(self):
        for name in self.names_and_locations.keys():
            yield self._get_location(name)

    def _get_location(self, name):
        if name not in self.names_and_locations:
            self.names_and_locations[name] = DataLocation()

        return self.names_and_locations[name]