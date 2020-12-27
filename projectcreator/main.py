# 
#  main.py
# 
#  Created by w0rng on 28.12.2020.
#  Copyright © 2020 w0rng. All rights reserved.
# 


import sys
import logging
from .create_project import create


def check_create_command():
    if len(sys.argv) < 3:
        logging.error('Не введен тип проекта')
        exit(1)
    elif len(sys.argv) < 4:
        logging.error('не введено название проекта')
        exit(1)

    create(sys.argv[2], sys.argv[3])


def print_help_info():
    print('Введите projectcreator create {project_type} {name} чтобы создать проект')


def main():
    commands = {
        'create': check_create_command,
    }

    if len(sys.argv) < 2:
        print_help_info()
        exit(0)

    if (command := sys.argv[1]) in commands:
        commands[command]()
    else:
        logging.warning('Команда не найдена')

if __name__ == "__main__":
    main()