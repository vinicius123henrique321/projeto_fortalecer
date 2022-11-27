from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")