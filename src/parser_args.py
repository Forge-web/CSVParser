import argparse


def create_parser_args():
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

    return parser


def parser_args(args):

    parser = create_parser_args()

    return parser.parse_args(args)