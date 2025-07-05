import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
                    type=str,
                    help='Путь до файла с расштрением')


parser.add_argument('-w', '--where',
                    type=str,
                    help='условия фильтрации')


args_read = parser.parse_args()