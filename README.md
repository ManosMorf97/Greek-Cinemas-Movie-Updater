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
 &nbsp; ● Title
 &nbsp; ● Description
 &nbsp; ● Original Title
 &nbsp; ● List of Directors
 &nbsp; ● The IMDB link to the profile of each of the directors
All the above information will be stored in a relational database. The data in the database will
be updated each time the process runs.
You are free to include any additional features / optimizations that you may find relevant or
could showcase your skills but please bear in mind that you should cover the core
requirements first before attempting any improvements. Also note that, although it may be
tempting to use ready-made libraries or gems for querying TMDB, we would prefer you to
make direct API requests.

## tools
* Python
* flask
* flask-sqlalchemy
* HTML
* CSS

## instalation
* python -m pip install -r requrements.txt

## app runing
1) python -m flask --app MovieUpdate run
2) open localhost:5000


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

