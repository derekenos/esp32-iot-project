"""Configuration data loader.
"""

from lib._collections import ChangeNotificationDict
from lib.filesystem import read_datafile


CONFIG_FILENAME = 'config.json'


config = ChangeNotificationDict()


def load_datafiles():
    global config

    config.clear()
    config.update(read_datafile(CONFIG_FILENAME))
