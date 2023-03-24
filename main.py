from flask import Flask, render_template, request, Response
from backend.stub_db import StubDB
from backend.basic_db import BasicDB
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--csv', metavar='path', required=True, help='File path of CSV to read and write')
args = parser.parse_args()

app = Flask(__name__)
db = BasicDB(args.csv)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    print(request.form)
    if request.form.get('submit') and request.form['submit'] == 'Search':
        result = db.Search(request.form['searchTerm'], request.form['search criteria'])
        result = result.reset_index(drop=True)
        print(result)
        return render_template('index.html', result = result)
    if request.form['submit'] == 'addnew':
        print(request.form)
        result = db.AddNew(request.form['FirstName'],request.form['LastName'],request.form['Phone'],request.form['OrderDate'],request.form['Files'],)
        return render_template('index.html')


app.run(debug=True)