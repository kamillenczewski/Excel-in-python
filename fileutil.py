from os.path import isdir
from os import listdir
from os import remove as remove_file
from os.path import join

def find_all_dirs(dir_path):
    file_names = listdir(dir_path)
    file_paths = [join(dir_path, name) for name in file_names]
    dir_paths = [path for path in file_paths if isdir(path)]

    if dir_paths:
        for path in dir_paths:
            dir_paths.extend(find_all_dirs(path))

    return dir_paths

def convert_all_files(dir_path, file_name_condition, convert_method):
    dirs = find_all_dirs(dir_path)
    file_names = []

    for dir in dirs + [dir_path]:
        file_names_in_dir = [join(dir, file_name) for file_name in listdir(dir) if file_name_condition(file_name)]
        file_names.extend(file_names_in_dir)

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

        remove_file(file_name)

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(convert_method(text))