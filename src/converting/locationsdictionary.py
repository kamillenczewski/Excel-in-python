from src.converting.datalocation import DataLocation


class LocationsDictionary:
    def __init__(self):
        self.names_and_locations: dict[str, DataLocation] = {}

        self._global_path = None
        self._global_sheet_name = None

    def set_global_path(self, path):
        self._global_path = path

    def set_path_for_all(self, path):
        for location in self.names_and_locations.values():
            location.path = path

    def set_global_sheet_name(self, sheet_name):
        self._global_sheet_name = sheet_name

    def set_string_range(self, name, string_range):
        self.ensure_location_with_name(name)
        self._get_location(name).string_range = string_range

    def set_path(self, name, path):
        self.ensure_location_with_name(name)
        self._get_location(name).path = path

    def add_location(self, name, location):
        self.names_and_locations[name] = location
    
    def add_empty_location(self, name):
        self.add_location(name, DataLocation())

    def ensure_location_with_name(self, name):
        if name not in self.names_and_locations:
            self.add_empty_location(name)

    def _get_path(self, name):
        return self._get_location(name).path

    def _get_sheet_name(self, name):
        return self._get_location(name).sheet_name

    def _get_string_range(self, name):
        return self._get_location(name).string_range


    def _get_location(self, name):
        if name not in self.names_and_locations:
            raise ValueError(f"There is no location with name: {name}!")
        
        return self.names_and_locations[name]

    def get_location(self, name):
        path = self._get_path(name) if self._global_path == None else self._global_path
        sheet_name = self._get_sheet_name(name) if self._global_sheet_name == None else self._global_sheet_name

        return DataLocation(path, sheet_name, self._get_string_range(name))

    def _get_locations(self, names):
        for name in names:
            yield self.get_location(name)

    def get_locations(self, names):
        return list(self._get_locations(names))