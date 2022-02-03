import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    favoriteTVshows = ["Digimon","Naruto: Shippuden","Sisyphus: The Myth","Fairy Tail","Fresh Off the Boat"]
    return flask.render_template("index.html", name="Nahid", favoriteTVshows=favoriteTVshows, length=len(favoriteTVshows))

app.run(debug=True)