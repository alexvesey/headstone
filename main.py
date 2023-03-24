from flask import Flask, render_template, request, Response
from backend.stub_db import StubDB

app = Flask(__name__)
db = StubDB()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        print('hello')
    print(request.form)
    result = db.Search(request.form['searchTerm'], request.form['search criteria'])
    result = result.reset_index(drop=True)
    print(result)
    return render_template('index.html', result = result)
app.run(debug=True)