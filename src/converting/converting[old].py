from excelworkbook import ExcelWorkbook
from functools import partial
from collections.abc import Iterable

def get_all_method_names(class_):
    return [func for func in dir(class_) if not func.startswith('__') and callable(getattr(class_, func))]

def returnSelfDecorator(class_, skip=None):
    names = get_all_method_names(class_)
    names = [name for name in names if not isinstance(skip, Iterable) or isinstance(skip, Iterable) and name not in skip]
    methods = [getattr(class_, name) for name in names]

    def new_method(old_method, self, *args, **kwargs):
        print(args)

        old_method(self, *args, **kwargs)
        return self

    for name, method in zip(names, methods):
        setattr(class_, name, partial(new_method, method))

    return class_

class DataLocation:
    def __init__(self, path=None, sheet_name=None, string_range=None):
        self.path = path
        self.sheet_name = sheet_name
        self.string_range = string_range   

def sort(values):
    return sorted(values)

def are_all_methods(value, *bool_methods):
    for method in bool_methods:
        if not method(value):
            return False
    
    return True

def filter(values, *filter_methods):
    for value in values:
        if are_all_methods(value, *filter_methods):
            yield value
        
def convert(source: DataLocation, convert_method, destination: DataLocation=None, inplace: bool=None):
    if isinstance(inplace, bool) and inplace:
        workbook = ExcelWorkbook(source.path)
        values = workbook.get(source.string_range, sheet_name=source.sheet_name)
        values = list(convert_method(values))
        workbook.set(values, source.string_range, sheet_name=source.sheet_name)
        workbook.save()
    else:
        if not isinstance(destination, DataLocation):
            raise ValueError('destination can not be equal to None!')

        workbook1 = ExcelWorkbook(source.path)
        values = workbook1.get(source.string_range, sheet_name=source.sheet_name)
        values = list(convert_method(values))
        workbook2 = ExcelWorkbook(destination.path)
        workbook2.set(values, destination.string_range, sheet_name=destination.sheet_name)
        workbook2.save()

def multiple_convert(source: DataLocation, conversions, destination: DataLocation=None, inplace: bool=None):
    def converting_method(values, conversions_):
        for convert_method_and_args in conversions_:
            if len(convert_method_and_args) == 1:
                convert_method = convert_method_and_args[0]
                values = convert_method(values)
            elif len(convert_method_and_args) >= 2:
                convert_method, *args = convert_method_and_args
                values = convert_method(values, *args)

        return values

    convert(source, lambda values: converting_method(values, conversions), destination, inplace)

class DataConverter:
    def __init__(self):
        self.source = None
        self.destination = None
        self.inplace = False
    
        self.convert_methods_and_args = []

    def set_source(self, value):
        self.source = value
        return self

    def set_inplace(self, value):
        self.inplace = value
        return self

    def set_destination(self, value):
        self.destination = value
        return self

    def convert(self, convert_method, *args):
        self.convert_methods_and_args.append((convert_method, *args))
        return self

    def execute(self):
        multiple_convert(self.source, self.convert_methods_and_args, self.destination, self.inplace)

def filter_func(x):
    return x % 2 == 0

def main():
    (DataConverter()
        .set_source(DataLocation('sample copy.xlsx', string_range='B2:[V]'))
        .set_destination(DataLocation('sample copy.xlsx', string_range='C2:[V]'))
        .convert(filter, filter_func)
        .convert(sort)
        .execute())

def two_args_func(x, y):
    return x + y
from random import randint
def main0():
    workbook = ExcelWorkbook('checking.xlsx')

    values = [randint(0, 100) for _ in range(100)]
    
    workbook.set(values, 'B2:[V]')

    values = [randint(0, 100) for _ in range(100)]
    
    workbook.set(values, 'C2:[V]')

def main1():
    workbook = ExcelWorkbook('checking.xlsx')

    column1 = workbook.get('B2:[V]')
    column2 = workbook.get('C2:[V]')

    column3 = [two_args_func(x, y) for x, y in zip(column1, column2)]
    
    workbook.set(column3, 'D2:[V]')
# 3 -formuły
def main2():
    workbook = ExcelWorkbook('szkola.xlsx')

    kurs = workbook.get_item('C1', sheet_name='3 -formuły')

    sztuki = workbook.get('B4:[V]', sheet_name="3 -formuły")
    dolary = workbook.get('C4:[V]', sheet_name="3 -formuły")

    # usd_values = [x*y for x, y in zip(sztuki, dolary)]
    zl_values = [x*y*kurs for x, y in zip(sztuki, dolary)]

    # workbook.set(usd_values, 'D4:[V]', sheet_name="3 -formuły")
    workbook.set(zl_values, 'E4:[V]', sheet_name="3 -formuły")

def main3():
    from intervalutil import indices_range

    workbook = ExcelWorkbook('xd.xlsx')

    data = ["" for _ in indices_range('C2:C101')]

    workbook.set(data, 'C2:[V]')
    workbook.save()

if __name__ == '__main__':
    main3()