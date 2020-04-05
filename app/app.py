#! /usr/bin/env python3

import logging
import os
import requests

from flask import Flask, request, render_template

app = Flask(__name__)

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

app_id = os.getenv('EDAMAM_APP_ID')
app_key = os.getenv('EDAMAM_APP_KEY')


def get_data(query, app_id, app_key):
    """Gets data from API"""

    url = f'https://api.edamam.com/search?q={query}&app_id={app_id}&app_key={app_key}'
    response = requests.get(url)

    if response.status_code == 200:
        logging.info(f'Status code from API: {response.status_code}')

        return response.json()
    else:
        logging.warning(f'Status code from API: {response.status_code}')


@app.route('/')
def my_form():
    """Gets input from user"""
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    """Renders search results"""

    query = request.form['text']
    hits = get_data(query, app_id, app_key)['hits']

    recipes = []

    for x in hits:
        dct = {}
        dct['label'] = x['recipe']['label']
        dct['source'] = x['recipe']['source']
        dct['url'] = x['recipe']['url']
        dct['image'] = x['recipe']['image']
        recipes.append(dct)

    return render_template('results.html', posts=recipes)


app.run(host='0.0.0.0')
