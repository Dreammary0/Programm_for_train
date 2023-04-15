import flask
import pandas
from app import app
from flask import render_template, request, session


@app.route('/', methods=['get'])
def index():
    list_cities = ['hui', 'hui1', 'hui2','hui3','hui5','hui6']
    list_types = [['hui', 'hui1', 'hui2'], ['hu3', 'hui4', 'hui5']]
    list_trips = [['hui', 'hui1', 'hui2', 'hui3', 'hui4', 'hui5'], ['hui', 'hui1', 'hui2', 'hui3', 'hui4', 'hui5']]

    html = render_template(
        'index.html',
        cities=list_cities,
        trips=list_trips,
        types=list_types,
        len=len,
        int=int)
    return html
