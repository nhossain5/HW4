import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html", name="Nahid")

app.run(debug=True)