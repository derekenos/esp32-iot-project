"""Filesystem Helpers
"""

import json
import os

from lib._os import path


TMP_DIR = '/tmp'
DATA_DIR = '/data'


def maybe_mkdir(_dir):
    """If the specified directory doesn't exist, create it and return True,
    otherwise return False.
    """
    if path.exists(_dir):
        return False
    os.mkdir(_dir)
    return True


def init_filesystem():
    """Ensure that the required filesystem directories exist and, if
    necessary, erase all files in the tmp directory.
    """
    maybe_mkdir(DATA_DIR)

    tmp_created = maybe_mkdir(TMP_DIR)
    if not tmp_created:
        # Temp directory already existed so delete any containing files.
        for filename in os.listdir(TMP_DIR):
            os.remove(path.join(TMP_DIR, filename))


_next_tempfile_id = 0
def NamedTemporaryFile(mode='wb'):
    global _next_tempfile_id
    name = str(_next_tempfile_id)
    fh = open(path.join(TMP_DIR, name))
    _next_tempfile_id += 1
    return name, fh


def read_datafile(filename):
    file_path = path.join(DATA_DIR, filename)
    if not path.exists(file_path):
        return None
    return json.load(open(file_path, 'r', encoding='utf-8'))


def write_datafile(filename, data):
    file_path = path.join(DATA_DIR, filename)
    # Attempt to encode here to prevent truncating an existing file in the case
    # of an error.
    data = json.dumps(data)
    with open(file_path, 'w') as fh:
        fh.write(data)
