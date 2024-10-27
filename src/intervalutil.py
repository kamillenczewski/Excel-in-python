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

def letters_range(start_letter, end_letter=None):
    number = ord(start_letter)
    letter = None

    if end_letter == None:
        while True:
            letter = convert(number)
            yield letter
            number += 1
    else:
        while letter != end_letter:
            letter = convert(number)
            yield letter
            number += 1

def convert(x):
    MAX_LETTERS = 26
    A_ASCII = ord('A')
    numbers = []

    x -= A_ASCII

    if x == 0:
        return 'A'

    while x > 0:
        rest = x % MAX_LETTERS
        x //= MAX_LETTERS
        char = chr(rest + A_ASCII)
        numbers.append(char)

    numbers = numbers[::-1]

    numbers[:-1] = [chr(ord(char) - 1) for char in numbers[:-1]]

    return ''.join(numbers)

def limited_generator(infinite_generator, iterations):
    for _ in range(iterations, -1, -1):
        yield next(infinite_generator)

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

if __name__ == '__main__':
    print(list(limited_generator(indices_range('B2:[H]'), iterations=30)))