from flask import Flask, render_template, request, redirect, url_for, session
import os


app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route("/sobre")
def sobre_page():
    return render_template('sobre.html')



if __name__ == '__main__':
    app.run(debug=True)