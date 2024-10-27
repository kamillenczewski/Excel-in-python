from os.path import isdir
from os import listdir
from os.path import join

def find_all_dirs(dir_path):
    file_names = listdir(dir_path)
    file_paths = [join(dir_path, name) for name in file_names]
    dir_paths = [path for path in file_paths if isdir(path)]

    if dir_paths:
        for path in dir_paths:
            dir_paths.extend(find_all_dirs(path))

    return dir_paths
    
def ensure_access_to_files():
    from sys import path
    from pathlib import Path
    
    main_dir_path = str(Path(__file__).parent.resolve())

    path_to_venv = join(main_dir_path, 'venv', 'Lib', 'site-packages')
    path_to_src = join(main_dir_path, 'src')

    path.insert(0, path_to_venv)
    path.insert(0, path_to_src)

    src_dirs = find_all_dirs(path_to_src)

    for dir in src_dirs:
        path.insert(0, dir)