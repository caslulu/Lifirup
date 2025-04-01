from flask import Flask, render_template, request, redirect, url_for, session
import os


app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')

@app.route("/sobre")
def sobre_page():
    return render_template('sobre.html')


@app.route("/precos")
def precos_page():
    return render_template('precos.html')



if __name__ == '__main__':
    app.run(debug=True)