# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
from pathlib import Path
from redditapi import getRedditData
# from api.webapi import api_bp
# create a Flask instance
app = Flask(__name__)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

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
    path = Path(app.root_path) / "static" / "img"
    return render_template("rgb.html", images=image_data(path))

@app.route('/postoftheday/')
def postoftheday():
    return render_template("postoftheday.html", rdata=getRedditData())

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

@app.route('/logicgates')
def logic_gates():
    return render_template("logicgates.html")

@app.route('/bREAKING-nEWS')
def breaking():
    return render_template("breakingnews.html")

@app.route('/youropinioniswrong')
def opinions():
    return render_template("opinions.html")

@app.route('/mindlesspleasure')
def entertainment():
    return render_template("entertainment.html")

@app.route('/fakenews')
def politics():
    return render_template("politics.html")

@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/articles/aaa', methods=['GET', 'POST'])
def article_search():
    if request.form:
        search_word = request.form.get("name")
        if len(search_word) != 0:  # input field has content
            return render_template("articles.html", name=search_word)
    file = open("requirements.txt", "r")
    unsigned(file.read())
    # starting and empty input default
    return render_template("articles.html", name="World")

@app.route('/sample')
def sample():
    return render_template("articles/first.html")

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

@app.errorhandler(404)
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('404.html')