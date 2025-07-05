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

        self.list_aggregate = {
            "avg": self.avg,
            "min": min,
            "max": max
        }


    def avg(self, list_num: list[int|float]):
        avg_result = 0
        for i in list_num:
            avg_result += i
        
        return avg_result / len(list_num)


    def aggregate_csv(self, expression: str, data: list[dict]):
        for aggregate_str in self.list_aggregate:
            if aggregate_str in expression and "=" in expression:
                list_num = []
                column, value = expression.split('=')

                for i in data:
                    try:
                        list_num.append(float(i[column]))
                    except:
                        raise TypeError("--aggregate column must be int or float")

                aggregate_func = self.list_aggregate[aggregate_str]
                return {str(column):[str(aggregate_func(list_num))]}

            
        raise ValueError("--aggregate must be 'column=min|max|avg'")


    def filter_csv(self, expression: str, data:dict) -> dict | None:
        for operator_str in self.operators:
            if operator_str in expression:

                column, value = expression.split(operator_str)
                column = column.strip()
                value = value.strip()
                
                try:
                    value1 = float(data[column])
                    value2 = float(value)
                except:  # noqa: E722
                    ...
                
                operator_func = self.operators[operator_str]

                if operator_func(value1, value2):
                    return data
            
            
        raise ValueError("--where must be  'column > | < | = str | int | float'")
                
                
    def read(self):
        with open(self.file_csv, encoding=self.encoding) as r_file:
            reader = csv.DictReader(r_file, delimiter=self.delimiter)
            content = []

            if exp := args_read.where:
                for i in reader:
                    
                    if res := self.filter_csv(str(exp), i):
                        content.append(res)
            
            if exp := args_read.aggregate:
                if content != []:
                    content = self.aggregate_csv(exp, content)
                
                else:
                    content = self.aggregate_csv(exp, [i for i in reader])
            
            print(content)

            return tabulate(content, tablefmt='grid', headers='keys')
    


    
