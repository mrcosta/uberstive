# -*- coding: utf-8 -*-

from quantotempotemos.mod_info.views import calculate_time
from datetime import date, datetime

#def test_calculate_time_with_today():
#    assert calculate_time(datetime.today()) == "4 meses"

def test_calculate_time():
    assert calculate_time(date(2016, 8, 29)) == "4 meses"

def test_calculate_time_with_one_year_and_some_months():
    assert calculate_time(date(2017, 8, 29)) == "1 ano e 4 meses"

def test_calculate_time_with_date_with_year_and_just_one_month():
    assert calculate_time(date(2017, 5, 29)) == "1 ano e 1 mês"

def test_calculate_time_with_exaclty_one_year():
    assert calculate_time(date(2017, 4, 29)) == "1 ano"

def test_calculate_time_with_exaclty_more_than_one_year():
    assert calculate_time(date(2018, 4, 29)) == "2 anos"

def test_calculate_time_with_more_than_one_year_and_1_month():
    assert calculate_time(date(2018, 5, 29)) == "2 anos e 1 mês"
