from os.path import join
from fileutil import find_all_dirs

def ensure_access_to_files():
    from sys import path
    from pathlib import Path
    
    main_dir_path = str(Path(__file__).parent.resolve())

    path_to_venv = join(main_dir_path, 'venv', 'Lib', 'site-packages')
    path_to_src = join(main_dir_path, 'src')

    path.insert(0, path_to_venv)
    path.insert(0, path_to_src)

    # src_dirs = find_all_dirs(path_to_src)

    # for dir in src_dirs:
    #     path.insert(0, dir)