# -*- coding: utf-8 -*-

from flask import render_template
from quantotempotemos import app
from datetime import date, datetime
from dateutil import relativedelta as rdelta
from collections import namedtuple

DateFormat = namedtuple('DateFormat', ['condition', 'format'])
BEGIN_LOVE = date(2016, 4, 3)

@app.route('/', methods=['GET'])
def how_long():
    return render_template("home.html", howlong=calculate_time(datetime.today()))

def calculate_time(today):
    how_long_date = rdelta.relativedelta(today, BEGIN_LOVE)

    year_format = [format.format(how_long_date.years) for format in years_format if
                   format.condition(how_long_date.years)][0]
    month_format = [format.format(how_long_date.months) for format in months_format if
                   format.condition(how_long_date.months)][0]

    return year_format + (" e " if year_format and month_format else "") + month_format

years_format = [
    DateFormat(lambda years: years == 0, lambda years: ""),
    DateFormat(lambda years: years == 1, lambda years: "1 ano"),
    DateFormat(lambda years: years > 1, lambda years: "{} anos".format(years)),
]

months_format = [
    DateFormat(lambda months: months == 0, lambda months: ""),
    DateFormat(lambda months: months == 1, lambda months: "1 mês"),
    DateFormat(lambda months: months > 1, lambda months: "{} meses".format(months)),
]



