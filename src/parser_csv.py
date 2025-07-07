from .parser_args import parser_args
from .filter_csv import FilterCSV

from tabulate import tabulate

import csv



class ParseCSV():
    def __init__(self, args, delimiter=',', encoding='utf-8'):
        self._args = args
        self.delimiter = delimiter
        self.encoding = encoding
        self.filter_csv = FilterCSV()

                
    def _get_content_file(self):
        with open(self._args.file, encoding=self.encoding) as r_file:
            reader = csv.DictReader(r_file, delimiter=self.delimiter)
            return [i for i in reader]


    def _to_aggregate(
            self, 
            content_file: list[dict]) -> dict[str:str] | None:

    
        if self._args.aggregate is None:
            return None

        result_aggregate = self.filter_csv.aggregate_by_column_Tnum(
            str(self._args.aggregate), 
            content_file
        )
            
        return result_aggregate
    
    def _to_filter(
            self,
            content_file: list[dict])->list[dict] | None:
        
        if self._args.where is None:
            return None
        
        result_filter = self.filter_csv.filter_by_column(
                str(self._args.where),
                content_file
            )

        return result_filter
    
        

    def _send_result(self, content_file: list[dict]):
        return tabulate(content_file, tablefmt='grid', headers='keys')


    def read_tabulate(self):
        content_file = self._get_content_file()
        

        _where = self._args.where
        _aggregate = self._args.aggregate
        
        if _where and _aggregate:
            content_file = self._to_aggregate(self._to_filter(content_file))
            return self._send_result(content_file)

        if _where:
            content_file = self._to_filter(content_file)

        if _aggregate:
            content_file = self._to_aggregate(content_file)
        
        
        return self._send_result(content_file)
        


    
