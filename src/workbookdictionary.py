from src.excelworkbook import ExcelWorkbook

class WorkbookDictionary:
    def __init__(self, paths_and_workbooks: dict[str, ExcelWorkbook]):
        self.paths_and_workbooks = paths_and_workbooks

    def add(self, path):
        if path not in self.paths_and_workbooks:
            self.paths_and_workbooks[path] = ExcelWorkbook(path)

    def extend(self, paths):
        for path in paths:
            self.add(path)


    def __getitem__(self, path):
        if path not in self.paths_and_workbooks:
            self.add(path)
            
        return self.paths_and_workbooks[path]
    
    def __contains__(self, item):
        return item in self.paths_and_workbooks

    def values(self):
        return self.paths_and_workbooks.values()
    
    def save(self):
        for workbook in self.paths_and_workbooks.values():
            workbook.save()