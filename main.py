# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
from pathlib import Path

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

@app.route('/🥵🥵🔥SUS🥵🥵🔥/')
def sus():
    return render_template("sus.html")

@app.route('/Ethan/')
def stub2():
    return render_template("stub2.html")

@app.route('/Jason/')
def jason():
    return render_template("Jason.html")

@app.route('/videos/')
def video():
    return render_template("VideoP.html")

@app.route('/signedaddition/')
def signed():
    return render_template("signedaddition.html")

@app.route('/unsignedaddition/')
def unsigned():
    return render_template("unsignedaddition.html")

@app.route('/rgb/')
def rgb():
    print("hello")
    path = Path(app.root_path) / "static" / "img"
    return render_template("rgb.html", images=image_data(path))

@app.route('/Sophie/')
def sussy():
    return render_template("sophie.html")

@app.route('/colorcode/')
def colorcode():
    return render_template("colorcode.html")

@app.route('/Punnu/')
def punnu():
    return render_template("punnu.html")

@app.route('/💡💡💡')
def binary():
    return render_template("binary.html")

@app.route('/thonas')
def bruh():
    return render_template("thonas.html")

@app.route('/articles')
def articles():
    return render_template("article.html")

@app.route('/logic_gates')
def logic_gates():
    return render_template("logic_gates.html")

# greetings project for Ethan Guo
@app.route('/Ethan/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("stub2.html", name=name)
    # starting and empty input default
    return render_template("stub2.html", name="World")

@app.route('/Jason/hello', methods=['GET', 'POST'])
def hello():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Jason.html", name=name)
    # starting and empty input default
    return render_template("Jason.html", name="World")

@app.route('/Punnu/hi', methods=['GET', 'POST'])
def hi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("punnu.html", name=name)
    # starting and empty input default
    return render_template("punnu.html", name="World")

@app.route('/Sophie/sussusamogus', methods=['GET', 'POST'])
def hey():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sophie.html", name=name)
    # starting and empty input default
    return render_template("sophie.html", name="World")

@app.route('/mini/hello', methods=['GET', 'POST'])
def sup():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sus.html", name=name)
    # starting and empty input default
    return render_template("sus.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=5000)
