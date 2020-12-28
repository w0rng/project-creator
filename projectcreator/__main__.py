#
#  __main__.py
#
#  Created by w0rng on 28.12.2020.
#  Copyright © 2020 w0rng. All rights reserved.
#


import sys
import logging
from create_project import create_project
from list_projects import print_list_projects
from create_config import create_config


logging.basicConfig(
    level=logging.ERROR,
    format='%(name)s - %(levelname)s - %(message)s'
)


def check_create_command():
    if len(sys.argv) < 3:
        logging.error('Не введен тип проекта')
        exit(1)
    elif len(sys.argv) < 4:
        logging.error('Не введено название проекта')
        exit(1)

    create_project(sys.argv[2], sys.argv[3])


def check_create_config():
    if len(sys.argv) < 3:
        logging.error('Не введено название нового конфига')
        exit(1)
    elif len(sys.argv) < 4:
        logging.error('Не введено название папки')
        exit(1)
    create_config(sys.argv[2], sys.argv[3])


def print_help_info():
    print('Введите projectcreator create {config_name} {name}',
          'чтобы создать проект')
    print('Введите projectcreator list чтобы посмотреть список доступных конфигов')
    print('Введите projectcreator newconfig {config_name} {path}',
          'чтобы создать конфиг из папки')


def main():
    commands = {
        'create': check_create_command,
        'list': print_list_projects,
        'newconfig': check_create_config,
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
