from flask import Flask, render_template, request, redirect, url_for, session
from recommender import get_recommendations
import pandas as pd

app = Flask(__name__)
app.secret_key = "secret123"  # for sessions

movies_df = pd.read_csv("data/movies.csv")

users = {
    "user1": "pass1",
    "user2": "pass2"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    recommended = []
    if request.method == "POST":
        liked_movie = request.form["movie"]
        recommended = get_recommendations(liked_movie)
    movie_titles = movies_df["title"].tolist()
    return render_template("index.html", movies=movie_titles, recommended=recommended)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
