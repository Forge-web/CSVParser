import operator

class FilterCSV:
    def __init__(self):
        self.OPERATORS = {
            "=": operator.eq,
            ">": operator.gt,
            "<": operator.lt
        }

        self.LISTAGGR = {
            "avg": self.avg,
            "min": min,
            "max": max
        }


    def avg(
            self, 
            list_num: list[int|float]) -> int | float:
        
        avg_result = 0
        for i in list_num:
            avg_result += i
        
        return avg_result / len(list_num)


    def aggregate_by_column_Tnum(
            self, 
            expression: str, 
            data: list[dict]) -> dict[str: list[str]]:
    
        for aggregate_str in self.LISTAGGR:
            if aggregate_str in expression and "=" in expression:
                list_num = []
                column, value = expression.split('=')

                for i in data:
                    try:
                        list_num.append(float(i[column]))
                    except:
                        raise TypeError("--aggregate column must be int or float")

                aggregate_func = self.LISTAGGR[aggregate_str]
                return {str(value):[str(aggregate_func(list_num))]}

            
        # raise ValueError("--aggregate must be 'column=min|max|avg'")


    def _filter_by_column(
            self, 
            expression: str, 
            data:dict) -> dict | None:
        
        for operator_str in self.OPERATORS:
            if operator_str in expression:

                column, value = expression.split(operator_str)

                column = data[column].strip()
                value = value.strip()
                try:
                    column = float(column)
                    value = float(value)
                
                except:  # noqa: E722
                    ...
                    # raise TypeError("--where must be  'column [>, <, =] [str, int, float]'")
                
                operator_func = self.OPERATORS[operator_str]
                if operator_func(column, value):
                    return data
            
    

    def filter_by_column(
            self,
            expression: str,
            data: list[dict]
        ) -> list[dict]:

        result = []

        for row in data:

            i = self._filter_by_column(
                expression=expression, 
                data=row
            )

            if i is not None:
                result.append(i)

        return result