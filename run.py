from ensureaccesstofiles import ensure_access_to_files

ensure_access_to_files()

from dataconversionbuilder import DataConversionBuilder
from polishnamesgenerator import generate_full_name
from empty import Empty

def main():
    Empty(DataConversionBuilder()
        .string_range('a', 'A2:[V]')
        .string_range('b', 'B2:[V]')
        .string_range('c', 'C2:[V]')
        .path_for_all('inicjaly.xlsx')
        .string_range('d', 'D2:[V]')
        .path('d', 'inicjaly nowe.xlsx')
        .convert(('a', 'b', 'c'), 'd', lambda a, b, c: a + b + ' [' + c + ']')
        .execute()
        .save())

def main1():
    Empty(DataConversionBuilder()
        .global_path('inicjaly nowe.xlsx')
        .string_range('a', 'A1:[V]')
        .set_data_generator('a', (generate_full_name() for _ in range(100)))
        .execute()
        .save())
    
main1()