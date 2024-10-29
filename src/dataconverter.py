from conversionblock import ConversionBlock
from datalocation import DataLocation
from excelworkbook import ExcelWorkbook
from workbookdictionary import WorkbookDictionary

class DataConverter:
    def __init__(self, workbooks_dictionary: WorkbookDictionary):
        self.workbooks_dictionary = workbooks_dictionary

        self.sources: list[DataLocation] = None
        self.destination: DataLocation = None
        self.convert_method = None

        self.data = None
        self.size = None

    def get_data_gen(self):
        for location in self.sources:
            path = location.path
            workbook = self.workbooks_dictionary[path]
            workbook.set_active_sheet(location.sheet_name)
            data = workbook.get(location.string_range)     

            yield list(data)

    def update_data(self):
        self.data = list(self.get_data_gen())

    def all_data_sets_have_same_size(self, data, size):
        for data_set in data:
            if len(data_set) != size:
                return False
        
        return True

    def update_size_of_data_set(self):
        size = len(self.data[0])

        if not self.all_data_sets_have_same_size(self.data, size):
            raise ValueError('All data sets should have the same size!')
        
        self.size = size

    def single_convert(self, conversion_block: ConversionBlock):
        self.update_attributes(conversion_block)
        self.update_workbooks()

        self.update_data()
        self.update_size_of_data_set()

        output = self.get_output()

        workbook = self.get_workbook(self.destination.path)
        workbook.set(output, self.destination.string_range, sheet_name=self.destination.sheet_name)
    
    def multiple_convert(self, conversion_blocks):
        for conversion_block in conversion_blocks:
            self.single_convert(conversion_block)

        return self

    def get_output_gen(self):
        for i in range(self.size):
            args = list(self.get_args(i)) 
            result = self.convert_method(*args)
            yield result

    def get_args(self, number_index):
        for list_ in self.data:
            yield list_[number_index]

    def get_output(self):
        return list(self.get_output_gen())

    def get_workbook(self, path):
        return self.workbooks_dictionary[path]

    def update_attributes(self, conversion_block: ConversionBlock):
        self.sources = conversion_block.sources
        self.destination = conversion_block.destination
        self.convert_method = conversion_block.convert_method

    def update_workbooks(self):
        paths = [location.path for location in self.sources + [self.destination]]
        paths = list(set(paths))
        self.workbooks_dictionary.extend(paths)