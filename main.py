# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")



@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/🥵🥵🔥SUS🥵🥵🔥')
def sus():
    return render_template("sus.html")

@app.route('/Ethan/')
def stub2():
    return render_template("stub2.html")

@app.route('/Jason/')
def Jason():
    return render_template("Jason.html")
@app.route('/sus')
def sussy():
    return render_template("sophie.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,)
