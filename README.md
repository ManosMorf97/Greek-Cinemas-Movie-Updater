# GreekCinemasMoviesUpdater

## This is a task given by Workable Company to evaluate me for a job position as Junior Software Operations Engineer

## Explanation 
Your objective is to build a small project named MovieData. The application will use the API
from The Movie DB (https://developers.themoviedb.org/3/getting-started). Use the following
API key: bbb0e77b94b09193e6f32d5fac7a3b9c or create a new one on the site.
The goal of this assignment is to implement an application or script that will retrieve and
store movie information.
The application must retrieve a list of the movies currently in theaters in Greece, along with
at least the following attributes:
 &nbsp; ● Title <br>
 &nbsp; ● Description <br>
 &nbsp; ● Original Title <br>
 &nbsp; ● List of Directors <br>
 &nbsp; ● The IMDB link to the profile of each of the directors <br>
All the above information will be stored in a relational database. The data in the database will
be updated each time the process runs.
You are free to include any additional features / optimizations that you may find relevant or
could showcase your skills but please bear in mind that you should cover the core
requirements first before attempting any improvements. Also note that, although it may be
tempting to use ready-made libraries or gems for querying TMDB, we would prefer you to
make direct API requests.

## tools
* Python
* mysql-connector-python
* flask
* flask-sqlalchemy
* HTML
* CSS

## instalation
* python -m pip install -r requrements.txt

## app runing
1) python -m flask --app MovieUpdate run
2) open localhost:5000 on browser.


## Relational Tables
* Movie
  - &nbsp; movie_id (PK)
  - &nbsp; title
  - &nbsp; original_title
  - &nbsp; description
* Director
  - &nbsp; director_id (PK)
  - &nbsp; name
  - &nbsp; movie_id (PK) (FK) Movie(movie_id)
 
 ## Application logic
 1) There are 2 Sets: TMDB and RelationalDB.
 2) An API request is sent to TMDB with region=gr to find the movies that are currently in Theaters in Greece.
 3) Then the movies that are only in the RelationalDB are stored to be deleted, and the movies that are only in the TMDB are stored to be kept.
 4) The movies to be deleted are deleted from Relational DB, and the movies to be kept are inserted in the RelationalDB.
 5) Afterwards, on the recently inserted movies we made requests about movie details keeping the movie_id, to acquire details about directors.
 6) To present the updated info we join the tables Movie and Director and we order the joined table by movie_id.

## Benefits on Implementation
1) Instead of reinventing the wheel creating algorithms from scratch to find the intersection,<br>union, etc the data-type Set is used to find the above.
2) To delete the old records the database is queried using the keyword IN instead of many queries with where.
3) The joined table is sorted via movie_Id attribute, in order to find the directors of each movie faster,<br>and represent them with the movie info, instead to search the directors for every movie.
4) Http-request for directors are made only for movies who have been recently inserted on the Relational DB.
5) The table Movie is cascaded so if a movie is deleted, the rows of director having the id of the<br>deleted movie will be deleted.

