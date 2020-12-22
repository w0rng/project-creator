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

    with open(os.path.expanduser("~")+"/.np.conf") as f:
        config = json.load(f)

    if sys.argv[1] not in config["types"]:
        dropError("нет такого типа проекта")

    config = config["types"][sys.argv[1]]

    if "path" in config:
        print("Создание папок")
        createFolder(config["path"])
    else:
        dropWaring("Иерархия папок не указана")

    if "files" in config:
        print("Создание файлов")
        for f in config["files"]:
            createFile(f, config["files"][f])
    else:
        dropWaring("Файлы не заданы")

    if "comands" in config:
        for comand in config["comands"]:
            doComand(comand)
    else:
        dropWaring("Команды не заданы")


def createFolder(lst, folder=""):
    '''Создает папку lst с подпапками folders'''
    tmplist = lst
    if folder != "":
        tmplist = lst[folder]
    
    for path in tmplist:
        try:
            if folder:
                os.mkdir(folder + "/" + path)
            else:
                os.mkdir(path)
        except OSError:
            dropWaring(path + " существует")
        if type(tmplist) != list:
            createFolder(lst, path)


def createFile(name, lines):
    '''Создает файл name с содержимым lines'''
    if os.path.exists(name):
        f = open(name, 'w')
        for line in lines:
            f.write(line+"\n")
    else:
        dropWaring(name + " существует")


def doComand(comand):
    '''Выполняет команду comand'''
    os.system(comand)


def dropError(str):
    '''Выводит ошибку str в консоль и закрывает программу'''
    print("Ошибка: " + str)
    exit(1)


def dropWaring(str):
    '''Выводит предупреждения str в консоль'''
    print(str)


if __name__ == "__main__":
    main()