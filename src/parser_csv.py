from .parser_args import args_read


from tabulate import tabulate

import csv
import operator


class ParseCSV():
    def __init__(self, file_csv, delimiter=',', encoding='utf-8'):
        self.file_csv = file_csv
        self.delimiter = delimiter
        self.encoding = encoding
 
        self.operators = {
            "=": operator.eq,
            ">": operator.gt,
            "<": operator.lt
        }


    def filter_csv(self, expression: str, data:dict) -> dict | None:
        for operator_str in self.operators:
            if operator_str in expression:

                key, value = expression.split(operator_str)
                key = key.strip()
                value = value.strip()
                
                try:
                    value1 = float(data[key])
                    value2 = float(value)
                except:  # noqa: E722
                    ...
                
                operator_func = self.operators[operator_str]

                
                if operator_func(value1, value2):
                    
                    return data
                
                
        
    def read(self):
        with open(self.file_csv, encoding=self.encoding) as r_file:
            reader = csv.DictReader(r_file, delimiter=self.delimiter)
            content = []
            if exp := args_read.where:
                for i in reader:
                    
                    if res:=self.filter_csv(str(exp), i):
                        content.append(res)
                    
                    
            # print (content)
            return tabulate(content, tablefmt='grid', headers='keys')
    


    
