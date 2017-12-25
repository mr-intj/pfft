import pathlib

# Application name suffix (used in window captions)
APP_NAME = 'Pfft'


def ellipsize(path):
    parts = list(pathlib.PurePath(path).parts)
    if len(parts) >= 4:
        parts[2:-1] = ['...']
    return str(pathlib.PurePath(*parts))


def make_caption(title):
    return '{} - {}'.format(title, APP_NAME)
