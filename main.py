import flask

app=flask.Flask(__name__)

@app.route("/")
def index():
    favoriteTVshows = ["Digimon","Naruto: Shippuden","Sisyphus: The Myth","Fairy Tail","Fresh Off the Boat"]
    images = ["https://m.media-amazon.com/images/M/MV5BNGJhOGJmZGItNjQwZS00MzQ5LTg0MDMtYTc3YzAwMDc4YjFmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_FMjpg_UX1000_.jpg",
    "https://m.media-amazon.com/images/M/MV5BMTE5NzIwMGUtYTE1MS00MDUxLTgyZjctOWVkZDAxM2M4ZWQ4XkEyXkFqcGdeQXVyNjc2NjA5MTU@._V1_FMjpg_UX1000_.jpg",
    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQPz3V4DT7sQvimUTdDRQNCfMs34WFHPI9U2K2MT5AxFHseswPM",
    "https://m.media-amazon.com/images/M/MV5BMzZjNmRhNWQtNTAyYy00Yjk2LWE0NzUtMmYyNTU0YTE5NjJiXkEyXkFqcGdeQXVyNjI4OTE5OTM@._V1_.jpg",
    "https://m.media-amazon.com/images/M/MV5BZDZjYmEwM2MtZmRkYi00YjJmLTgxNDYtZDI3NTgxOGRjZmYzXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg"]
    return flask.render_template("index.html", name="Nahid", favoriteTVshows=favoriteTVshows, length=len(favoriteTVshows), images=images)

app.run(debug=True)