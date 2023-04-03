from flask import Flask, request, render_template, session, redirect
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home():
    return redirect("/index")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/berries')
def berries():
    return render_template('berries.html')

@app.route('/datainf')
def datainf():
    return render_template('datainf.html')

@app.route('/sdg')
def sdg():
    return render_template('sdg.html')

@app.route('/sustainability')
def sus():
    return render_template('sustainability.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return "<h1>Ooops, we messed up somewhere. How about hitting that good ol' reload button, to see if that fixes. If not, just wait for an undefinite amount of time, and eventually we'll fix the issue (no money back guarantee)</h1>", 500




if __name__ == '__main__':
    app.run(host='0.0.0.0')

