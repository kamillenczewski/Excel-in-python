from ensureaccesstofiles import ensure_access_to_files

ensure_access_to_files()

from src.visualbuilder import Builder
from src.locationsbuilder import LocationsBuilder
from src.conversionblockbuilder import ConversionBlockBuilder
from src.argumenttypesbuilder import ArgumentTypesBuilder

def main():
    (Builder()
        .locations(
            LocationsBuilder()
                .global_path('inicjaly.xlsx')
                .string_range('a', 'A2:[V]')
                .string_range('b', 'B2:[V]')
                .string_range('c', 'C2:[V]')
                .build()
        )
        .convert_request(
            ConversionBlockBuilder()
                .sources('a', 'b')
                .destination('c')
                .convert_method(lambda a, b: a[0] + '. ' + b[0] + '.')
                .build()
        )
        
        .execute()
        .save()
    )

main()