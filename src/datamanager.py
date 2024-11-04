from src.workbookdictionary import WorkbookDictionary
from src.locationsdictionary import LocationsDictionary
from src.excelworkbook import ExcelWorkbook


class DataManager:
    def __init__(self, locations_dictionary: LocationsDictionary):
        self.locations_dictionary = locations_dictionary
        self.workbook_dictionary = WorkbookDictionary(self._create_workbooks_with_locations(self.locations_dictionary.get_locations_gen()))

    def get_values(self, location_name):
        location = self._get_location(location_name)

        workbook = self._get_workbook(location.path)
        workbook.set_active_sheet(location.sheet_name)

        values = workbook.get(location.string_range, sheet_name=location.sheet_name)    

        return values

    def set_values(self, values, location_name):
        location = self._get_location(location_name)

        workbook = self._get_workbook(location.path)
        workbook.set_active_sheet(location.sheet_name)

        workbook.set(values, location.string_range, sheet_name=location.sheet_name)  

    def save(self):
        self.workbook_dictionary.save()


    def _get_location(self, name):
        return self.locations_dictionary[name]

    def _get_workbook(self, path):
        return self.workbook_dictionary[path]
    
    def _create_workbooks_with_locations(self, locations):
        paths_and_workbooks = {}

        paths = (location.path for location in locations)

        for path in paths:
            if path not in paths_and_workbooks:
                paths_and_workbooks[path] = ExcelWorkbook(path)

        return paths_and_workbooks