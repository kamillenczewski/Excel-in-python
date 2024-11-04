from ensureaccesstofiles import ensure_access_to_files

ensure_access_to_files()

from visualbuilder import Builder
from src.conversionblockbuilder import ConversionBlockBuilder
from src.argumenttypesbuilder import ArgumentTypesBuilder
from src.argumentconvertersbuilder import ArgumentConvertersBuilder

def convert_table(table):
    print(table)
    return table

def to_dict(table):
    split_point = len(table) // 2

    column1 = table[:split_point]
    column2 = table[split_point:]
    
    dictionary = {a: b for a, b in zip(column1, column2)}

    return dictionary

def convert_method(first_name, dictionary):   
    if first_name in dictionary:
        return dictionary[first_name]
    
    return 0
        

def main1():
    (Builder()
        .string_range('a', 'A2:[V]')
        .string_range('b', 'B2:[V]')
        .string_range('dict', 'D3:E4')
        .string_range('c', 'G2:[V]')
        .path_for_all('inicjaly copy.xlsx')

        .sort_request('a', 'a')

        .convert_request(
            ConversionBlockBuilder()
                .source_names('a', 'dict')
                .destination('c')
                .convert_method(convert_method)
                .build(),
            ArgumentTypesBuilder()
                .arg('a', 'element')
                .arg('dict', 'table')
                .build(),
            ArgumentConvertersBuilder()
                .arg('dict', to_dict)
                .build()
        )
        
        .execute()
        .save()
    )
  
def main():
    (Builder()
        .string_range('a', 'A2:[V]')
        .string_range('b', 'B2:[V]')
        .string_range('c', 'C2:[V]')
        .path_for_all('inicjaly copy.xlsx')

        .sort_request(('a', 'b', 'c'), 'a', 'b')
        
        .execute()
        .save()
    )

def main():
    (Builder()
        .locations()
        .string_range('b', 'B2:[V]')
        .string_range('c', 'C2:[V]')
        .path_for_all('inicjaly copy.xlsx')

        .sort_request(('a', 'b', 'c'), 'a', 'b')
        
        .execute()
        .save()
    )

# Special builder for more visual friendly/user friendly appearance of written code
# ArgumentTypesBuilder

main()