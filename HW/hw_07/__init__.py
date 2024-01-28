from .task01 import rename_files

import os
import glob

__all__ = ['rename_files']

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    folder_path = "test_folder"
    files = glob.glob(os.path.join(folder_path, f'*.{source_ext}'))

    if not name_range:
        name_range = [0, len(desired_name)]

    for i, file_path in enumerate(files, start=1):
        file_name = os.path.basename(file_path)
        original_name = file_name[: file_name.rindex('.')]
        original_name = original_name[name_range[0]:name_range[1]]

        new_name = f"{desired_name}{str(i).zfill(num_digits)}.{target_ext}"
        os.rename(file_path, os.path.join(folder_path, new_name))
