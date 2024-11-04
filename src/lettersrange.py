A_ASCII = ord('A')
Z_ASCII = ord('Z')

FIRST_INDEX = 0
LAST_INDEX = Z_ASCII - A_ASCII


def letter_index_to_letter(letter_index):
    return chr(A_ASCII + letter_index)

def letter_to_letter_index(letter):
    return ord(letter) - A_ASCII

# Letter string is composition of letters like AA, AB, CD, AAD, ZZZZ
# - they are far indices in excel sheets

def letter_string_to_letter_indices(letter_string):
    return [letter_to_letter_index(letter) for letter in letter_string]

def letter_indices_to_letter_string(letter_indices):
    return ''.join([letter_index_to_letter(index) for index in letter_indices])


def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            return False
        
    return True
            


def letters_range(start_letter_string, end_letter_string=None):
    current_indices = letter_string_to_letter_indices(start_letter_string)
    end_indices = letter_string_to_letter_indices(end_letter_string)

    while not are_lists_equal(current_indices, end_indices):
        yield letter_indices_to_letter_string(current_indices)
        increase_indices_list(current_indices)

    yield letter_indices_to_letter_string(current_indices)

def increase_indices_list(indices_list, current_list_index=None):
    if current_list_index == None:
        current_list_index = len(indices_list) - 1

    if current_list_index == -1:
        indices_list.insert(0, FIRST_INDEX)
        return

    if indices_list[current_list_index] + 1 > LAST_INDEX:
        indices_list[current_list_index] = 0
        current_list_index -= 1
        increase_indices_list(indices_list, current_list_index)
    else:
        indices_list[current_list_index] += 1

if __name__ == '__main__':
    gen = letters_range('A', 'ABC')

    for i in gen:
        print(i)