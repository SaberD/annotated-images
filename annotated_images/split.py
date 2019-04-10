"""Splits data into training testing and (validation)
"""

import pathlib
import random
import shutil
import glob
import json
import xml.etree.cElementTree as et
from os import path, listdir


def list_dirs(directory):
    """Returns all directories in a given directory
    """
    return [f for f in pathlib.Path(directory).iterdir() if f.is_dir()]


def list_files(directory):
    """Returns files in a given directory
    Default only splits annotated images, if no annotations are found then all images are split.
    """
    files = glob.glob(directory + "*.json")
    if len(files) == 0:
        files = glob.glob(directory + "*.xml")
    if len(files) == 0:
        files = glob.glob
    if len(files) == 0:
        files = glob.glob(directory + "*.*")
    return files


def split(input_dir, output_dir="output", seed=1337, ratio=(.8, .1, .1)):
    """Copies files from input dir to folders in output dir

    Keeps the annotation data together with the images while splitting. 
    To only split into train and test folder, only input ratio of len 2 (i.e. ratio=(0.8, 0.2)).

    Args:
        input_dir (str): path to images and annotation data.
        output_dir (str): path to setup train/test/val folders
        seed (int): enables reproducible splits results
        ratio (list): ratios to split into train/test/val. has to sum up to 1.0

    Returns:
        dict with the count of the number of images in each folder
    """
    assert sum(ratio) == 1
    assert len(ratio) in (2, 3)

    return  split_ratio(input_dir, output_dir, ratio, seed)

def setup_files(input_dir, seed):
    """Returns shuffled files
    """
    # make sure its reproducible
    random.seed(seed)

    files = list_files(input_dir)

    files.sort()
    random.shuffle(files)
    return files

def split_ratio(input_dir, output_dir, ratio, seed):
    """Splits one very class folder
    """
    files = setup_files(input_dir, seed)

    split_train = int(ratio[0] * len(files))
    split_test = split_train + int(ratio[1] * len(files))

    li = split_files(files, split_train, split_test, len(ratio) == 3)
    return copy_files(li, output_dir)


def split_files(files, split_train, split_test, use_val):
    """Splits the files along the provided indices
    Returns a dict with the number of images in each folder
    """
    files_train = files[:split_train]
    files_test = files[split_train:split_test] if use_val else files[split_train:]

    li = [(files_train, 'train'), (files_test, 'test')]

    # optional validation folder
    if use_val:
        files_val = files[split_test:]
        li.append((files_val, 'val'))
    return li


def copy_files(files_type, output):
    """Copies the files from the input folder to the output folder
    """
    total = 0
    out = dict()
    for (files, folder_type) in files_type:
        counter = 0
        full_path = path.join(output, folder_type)

        pathlib.Path(full_path).mkdir(
            parents=True, exist_ok=True)
        for f in files:
            name = path.splitext(f)[0]
            counter += 1
            for i in glob.glob(name+".*"):
                shutil.copy2(i, full_path)
        out[folder_type] = counter
        total += counter
    out["total"]=total
    return out