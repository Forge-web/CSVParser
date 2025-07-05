import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file',
                    type=str,
                    help='Путь до файла с расширением')


parser.add_argument('--where',
                    type=str,
                    help='Условия фильтрации')


parser.add_argument('--aggregate',
                    type=str,
                    help='Условия сортировки')


args_read = parser.parse_args()