from src.polishnames import MALES_FIRST_NAMES, MALE_LAST_NAMES, FEMALE_FIRST_NAMES, FEMALE_LAST_NAMES
from random import choice, choices

def generate_first_name():
    return choice(MALES_FIRST_NAMES + FEMALE_FIRST_NAMES)

def generate_last_name():
    return choice(MALE_LAST_NAMES + FEMALE_LAST_NAMES)

def generate_first_names(amount):
    return choices(MALES_FIRST_NAMES + FEMALE_FIRST_NAMES, k=amount)

def generate_last_names(amount):
    return choices(MALE_LAST_NAMES + FEMALE_LAST_NAMES, k=amount)

def generate_full_name():
    match(choice(('male', 'female'))):
        case 'male':
            return choice(MALES_FIRST_NAMES) + ' ' + choice(MALE_LAST_NAMES)
        case 'female':
            return choice(FEMALE_FIRST_NAMES) + ' ' + choice(FEMALE_LAST_NAMES)
        
def generate_full_names_as_strings(amount):
    for _ in range(amount):
        yield generate_full_name()

def generate_full_names_as_two_lists(amount):
    strings = generate_full_names_as_strings(amount)
    first_names_and_last_names_tuples = [string.split() for string in strings]
    first_names = [value[0] for value in first_names_and_last_names_tuples]
    last_names = [value[1] for value in first_names_and_last_names_tuples]

    return first_names, last_names