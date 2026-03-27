from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', "r") as file:
        item = json.load(file)
        items_list = item.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    error = ""
    print(bool(error))
    entries = []
    source = request.args.copy().get('source')
    id_param = request.args.copy().get('id')

    if source == 'json':
        with open('products.json', "r") as file:
            if id_param:
                entries = [
                    dict
                    for dict in json.load(file)
                    if str(dict['id']) == id_param
                ]
                if entries == []:
                    error = "Product not found"
            else:
                entries = json.load(file)
    elif source == 'csv':
        with open('products.csv', "r") as file:
            if id_param:
                entries = [
                    dict
                    for dict in [
                        dict
                        for dict in csv.DictReader(file)]
                    if str(dict['id']) == id_param
                ]
                print(entries)
                if not entries:
                    error = "Product not found"
            else:
                entries = [dict for dict in csv.DictReader(file)]
    else:
        error = "Wrong source"
    return render_template('product_display.html', entries=entries, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
