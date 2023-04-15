import flask
import pandas
import openpyxl

from app import app
from flask import render_template, request, session


@app.route('/problem_solver', methods=['get'])
def problem_solver():

    # Датафрейм для примера
    data = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14, 15, 16, 17, 18],
            [19, 20, 21, 22, 23, 24, 25, 26, 27],
            [28, 29, 30, 31, 32, 33, 34, 35, 36],
            [37, 38, 39, 40, 41, 42, 43, 44, 45]]
    columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9']
    df = pandas.DataFrame(data=data, columns=columns)

    #   Список ошибок (если пустой, отдаст таблицу, иначе выведет список ошибок)
    errors = []

    html = render_template(
        'problem_solver.html',
    errors = errors,
    relation = df,
    len = len,
    int = int,
    lenerror = int(len(errors)))
    return html