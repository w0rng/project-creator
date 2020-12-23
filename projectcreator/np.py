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
        dropError("не введен тип проекта")

    PROJECT_TYPE = sys.argv[1]
    PATH_CONFIGS = os.path.expanduser("~") + '/.config/project_creator/'

    if PROJECT_TYPE not in os.listdir(PATH_CONFIGS):
        print('Нет такого проекта') 

    with open(PATH_CONFIGS+PROJECT_TYPE) as f:
        config = json.load(f)

    if "path" in config:
        print("Создание папок")
        create_folders(config["path"])

    if "files" in config:
        print("Создание файлов")
        for f in config["files"]:
            create_file(f, config["files"][f])

    if "commands" in config:
        print("Выполнение команд")
        for commands in config["commands"]:
            doCommands(commands)


def __get_folders(folders, path=''):
    '''Возвращает пути к папкам'''
    for folder in folders:
        yield f'{path}{folder}/'
        if len(folders[folder]):
            yield from __get_folders(folders[folder], f'{path}{folder}/')


def create_folders(folders):
    '''Создает структуру папок'''
    for path in __get_folders(folders):
        if not os.path.exists(path):
            os.mkdir(path)


def create_file(name, lines):
    '''Создает файл name с содержимым lines'''
    if os.path.exists(name):
        dropWaring(name + " существует")
        return None
    with open(name, 'w') as file:
        for line in lines:
            file.write(line+'\n')


def doCommands(commands):
    '''Выполняет команду commands'''
    os.system(commands)


def dropError(str):
    '''Выводит ошибку str в консоль и закрывает программу'''
    print("Ошибка: " + str)
    exit(1)


def dropWaring(str):
    '''Выводит предупреждения str в консоль'''
    print(str)


if __name__ == "__main__":
    main()