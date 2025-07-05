from src.parser_args import args_read
from src.parser_csv import ParseCSV

from tabulate import tabulate
import argparse


parser_csv = ParseCSV(file_csv=args_read.file)

if __name__ == "__main__":
    print(parser_csv.read())