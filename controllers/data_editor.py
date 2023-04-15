import flask
import pandas
from app import app
from flask import render_template, request, session

@app.route('/data_editor', methods=['get'])
def data_editor():
    list_trips = ['hui', 'hui1', 'hui2']
    list_trains = [['hui', 'hui1', 'hui2','sos'], ['hu3', 'hui4', 'hui5','sosi']]
    list_types =  ['hui', 'hui1', 'hui2']


    html = render_template(
        'data_editor.html',
    len = len,
    int = int,
    train_types = list_types,
    travel_trips = list_trips,
    trains =  list_trains
    )

    return html