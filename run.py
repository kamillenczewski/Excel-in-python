from ensureaccesstofiles import ensure_access_to_files
from src.converting.dataconversionbuilder import DataConversionBuilder
from src.intervalutil import split_excel_index
from src.polishnamesgenerator import generate_full_name

ensure_access_to_files()

# TO DO:
# every string range should be converted to indices_range
# because it will be look better and removes weird args possibilities

def main():
    (DataConversionBuilder()
        .string_range('a', 'A2:[V]')
        .string_range('b', 'B2:[V]')
        .string_range('c', 'C2:[V]')
        .path_for_all('inicjaly.xlsx')
        .string_range('d', 'D2:[V]')
        .path('d', 'inicjaly nowe.xlsx')
        .convert(('a', 'b', 'c'), 'd', lambda a, b, c: a + b + ' [' + c + ']')
        .execute()
    )

def main1():
    (DataConversionBuilder()
        .global_path('inicjaly nowe.xlsx')
        .string_range('a', 'A1:[V]')
        .set_data_generator('a', (generate_full_name() for _ in range(100)))
        .execute()
    )

main1()