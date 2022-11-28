from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/sobre")
def sobre():
  return render_template("sobre.html")

@app.route("/faleconosco")
def conosco():
  return render_template("faleconosco.html")






if __name__ == '__main__':
  app.run(debug=True)