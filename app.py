from flask import Flask, render_template, request, logging, Response, redirect, flash

# Flask の起動
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.run(host="localhost")
