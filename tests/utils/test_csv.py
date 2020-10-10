import pytest
import os
import core.utils.csv as csv

def test_csv():
    test_headers = ['style','country']
    test_dict = dict(style='Porter', country='United Kingdom')
    test_file = "beer.csv"
    try:
        csv.dict_writer(test_file, test_headers, test_dict)
    except:
        pass
    if os.path.exists(test_file):
        os.remove(test_file