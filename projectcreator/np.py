#!/usr/bin/python3
# 
#  np.py
# 
#  Created by w0rng on 12.09.2018.
#  Copyright © 2020 w0rng. All rights reserved.
# 


import json
import sys
import os


def main():
    if len(sys.argv) < 2:
        drop_error('не введен тип проекта')

    project_type = sys.argv[1]
    path_configs = os.path.expanduser("~") + '/.config/project_creator/'

    if project_type not in os.listdir(path_configs):
        print('Нет такого проекта')

    with open(path_configs+project_type) as f:
        config = json.load(f)

    if 'path' in config:
        print('Создание папок')
        create_folders(config['path'])

    if 'files' in config:
        print('Создание файлов')
        for f in config['files']:
            create_file(f, config['files'][f])

    if 'commands' in config:
        print('Выполнение команд')
        for commands in config['commands']:
            run_command(commands)


def __get_folders(folders, path=''):
    """Возвращает пути к папкам"""
    for folder in folders:
        yield f'{path}{folder}/'
        if len(folders[folder]):
            yield from __get_folders(folders[folder], f'{path}{folder}/')


def create_folders(folders):
    """Создает структуру папок"""
    for path in __get_folders(folders):
        if not os.path.exists(path):
            os.mkdir(path)


def create_file(name, lines):
    """Создает файл name с содержимым lines"""
    if os.path.exists(name):
        drop_waring(f'{name} существует')
        return None
    with open(name, 'w') as file:
        for line in lines:
            file.write(line+'\n')


def run_command(commands):
    """Выполняет команду commands"""
    os.system(commands)


def drop_error(error):
    """Выводит ошибку error в консоль и закрывает программу"""
    print(f'Ошибка: {error}')
    exit(1)


def drop_waring(waring):
    """Выводит предупреждения waring в консоль"""
    print(waring)


if __name__ == '__main__':
    main()
