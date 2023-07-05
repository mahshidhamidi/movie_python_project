MOVIE RANKING PROJECT 

manage a list of their top 10 favorite movies. Users can rate movies, write reviews, and add new movies to their lists.
## Prerequisites
Make sure you have the following installed before running the application:
- Python 3
- Flask
- Flask-Bootstrap
- Flask-SQLAlchemy
- Flask-WTF
- Requests
## Getting Started
1. Clone the repository to your local machine.
2. Install the required dependencies using pip or any other package manager.
3. Obtain an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/) and replace `api_key` in the code with your API key.
4. Run the Flask application using the command `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.
## Features
- Display a list of top 10 movies with their ranking, title, release year, rating, review, and description.
- Sort movies by rating in descending order.
- Edit the rating and review of a movie.
- Delete a movie from the list.
- Add a new movie by searching TMDb API.
- Select a movie from the search results to view details and add it to the list.
- Store movie data in a SQLite database.
## Usage
1. Launch the application and navigate to the home page.
2. Explore the list of top 10 movies.
3. To rate and review a movie, click on the "Update" button on the movie card. Enter your rating and review in the form and submit it.
4. To delete a movie, click on the "Delete" button on the movie card. The movie will be removed from the list.
5. To add a new movie, click on the "Add Movie" button on the home page. Enter the movie title in the form and submit it. The application will fetch movie details from the TMDb API and display a list of search results.
6. Select a movie from the search results to view its details. Click on the "Update" button to add the movie to your list.
7. You can always access the home page to view and manage your list of top 10 movies.
