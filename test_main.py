from unittest.mock import patch
from unittest import TestCase
import pytest


from src.parser_csv import ParseCSV
from src.parser_args import parser_args
from src.filter_csv import FilterCSV

from dataclasses import dataclass
import argparse


test_list_dict = [
    {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'}, 
    {'name': 'iphone 16 pro', 'brand': 'apple', 'price': '1999', 'rating': '4.9'}, 
    {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'}, 
    {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
    {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'}]


list_args_aggregate = [
    "price=min", 
    "price=max", 
    "price=avg", 
    "rating=min", 
    "rating=max", 
    "rating=avg"
]

list_args_filter = [
    "price>300",
    "price<999",
    "price=199",
    "rating>4.5",
    "rating<4.8",
    "rating=4.9",
    "name=iphone 15 pro",
    "brand=apple"
]

@pytest.mark.parametrize("expression", list_args_aggregate)
def test_aggregate_by_column_Tnum(expression):
        
    assert FilterCSV().aggregate_by_column_Tnum(
        expression,
        test_list_dict)


@pytest.mark.parametrize("expression", list_args_filter)
def test_filter_by_column(expression):
      
    assert FilterCSV().filter_by_column(
        expression, 
        test_list_dict)


def test__filter_by_column_str_True():
    assert FilterCSV()._filter_by_column(
        "brand=apple",
        test_list_dict[0]
    ) == test_list_dict[0]


def test__filter_by_column_str_False():
    assert FilterCSV()._filter_by_column(
        "brand=sumsung",
        test_list_dict[0]
    ) is None


def test__filter_by_column_int_True():
    assert FilterCSV()._filter_by_column(
        "price>199",
        {"name": "test dict", "price": "200"}
    ) == {"name": "test dict", "price": "200"}


def test__filter_by_column_int_False():
    assert FilterCSV()._filter_by_column(
        "price<200",
        {"name": "test dict", "price": "200"}
    ) is None


def test_avg():
    assert FilterCSV().avg([1, 2, 3]) == 2
    assert FilterCSV().avg([4, 5, 6]) == 5




def test__get_content_file():
    assert ParseCSV(
        args=parser_args(['--file', 'test.csv'])
    )._get_content_file() == test_list_dict


def test__to_aggregate_min():
    assert ParseCSV(
        args=parser_args(['--aggregate', 'price=min'])
    )._to_aggregate(test_list_dict) == {"min": ["199.0"]}


def test__to_aggregate_max():
    assert ParseCSV(
        args=parser_args(['--aggregate', 'price=max'])
    )._to_aggregate(test_list_dict) == {"max": ["1999.0"]}


def test__to_aggregate_avg():
    assert ParseCSV(
        args=parser_args(['--aggregate', 'price=avg'])
    )._to_aggregate(test_list_dict) == {"avg": ["939.0"]}

 
@pytest.mark.parametrize("list_args", 
                            ['brand=samsung',
                             'brand=apple',
                             'price>500',
                             'price<500',
                             'price=199' 
                            ]
                        )
def test__to_filter(list_args):
    
    test_do = ParseCSV(
        args=parser_args(['--where', list_args])
    )._to_filter(test_list_dict)
    
    for i in test_do:
        assert i in test_list_dict
    

