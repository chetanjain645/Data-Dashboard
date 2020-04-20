from worldbankapp import app

from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling

data = data_wrangling()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", data_var=data)


@app.route("/project-one")
def project_one():
    return render_template("project_one.html")


@app.route("/chetan")
def chetan():
    return render_template("chetan.html")
