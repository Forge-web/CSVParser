from src.parser_csv import ParseCSV
from src.parser_args import create_parser_args

parser_csv = ParseCSV(args=create_parser_args().parse_args())

if __name__ == "__main__":
    print(parser_csv.read_tabulate())