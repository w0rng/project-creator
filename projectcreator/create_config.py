#
#  create_config.py
#
#  Created by w0rng on 28.12.2020.
#  Copyright © 2020 w0rng. All rights reserved.
#

import os
import logging
from config import IGNORE_PATHS


def create_config(config_name, path):
    path_configs = os.path.expanduser("~") + '/.config/project_creator/'

    if config_name in os.listdir(path_configs):
        logging.error(f'{config_name} уже существует')
        exit(1)

    if not os.path.exists(path):
        logging.error(f'Папка {config_name} не найдена')
        exit(1)

    print(get_paths_config(path))


def get_paths_config(path):
    result = {}
    for item in __get_paths_structure(path):
        p = result
        for x in item.split('/'):
            p = p.setdefault(x, {})
    return result[path]


def __get_paths_structure(path):
    for i in os.listdir(path):
        if not os.path.isdir(f'{path}/{i}'):
            logging.debug(f'Файл {i} пропущен при генерации структуры папок')
            continue
        if i in IGNORE_PATHS:
            logging.debug(f'Папка {i} проигнорированна')
            continue

        yield f'{path}/{i}'
        yield from __get_paths_structure(f'{path}/{i}')
