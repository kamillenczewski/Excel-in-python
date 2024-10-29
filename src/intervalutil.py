from lettersrange import letters_range

def split_excel_index(index: str):
    for i in range(len(index) - 1):
        if index[i].isalpha() != index[i + 1].isalpha():
            split_index = i + 1
            return index[:split_index], int(index[split_index:])

def join_excel_index(letter, number):
    return letter + str(number)

def infinite_range(start):
    index = start

    while True:
        yield index
        index += 1

def limited_generator(generator, limit):
    return (index for _, index in zip(range(limit), generator))

def vertical_indices_range(start_index):
    index_letter, index_number = split_excel_index(start_index)

    for letter in [index_letter]:
        for number in infinite_range(index_number):
            yield f'{letter}{number}'

def horizontal_indices_range(start_index):
    index_letter, index_number = split_excel_index(start_index)

    for letter in letters_range(index_letter):
        for number in [index_number]:
            yield f'{letter}{number}'
            
def default_indices_range(start_index, end_index):
    start_letter, start_number = split_excel_index(start_index)
    end_letter, end_number = split_excel_index(end_index)

    for letter in letters_range(start_letter, end_letter):
        for number in range(start_number, end_number + 1):
            yield f'{letter}{number}'    

def indices_range(excel_like_range: str):
    excel_like_range = excel_like_range.replace(' ', '')

    first_excel_index, second_excel_index = excel_like_range.split(':')

    if '[V]' in second_excel_index:
        return vertical_indices_range(first_excel_index)
    elif '[H]' in second_excel_index:
        return horizontal_indices_range(first_excel_index)
    else:
        return default_indices_range(first_excel_index, second_excel_index)