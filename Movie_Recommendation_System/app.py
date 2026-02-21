from flask import Flask, render_template, request
import pandas as pd
import requests
app = Flask(__name__)
API_KEY ="f4f019c5"
# Load dataset (make sure movies.csv is in same folder)
movies = pd.read_csv("ml-latest-small/movies.csv")

# Create movie list for dropdown
movie_list = movies["title"].values


# Simple recommendation function
def recommend(movie_name):
    # Just return 5 random movies (temporary logic)
    return movies["title"].sample(5).values
def fetch_poster(movie_name):
    # Remove year from title (Example: "Movie (2000)")
    movie_name = movie_name.split(" (")[0]

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_name}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True" and data.get("Poster") != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

@app.route("/", methods=["GET", "POST"])
def home():
    movies_list = []
    posters = []

    if request.method == "POST":
        selected_movie = request.form["movie"]
        recommendations = recommend(selected_movie)

        for movie in recommendations:
            movies_list.append(movie)
            posters.append(fetch_poster(movie))

    return render_template(
        "index.html",
        movie_list=movie_list,
        movies=movies_list,
        posters=posters
    )


if __name__ == "__main__":
    app.run(debug=True)